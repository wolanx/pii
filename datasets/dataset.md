FLOPs

# ILSVRC

## PASCAL VOC

- torch imagenet example
- size 160g
- ILSVRC
- https://www.kaggle.com/competitions/imagenet-object-localization-challenge/data

# torchvision

## MNIST

- torchvision.datasets.MNIST(root="../datasets", train=True, download=True)
- (60000, 28, 28)

## CIFAR10

- torchvision.datasets.CIFAR10(root="../datasets", train=True, download=True)
- (50000, 32, 32, 3) + (10000, 32, 32, 3)
- 60000 = 10大类 * 每类6000
- http://www.cs.toronto.edu/~kriz/cifar.html
- 163 MB

```text
{'airplane': 0, 'automobile': 1, 'bird': 2, 'cat': 3, 'deer': 4, 'dog': 5, 'frog': 6, 'horse': 7, 'ship': 8, 'truck': 9}
```

## CIFAR100

- torchvision.datasets.CIFAR100(root="../datasets", train=True, download=True)
- (50000, 32, 32, 3) + (10000, 32, 32, 3)
- 60000 = 10大类 * 10小类 * 每类600
- http://www.cs.toronto.edu/~kriz/cifar.html
- 161 MB

|Superclass|Classes|
|----------|------|
|aquatic mammals | beaver, dolphin, otter, seal, whale|
|fish | aquarium fish, flatfish, ray, shark, trout|
|flowers | orchids, poppies, roses, sunflowers, tulips|
|food containers | bottles, bowls, cans, cups, plates|
|fruit and vegetables | apples, mushrooms, oranges, pears, sweet peppers|
|household electrical devices | clock, computer keyboard, lamp, telephone, television|
|household furniture | bed, chair, couch, table, wardrobe|
|insects | bee, beetle, butterfly, caterpillar, cockroach|
|large carnivores | bear, leopard, lion, tiger, wolf|
|large man-made outdoor things | bridge, castle, house, road, skyscraper|
|large natural outdoor scenes | cloud, forest, mountain, plain, sea|
|large omnivores and herbivores | camel, cattle, chimpanzee, elephant, kangaroo|
|medium-sized mammals | fox, porcupine, possum, raccoon, skunk|
|non-insect invertebrates | crab, lobster, snail, spider, worm|
|people | baby, boy, girl, man, woman|
|reptiles | crocodile, dinosaur, lizard, snake, turtle|
|small mammals | hamster, mouse, rabbit, shrew, squirrel|
|trees | maple, oak, palm, pine, willow|
|vehicles 1 | bicycle, bus, motorcycle, pickup truck, train|
|vehicles 2 | lawn-mower, rocket, streetcar, tank, tractor|

```text
{'apple': 0, 'aquarium_fish': 1, 'baby': 2, 'bear': 3, 'beaver': 4, 'bed': 5, 'bee': 6, 'beetle': 7, 'bicycle': 8, 'bottle': 9, 'bowl': 10, 'boy': 11, 'bridge': 12, 'bus': 13, 'butterfly': 14, 'camel': 15, 'can': 16, 'castle': 17, 'caterpillar': 18, 'cattle': 19, 'chair': 20, 'chimpanzee': 21, 'clock': 22, 'cloud': 23, 'cockroach': 24, 'couch': 25, 'crab': 26, 'crocodile': 27, 'cup': 28, 'dinosaur': 29, 'dolphin': 30, 'elephant': 31, 'flatfish': 32, 'forest': 33, 'fox': 34, 'girl': 35, 'hamster': 36, 'house': 37, 'kangaroo': 38, 'keyboard': 39, 'lamp': 40, 'lawn_mower': 41, 'leopard': 42, 'lion': 43, 'lizard': 44, 'lobster': 45, 'man': 46, 'maple_tree': 47, 'motorcycle': 48, 'mountain': 49, 'mouse': 50, 'mushroom': 51, 'oak_tree': 52, 'orange': 53, 'orchid': 54, 'otter': 55, 'palm_tree': 56, 'pear': 57, 'pickup_truck': 58, 'pine_tree': 59, 'plain': 60, 'plate': 61, 'poppy': 62, 'porcupine': 63, 'possum': 64, 'rabbit': 65, 'raccoon': 66, 'ray': 67, 'road': 68, 'rocket': 69, 'rose': 70, 'sea': 71, 'seal': 72, 'shark': 73, 'shrew': 74, 'skunk': 75, 'skyscraper': 76, 'snail': 77, 'snake': 78, 'spider': 79, 'squirrel': 80, 'streetcar': 81, 'sunflower': 82, 'sweet_pepper': 83, 'table': 84, 'tank': 85, 'telephone': 86, 'television': 87, 'tiger': 88, 'tractor': 89, 'train': 90, 'trout': 91, 'tulip': 92, 'turtle': 93, 'wardrobe': 94, 'whale': 95, 'willow_tree': 96, 'wolf': 97, 'woman': 98, 'worm': 99}
```

# 其他

## VOC2012

- Pascal VOC 2012
- 语义分割数据集
- http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
- Pytorch实现VOC数据集的Dataset https://www.jianshu.com/p/fae7aa07a588
- 1.90 GB

```text
// tree
Annotations 17152个xml
ImageSets
JPEGImages 17152张jpg
SegmentationClass 同一类一个色，两个人一个色
SegmentationObject 同一类不同对象不同色，两个人两个色

// G:/conda/envs/py39/lib/site-packages/torchvision/datasets/voc.py:18
"2012": {
    "url": "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar",
    "filename": "VOCtrainval_11-May-2012.tar",
    "md5": "6cd6e144f989b92b3379bac3b3de84fd",
    "base_dir": os.path.join("VOCdevkit", "VOC2012"),
},
```
