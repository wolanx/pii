import torch.nn.functional
from torch import nn


def Train_Epoch(train_loader, data, epoch, loss):
    # Train Epoch: 2 [16640/60000 (28%)]	Loss: 0.142410
    batch_idx = 123
    print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
        epoch,
        batch_idx * len(data), len(train_loader.dataset), 100. * batch_idx / len(train_loader),
        loss.item()))


def train(model: nn.Module, device, train_loader, optimizer: torch.optim.Optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()

        output = model(data)
        loss = nn.functional.nll_loss(output, target)
        loss.backward()

        optimizer.step()

        if batch_idx % 10 == 0:
            # Train Epoch: 2 [16640/60000 (28%)]	Loss: 0.142410
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch,
                batch_idx * len(data), len(train_loader.dataset), 100. * batch_idx / len(train_loader),
                loss.item()))
