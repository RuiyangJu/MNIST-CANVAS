import torch
import torch.nn as nn
import torch.nn.functional as F

class LinearBottleNeck(nn.Module):
    def __init__(self, in_channels, out_channels, stride, t=2):
        super().__init__()

        self.residual = nn.Sequential(
            nn.Conv2d(in_channels, in_channels * t, 1),
            nn.BatchNorm2d(in_channels * t),
            nn.ReLU6(inplace=True),

            nn.Conv2d(in_channels * t, in_channels * t, 3, stride=stride, padding=1, groups=in_channels * t),
            nn.BatchNorm2d(in_channels * t),
            nn.ReLU6(inplace=True),

            nn.Conv2d(in_channels * t, out_channels, 1),
            nn.BatchNorm2d(out_channels)
        )

        self.stride = stride
        self.in_channels = in_channels
        self.out_channels = out_channels

    def forward(self, x):

        residual = self.residual(x)

        if self.stride == 1 and self.in_channels == self.out_channels:
            residual += x

        return residual

class MobileNetV2(nn.Module):

    def __init__(self, class_num=10):
        super().__init__()

        self.pre = nn.Sequential(
            nn.Conv2d(1, 16, 1, padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU6(inplace=True)
        )

        self.stage1 = LinearBottleNeck(16, 8, 1, 1)
        self.stage2 = self._make_stage(2, 8, 12, 2, 2)
        self.stage3 = self._make_stage(2, 12, 16, 2, 2)
        self.stage4 = self._make_stage(2, 16, 24, 2, 2)
        self.stage5 = LinearBottleNeck(24, 32, 1, 2)

        self.conv1 = nn.Sequential(
            nn.Conv2d(32, 64, 1),
            nn.BatchNorm2d(64),
            nn.ReLU6(inplace=True)
        )

        self.conv2 = nn.Conv2d(64, class_num, 1)

    def forward(self, x):
        x = self.pre(x)
        x = self.stage1(x)
        x = self.stage2(x)
        x = self.stage3(x)
        x = self.stage4(x)
        x = self.stage5(x)
        x = self.conv1(x)
        x = F.adaptive_avg_pool2d(x, 1)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)

        return x

    def _make_stage(self, repeat, in_channels, out_channels, stride, t):

        layers = []
        layers.append(LinearBottleNeck(in_channels, out_channels, stride, t))

        while repeat - 1:
            layers.append(LinearBottleNeck(out_channels, out_channels, 1, t))
            repeat -= 1

        return nn.Sequential(*layers)

def mobilenetv2():
    return MobileNetV2()