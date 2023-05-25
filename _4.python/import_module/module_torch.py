'''
維基百科上的範例
'''
import torch

dtype = torch.float
device = torch.device("cpu") # 本次在CPU上執行所有的計算
# device = torch.device("cuda:0") # 本次在GPU上執行所有的計算

# 建立一個張量並用隨機數填充這個張量
a = torch.randn(2, 3, device = device, dtype = dtype)
print(a) # 輸出張量a
# 輸出: tensor([[-1.1884,  0.8498, -1.7129],
#                  [-0.8816,  0.1944,  0.5847]])

# 建立一個張量並用隨機數填充這個張量
b = torch.randn(2, 3, device = device, dtype = dtype)
print(b) # Output of tensor B
# 輸出: tensor([[ 0.7178, -0.8453, -1.3403],
#                  [ 1.3262,  1.1512, -1.7070]])

print(a*b) # 輸出兩個張量的乘積
# 輸出: tensor([[-0.8530, -0.7183,  2.58],
#                  [-1.1692,  0.2238, -0.9981]])

print(a.sum()) # 輸出在張量a中所有元素的總和
# 輸出: tensor(-2.1540)

print(a[1,2]) # 輸出第2行第3列（0起始）的元素
# 輸出: tensor(0.5847)

print(a.max()) # 輸出在張量a中的極大值
# 輸出: tensor(-1.7129)



