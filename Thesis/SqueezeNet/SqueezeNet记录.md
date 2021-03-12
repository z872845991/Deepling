## SqueezeNet

- Fire module 

  > 组成：
  >
  > - *squeeze* convolution: 1*1 filters
  > - *expand* convolution: 1\*1 and 3\*3 filters
  >
  > ![image-20210311192430665](C:\Users\z8728\AppData\Roaming\Typora\typora-user-images\image-20210311192430665.png)
  >
  > > We expose three tunable dimensions (hyperparameters) in a Fire
  > > module: s1x1, e1x1, and e3x3. In a Fire module, s1x1is the number of filters in the squeeze layer
  > > (all 1x1), e1x1is the number of 1x1 filters in the expand layer, and e3x3is the number of 3x3 filters
  > > in the expand layer. When we use Fire modules we set s1x1to be less than (e1x1+ e3x3), so the
  > > squeeze layer helps to limit the number of input channels to the 3x3 filters, as per Strategy 2 from
  > > Section 3.1.

- 重构CNN的三个主要策略：

  - 用1\*1的卷积核代替3\*3的卷积核
  - 减少输入层的通道数量
  - 将降采样的时间滞后

- Details

  - 我们在输入数据中添加1像素的零填充边界到expand的3×3过滤器,以保证产生和1*1过滤器相同效果的高度和宽度。
  - 不使用全连接层
  
- 总结：在本文中，我们将ImageNet作为一个目标数据集。然而，将imagenet训练的CNN表示应用于各种应用程序，如细粒度对象识别、图像中的标识识别和生成关于图像的句子，已经成为一种常见的做法。经过ImageNet训练的cnn也被应用于许多与自动驾驶相关的应用，包括图像和视频中的行人和车辆检测，以及道路形状的分割。我们认为，SqueezeNet将是CNN架构在各种应用中的一个很好的候选，特别是在那些模型尺寸较小的应用中。


