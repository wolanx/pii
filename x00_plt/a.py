import numpy as np
from matplotlib import pyplot as plt
import xml.etree.ElementTree as ET

self.classes = (
    'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow',
    'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
)
self.class_to_idx = {_class: i for i, _class in enumerate(self.classes)}

anno = ET.parse(os.path.join(self.root, 'Annotations', f'{name}.xml'))

bbox = []
for obj in anno.findall('object'):
    cname = obj.find('name').text.lower().strip()
    sid = self.classes.index(cname)
    boxEl = obj.find('bndbox')
    box = []
    for tag in ('ymin', 'xmin', 'ymax', 'xmax'):
        box.append(int(boxEl.find(tag).text) - 1)

    box.append(sid)
    bbox.append(box)

bbox = np.stack(bbox).astype(np.float32)

ax = plt.gca()
for (y1, x1, y2, x2, cid) in bbox:
    label = dataset1.classes[int(cid)]
    rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, fill=False, edgecolor='red', linewidth=1)
    plt.annotate(label, xy=(x1, y2 + 20), color='red')
    ax.add_patch(rect)