# ch1_1.py
import numpy as np

row1 = [1, 2, 3]
arr1 = np.array(row1, ndmin=2)
print(f"陣列維度 = {arr1.ndim}")
print(f"陣列外型 = {arr1.shape}")
print(f"陣列大小 = {arr1.size}")
print("陣列內容")
print(arr1)
print("-"*70)
row2 = [4, 5, 6]
arr2 = np.array([row1,row2], ndmin=2)
print(f"陣列維度 = {arr2.ndim}")
print(f"陣列外型 = {arr2.shape}")
print(f"陣列大小 = {arr2.size}")
print("陣列內容")
print(arr2)










 
