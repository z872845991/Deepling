# Pytorch中@和*的用处

## 1. '@' 是用来的tensor进行矩阵乘法运算的：

```python
import torch
d = 2
n=50
X = torch.randn(n,d)
true_w = torch.tensor([[-1.0],[2.0]])
y = X @ true_w + torch.randn(n,1)*0.1
print(X.shape)
print(y.shape)
print(true_w.shape)
```

```python
torch.Size([50, 2])
torch.Size([50, 1])
torch.Size([2, 1])
```

## 2. '*' 用来的tensor中矩阵中的对应元素之间相乘：

```python
x = torch.tensor([[1,2],[3,4]])
y = torch.tensor([[2,1],[4,3]])
c = x*y
print("x_shape",x.shape)
print("y_shape",y.shape)
print("c_shape",c.shape)
print(c)
```

```python
x_shape torch.Size([2, 2])
y_shape torch.Size([2, 2])
c_shape torch.Size([2, 2])
tensor([[ 2,  2],
        [12, 12]])
```



