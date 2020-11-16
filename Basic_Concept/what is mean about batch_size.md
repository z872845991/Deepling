# For example

## Batch size

```python
 for batch_idx, (features, targets) in enumerate(train_loader,1):
        print('The %3d :'%(batch_idx),'\t',len(features),'\t',len(targets))
```

在原文档中，batch size被设置为128，也就是在进行训练、测试时，每128条数据一组，就是这些数据一起训练。

```
The   1 : 	 128 	 128
The   2 : 	 128 	 128
The   3 : 	 128 	 128
The   4 : 	 128 	 128
```

执行这个循环之后，会得到上面的结果，原文档中有469条。这里只是简单的输出看一下。

`enumerate` 该函数的第二项是从索引从的开始位置，设置为1，batch_idx 将从1开始。

batch_idx指示的就是现在在训练第几个batch块。

就好比一个厨师，要做西红柿炒鸡蛋，以鸡蛋为例，batch size就好像是每次要炒几个鸡蛋。

而batch_idx就是厨师完成了几盘；

而train_loader里面的数据，就好像是菜篮子里的鸡蛋。

### 注：上文提到的原文档，即Deepling/mnist中的`mnist_jesse.ipynb`