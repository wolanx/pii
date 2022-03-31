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


class MyModel(nn.Module):
    def __init__(self) -> None:
        super(MyModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, (3, 3), (1, 1))
        self.conv2 = nn.Conv2d(32, 64, (3, 3), (1, 1))
        self.dropout1 = nn.Dropout(.25)
        self.dropout2 = nn.Dropout(.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)

        x = F.max_pool2d(x, 2)
        # x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        # x = self.dropout2(x)
        x = self.fc2(x)

        ret = F.log_softmax(x, dim=1)
        return ret


data, target = train_loader.dataset[0]

model: nn.Module = MyModel()
model.load_state_dict(torch.load('mnist.pth'))
model.eval()

with torch.no_grad():
    ret = model(data)
    print(ret)

print()
