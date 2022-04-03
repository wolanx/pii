import torch
import torch.nn.functional as F
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
    # transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))  # 归一化到(0,1) 分布到(-1,1)
])
dataset1 = torchvision.datasets.MNIST(root="../../data", train=True, download=False, transform=transform)

train_loader: DataLoader = torch.utils.data.DataLoader(dataset1, batch_size=64, shuffle=True)


class MyModel2(nn.Module):  # e1 86% e5 92%
    def __init__(self) -> None:
        super().__init__()
        self.fc1 = nn.Linear(784, 200)
        self.fc2 = nn.Linear(200, 200)
        self.fc3 = nn.Linear(200, 10)

    def forward(self, x):  # 64, 1, 28, 28 第一个 64 是 batch_size
        x = torch.flatten(x, 1)  # 728
        x = self.fc1(x)  # 200
        x = self.fc2(x)  # 200
        x = self.fc3(x)  # 10

        x = F.log_softmax(x, dim=1)  # 10
        return x


data, target = train_loader.dataset[0]

print(data.size(), target)

model: nn.Module = MyModel2()
model.load_state_dict(torch.load('mnist.pth'))
model.eval()

for i in range(50):
    data, target = train_loader.dataset[i]
    output = model(data)
    pred = torch.argmax(output, dim=1, keepdim=False)
    print(target, pred.item())
