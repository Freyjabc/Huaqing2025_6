# 完整的模型训练套路(以CIFAR10为例)
import time
import torch.optim
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from dataset.dataset import ImageTxtDataset
from torchvision.transforms import transforms
from model import *

# 检查并设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 准备数据集
train_data = ImageTxtDataset(r"D:\实习\深度学习基础\dataset\train.txt",
                             r"D:\实习\深度学习基础\dataset\Images2\train",
                             transforms.Compose([transforms.Resize(256),
                                                 transforms.RandomHorizontalFlip(),
                                                 transforms.ToTensor(),
                                                 transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                                      std=[0.229, 0.224, 0.225])
                                                 ])
                             )

test_data = ImageTxtDataset(r"D:\实习\深度学习基础\dataset\val.txt",
                            r"D:\实习\深度学习基础\dataset\Images2\val",
                            transforms.Compose([transforms.Resize(256),
                                                transforms.RandomHorizontalFlip(),
                                                transforms.ToTensor(),
                                                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                                     std=[0.229, 0.224, 0.225])
                                                ])
                            )

# 数据集长度
train_data_size = len(train_data)
test_data_size = len(test_data)
print(f"训练数据集的长度{train_data_size}")
print(f"测试数据集的长度{test_data_size}")

# 加载数据集
train_loader = DataLoader(train_data, batch_size=64)
test_loader = DataLoader(test_data, batch_size=64)

# 创建网络模型并移动到设备
chen = Chen().to(device)

# 创建损失函数
loss_fn = nn.CrossEntropyLoss().to(device)

# 优化器
learning_rate = 0.01
optim = torch.optim.SGD(chen.parameters(), lr=learning_rate)

# 设置训练网络的一些参数
total_train_step = 0
total_test_step = 0
epoch = 10

# 添加tensorboard
writer = SummaryWriter("../logs_train")

# 添加开始时间
start_time = time.time()

for i in range(epoch):
    print(f"-----第{i + 1}轮训练开始-----")
    # 训练步骤
    chen.train()  # 设置为训练模式
    for data in train_loader:
        imgs, targets = data
        # 将数据移动到设备
        imgs = imgs.to(device)
        targets = targets.to(device)

        outputs = chen(imgs)
        loss = loss_fn(outputs, targets)

        # 优化器优化模型
        optim.zero_grad()
        loss.backward()
        optim.step()

        total_train_step += 1
        if total_train_step % 500 == 0:
            print(f"第{total_train_step}的训练的loss:{loss.item()}")
            writer.add_scalar("train_loss", loss.item(), total_train_step)

    end_time = time.time()
    print(f"训练时间{end_time - start_time}")

    # 测试步骤
    chen.eval()  # 设置为评估模式
    total_test_loss = 0.0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_loader:
            imgs, targets = data
            # 将数据移动到设备
            imgs = imgs.to(device)
            targets = targets.to(device)

            outputs = chen(imgs)
            loss = loss_fn(outputs, targets)
            total_test_loss += loss.item()
            accuracy = (outputs.argmax(1) == targets).sum()
            total_accuracy += accuracy

    print(f"整体测试集上的loss:{total_test_loss}")
    print(f"整体测试集上的正确率：{total_accuracy / test_data_size}")
    writer.add_scalar("test_loss", total_test_loss, total_test_step)
    writer.add_scalar("test_accuracy", total_accuracy / test_data_size, total_test_step)
    total_test_step += 1

    # 保存每一轮训练模型
    torch.save(chen.state_dict(), f"model_save\\chen_{i}.pth")  # 推荐保存state_dict而不是整个模型
    print("模型已保存")

writer.close()