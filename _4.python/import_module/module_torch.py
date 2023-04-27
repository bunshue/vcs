'''
維基百科上的範例
'''
import torch

dtype = torch.float
device = torch.device("cpu") # 本次在CPU上执行所有的计算
# device = torch.device("cuda:0") # 本次在GPU上执行所有的计算

# 建立一个张量并用随机数填充这个张量
a = torch.randn(2, 3, device=device, dtype=dtype)
print(a) # 输出张量a
# 输出: tensor([[-1.1884,  0.8498, -1.7129],
#                  [-0.8816,  0.1944,  0.5847]])

# 建立一个张量并用随机数填充这个张量
b = torch.randn(2, 3, device=device, dtype=dtype)
print(b) # Output of tensor B
# 输出: tensor([[ 0.7178, -0.8453, -1.3403],
#                  [ 1.3262,  1.1512, -1.7070]])

print(a*b) # 输出两个张量的乘积
# 输出: tensor([[-0.8530, -0.7183,  2.58],
#                  [-1.1692,  0.2238, -0.9981]])

print(a.sum()) # 输出在张量a中所有元素的总和
# 输出: tensor(-2.1540)

print(a[1,2]) # 输出第2行第3列（0起始）的元素
# 输出: tensor(0.5847)

print(a.max()) # 输出在张量a中的极大值
# 输出: tensor(-1.7129)




