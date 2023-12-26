# ex10_4.py

A = []
for i in range(1,100,2):
    A.append(i)

num = 2
B = []
primeNum = 0
while num < 100:
    if num == 2:                                # 2是質數所以直接輸出
        B.append(num)
        primeNum += 1
    else:
        for n in range(2, num):                 # 用2 .. num-1當除數測試
            if num % n == 0:                    # 如果整除則不是質數
                break                           # 離開迴圈
        else:                                   # 否則是質數
            primeNum += 1
            B.append(num)
    num += 1

aSet = set(A)                                   # 將串列A轉成集合aSet
bSet = set(B)                                   # 將串列B轉成集合bSet

unionAB = aSet | bSet
print("聯集 : ", unionAB)
interAB = aSet & bSet
print("交集 : ", interAB)
A_B = aSet - bSet
print("A-B差集 : ", A_B)
B_A = bSet - aSet
print("B-A差集 : ", B_A)
AsdB = aSet ^ bSet
print("AB對稱差集 : ", AsdB)
