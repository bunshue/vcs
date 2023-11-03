# ch10_11.py
A = {1, 2, 3, 4, 5}         # 定義集合A
B = {3, 4, 5, 6, 7}         # 定義集合B
# 將intersection( )應用在A集合
AB = A.intersection(B)      # A和B的交集
print("A和B的交集是 ", AB)
# 將intersection( )應用在B集合
BA = B.intersection(A)      # B和A的交集
print("B和A的交集是 ", BA)

