import os

import torch
import torchvision
from PIL import Image
from matplotlib import pyplot as plt
from torchvision.transforms import transforms

# model = torch.hub.load('pytorch/vision:v0.10.0', 'deeplabv3_resnet50', pretrained=True)
model = torchvision.models.segmentation.deeplabv3_resnet50(pretrained=True, progress=True)
# model.load_state_dict(torch.load('temp.pth'))
model.cuda()
model.eval()

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
