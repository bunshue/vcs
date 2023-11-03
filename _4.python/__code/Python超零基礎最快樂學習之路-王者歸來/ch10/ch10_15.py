# ch10_15.py
A = {1, 2, 3, 4, 5}             # 定義集合A
B = {3, 4, 5, 6, 7}             # 定義集合B
# 將difference( )應用在A集合
A_B = A.difference(B)           # A-B的差集
print("A-B的差集是 ", A_B)    
# 將difference( )應用在B集合
B_A = B.difference(A)           # B-A的差集
print("B-A的差集是 ", B_A)

