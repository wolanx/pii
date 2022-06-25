import os
import xml.etree.ElementTree as ET

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import torch
import torchvision.transforms as transforms
from PIL import Image
from torch import nn
from torch.utils.data import Dataset


class VOCDataset(Dataset):
    def __init__(self, root, train=True, transform=None):
        super(VOCDataset, self).__init__()
        self.root = root
        self.transform = transform
        self.classes = (
            'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow',
            'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
        )
        self.class_to_idx = {_class: i for i, _class in enumerate(self.classes)}

        suffix = 'trainval' if train else 'val'

        files = os.path.join(root, 'ImageSets', 'Segmentation', f'{suffix}.txt')
        # files = os.path.join(root, f'a.txt')  # fixme
        self.files = [id_.strip() for id_ in open(files)]

    def __getitem__(self, sid):
        name = self.files[sid]
        anno = ET.parse(os.path.join(self.root, 'Annotations', f'{name}.xml'))

        # bbox = []
        # for obj in anno.findall('object'):
        #     cname = obj.find('name').text.lower().strip()
        #     sid = self.classes.index(cname)
        #     boxEl = obj.find('bndbox')
        #     box = []
        #     for tag in ('ymin', 'xmin', 'ymax', 'xmax'):
        #         box.append(int(boxEl.find(tag).text) - 1)
        #
        #     box.append(sid)
        #     bbox.append(box)
        #
        # bbox = np.stack(bbox).astype(np.float32)

        img_file = os.path.join(self.root, 'JPEGImages', f'{name}.jpg')
        mask_file = os.path.join(self.root, 'SegmentationClass', f'{name}.png')
        img = Image.open(img_file)
        mask = Image.open(mask_file)
        img = img.convert("RGB")

        if self.transform:
            # img, mask = self.transform(img, mask)
            img = self.transform(img)
            # mask = self.transform(mask)
            mask = transforms.Compose([transforms.ToTensor()])(mask)

        return img, mask  # , bbox, name

    def __len__(self):
        return len(self.files)


def imshow(img, bbox, name):
    # (c, h, w) => (h, w, c) (3, 375, 500) => (375, 500, 3)
    img = img.permute(1, 2, 0)
    plt.imshow(img)  # img.shape (w, h, c)
    ax = plt.gca()
    for (y1, x1, y2, x2, cid) in bbox:
        label = dataset1.classes[int(cid)]
        rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, fill=False, edgecolor='red', linewidth=1)
        plt.annotate(label, xy=(x1, y2 + 20), color='red')
        ax.add_patch(rect)

    plt.show()


img, mask = train_loader.dataset[6]  # , bbox, name
# print(f"target: {name}")
imshow(img, [], 'name')
# imshow(mask, [], 'name')
plt.imshow(mask)

img_file = os.path.join("../demo3-7_use_cnn", 'dog.jpg')
name = '2008_002762'
img_file = os.path.join("../../datasets" + "/VOCdevkit/VOC2012", 'JPEGImages', f'{name}.jpg')
input_image = Image.open(img_file)
plt.imshow(input_image)
plt.show()
input_image = input_image.convert("RGB")

preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0)

with torch.no_grad():
    output = model(input_batch.cuda())
output = output['out'][0]
output_predictions = output.argmax(0)
palette = torch.tensor([2 ** 25 - 1, 2 ** 15 - 1, 2 ** 21 - 1])
colors = torch.as_tensor([i for i in range(21)])[:, None] * palette
colors = (colors % 255).numpy().astype("uint8")

r = Image.fromarray(output_predictions.byte().cpu().numpy())  # .resize((128, 128))
r.putpalette(colors)

plt.imshow(output_predictions.cpu())
plt.show()
plt.imshow(r)
plt.show()


