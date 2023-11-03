# ch10_17.py
A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
# 將symmetric_difference( )應用在A集合
A_sydi_B = A.symmetric_difference(B)    # A和B的對稱差集
print("A和B的對稱差集是 ", A_sydi_B)    
# 將symmetric_difference( )應用在B集合
B_sydi_A = B.symmetric_difference(A)    # B和A的對稱差集
print("B和A的對稱差集是 ", B_sydi_A)

