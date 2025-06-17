import torch
from torch import nn

class alexnet(nn.Module):
    def __init__(self):
        super(alexnet, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 48, kernel_size=11, stride=4),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(48, 128, kernel_size=5),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(128, 192, kernel_size=3),
            nn.Conv2d(192, 192, kernel_size=3),
            nn.Conv2d(192, 128, kernel_size=3),
            nn.MaxPool2d(kernel_size=2),
            nn.Flatten(),
            nn.Linear(128 * 3 * 3, 2048),
            nn.Linear(2048, 1024),
            nn.Linear(1024, 10),
        )

    def forward(self, x):
        y = self.model(x)
        return y

if __name__ == 'main':
    x = torch.randn(1, 3, 224, 224)
    alex = alexnet()
    y = alex(x)
    print(y.shape)