class _ImagePool(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.conv = _ConvBnReLU(in_ch, out_ch, 1, 1, 0, 1)

    def forward(self, x):
        _, _, H, W = x.shape
        h = self.pool(x)
        h = self.conv(h)
        h = F.interpolate(h, size=(H, W), mode="bilinear", align_corners=False)
        return h


class _ASPP(nn.Module):
    """
    Atrous spatial pyramid pooling with image-level feature
    """

    def __init__(self, in_ch, out_ch, rates):
        super(_ASPP, self).__init__()
        self.stages = nn.Module()
        self.stages.add_module("c0", _ConvBnReLU(in_ch, out_ch, 1, 1, 0, 1))
        for i, rate in enumerate(rates):
            self.stages.add_module(
                "c{}".format(i + 1),
                _ConvBnReLU(in_ch, out_ch, 3, 1, padding=rate, dilation=rate),
            )
        self.stages.add_module("imagepool", _ImagePool(in_ch, out_ch))

    def forward(self, x):
        return torch.cat([stage(x) for stage in self.stages.children()], dim=1)


class DeepLabV3Plus(nn.Module):
    """
    DeepLab v3+: Dilated ResNet with multi-grid + improved ASPP + decoder
    """

    def __init__(self, n_classes, n_blocks, atrous_rates, multi_grids, output_stride):
        super(DeepLabV3Plus, self).__init__()

        # Stride and dilation
        if output_stride == 8:
            s = [1, 2, 1, 1]
            d = [1, 1, 2, 4]
        elif output_stride == 16:
            s = [1, 2, 2, 1]
            d = [1, 1, 1, 2]

        # Encoder
        ch = [64 * 2 ** p for p in range(6)]
        self.layer1 = _Stem(ch[0])
        self.layer2 = _ResLayer(n_blocks[0], ch[0], ch[2], s[0], d[0])
        self.layer3 = _ResLayer(n_blocks[1], ch[2], ch[3], s[1], d[1])
        self.layer4 = _ResLayer(n_blocks[2], ch[3], ch[4], s[2], d[2])
        self.layer5 = _ResLayer(n_blocks[3], ch[4], ch[5], s[3], d[3], multi_grids)
        self.aspp = _ASPP(ch[5], 256, atrous_rates)
        concat_ch = 256 * (len(atrous_rates) + 2)
        self.add_module("fc1", _ConvBnReLU(concat_ch, 256, 1, 1, 0, 1))

        # Decoder
        self.reduce = _ConvBnReLU(256, 48, 1, 1, 0, 1)
        self.fc2 = nn.Sequential(
            OrderedDict(
                [
                    ("conv1", _ConvBnReLU(304, 256, 3, 1, 1, 1)),
                    ("conv2", _ConvBnReLU(256, 256, 3, 1, 1, 1)),
                    ("conv3", nn.Conv2d(256, n_classes, kernel_size=1)),
                ]
            )
        )

    def forward(self, x):
        h = self.layer1(x)
        h = self.layer2(h)
        h_ = self.reduce(h)
        h = self.layer3(h)
        h = self.layer4(h)
        h = self.layer5(h)
        h = self.aspp(h)
        h = self.fc1(h)
        h = F.interpolate(h, size=h_.shape[2:], mode="bilinear", align_corners=False)
        h = torch.cat((h, h_), dim=1)
        h = self.fc2(h)
        h = F.interpolate(h, size=x.shape[2:], mode="bilinear", align_corners=False)
        return h


class _ConvBnReLU(nn.Sequential):
    """
    Cascade of 2D convolution, batch norm, and ReLU.
    """

    def __init__(
            self, in_ch, out_ch, kernel_size, stride, padding, dilation, relu=True
    ):
        super(_ConvBnReLU, self).__init__()
        self.add_module(
            "conv",
            nn.Conv2d(
                in_ch, out_ch, kernel_size, stride, padding, dilation, bias=False
            ),
        )
        self.add_module("bn", nn.BatchNorm2d(out_ch, eps=1e-5, momentum=0.999))

        if relu:
            self.add_module("relu", nn.ReLU())


class _Bottleneck(nn.Module):
    """
    Bottleneck block of MSRA ResNet.
    """

    def __init__(self, in_ch, out_ch, stride, dilation, downsample):
        super(_Bottleneck, self).__init__()
        mid_ch = out_ch // 4
        self.reduce = _ConvBnReLU(in_ch, mid_ch, 1, stride, 0, 1, True)
        self.conv3x3 = _ConvBnReLU(mid_ch, mid_ch, 3, 1, dilation, dilation, True)
        self.increase = _ConvBnReLU(mid_ch, out_ch, 1, 1, 0, 1, False)
        self.shortcut = (
            _ConvBnReLU(in_ch, out_ch, 1, stride, 0, 1, False)
            if downsample
            else lambda x: x  # identity
        )

    def forward(self, x):
        h = self.reduce(x)
        h = self.conv3x3(h)
        h = self.increase(h)
        h += self.shortcut(x)
        return F.relu(h)


class _ResLayer(nn.Sequential):
    """
    Residual layer with multi grids
    """

    def __init__(self, n_layers, in_ch, out_ch, stride, dilation, multi_grids=None):
        super(_ResLayer, self).__init__()

        if multi_grids is None:
            multi_grids = [1 for _ in range(n_layers)]
        else:
            assert n_layers == len(multi_grids)

        # Downsampling is only in the first block
        for i in range(n_layers):
            self.add_module(
                "block{}".format(i + 1),
                _Bottleneck(
                    in_ch=(in_ch if i == 0 else out_ch),
                    out_ch=out_ch,
                    stride=(stride if i == 0 else 1),
                    dilation=dilation * multi_grids[i],
                    downsample=(True if i == 0 else False),
                ),
            )


class _Stem(nn.Sequential):
    """
    The 1st conv layer.
    Note that the max pooling is different from both MSRA and FAIR ResNet.
    """

    def __init__(self, out_ch):
        super(_Stem, self).__init__()
        self.add_module("conv1", _ConvBnReLU(3, out_ch, 7, 2, 3, 1))
        self.add_module("pool", nn.MaxPool2d(3, 2, 1, ceil_mode=True))


# model = DeepLabV3Plus(
#     n_classes=21,
#     n_blocks=[3, 4, 23, 3],
#     atrous_rates=[6, 12, 18],
#     multi_grids=[1, 2, 4],
#     output_stride=16,
# )
model = DeepLab(backbone='mobilenet', output_stride=16)
model.cuda()
# print(model)
