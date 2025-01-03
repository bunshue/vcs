"""
維基百科上的範例
"""

# 做 N X M 陣列的運算

import torch

N, M = 2, 3

device = torch.device("cpu")  # 本次在CPU上執行所有的計算
# device = torch.device("cuda:0") # 本次在GPU上執行所有的計算

print("建立隨機(NXM)陣列a")
a = torch.randn(N, M, device=device, dtype=torch.float)
print(a)

print("建立隨機(NXM)陣列b")
b = torch.randn(N, M, device=device, dtype=torch.float)
print(b)

print("a * b")
print(a * b)

print("a.sum() :", a.sum())
print("a.max() :", a.max())
print("a[1, 2] :", a[1, 2])
