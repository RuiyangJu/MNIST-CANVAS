# [mnist-canvas page](https://ruiyangju.github.io/mnist-canvas/)

<p align="center">
  <img src="mnist.jpg" width="640" title="mnist">
</p>

## Introduction
A web canvas that you can draw and see the MNIST classification result distribution.

## Requirements
* Python 3.6+
* Pytorch 0.4.0+
* Pandas 0.23.4+
* NumPy 1.14.3+

## Usage
  Train the model:
  
      python3 main.py
  
  Convert pth to onnx:
  
      python3 convert.py

  optional arguments:
  
      --lr                default=1e-3    learning rate
      --epoch             default=20     number of epochs tp train for
      --trainBatchSize    default=128     training batch size
      --testBatchSize     default=128     test batch size
 
## Config
###### Optimizer 
__Adam Optimizer__
###### Learning Rate
__1e-3__ for [1,10] epochs <br>
__5e-4__ for [10,20] epochs <br>
      
## Results
For more details, you can read [mobilenetv2_detail.txt](mobilenetv2_detail.txt)

| Model | MNIST Test Accuracy (%) | FLOPs (G) | MAdd (G) | Memory (MB) | #Params (M) |
| MobileNetV2 | 14.06 | 2.42 | 4.75 | 384.78 | 2.37 |

## 上課內容：
* HTML -> 網站上的物件有哪些
* CSS -> 物件要長怎樣
* javascript -> 物件怎麼動
