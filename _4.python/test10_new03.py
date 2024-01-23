import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


names = ["A太","B介","C子","D郎"]
for i, name in enumerate(names):
    if name == "C子":
        print(i, "號的", name, "找到了。")

print("------------------------------------------------------------")  # 60個

def search(findname):
    names = ["A太","B介","C子","D郎"]
    for i, name in enumerate(names):
        if name == findname:
            return i, name
    return -1, "找不到該名稱。"

n, name = search("C子")
print(name, n, "號")
n, name = search("A子")
print(name, n, "號")


print("------------------------------------------------------------")  # 60個

print("divmod的寫法")

dist = 384400  # 地球到月亮距離
speed = 1225  # 馬赫速度每小時1225公里
total_hours = dist // speed  # 計算小時數
days, hours = divmod(total_hours, 24)  # 商和餘數
print("總供需要天數")
print(days)
print("小時數")
print(hours)

print("------------------------------------------------------------")  # 60個

money=1234
num=7
ans=divmod(money,num)
print('每一位同學的平均退費為',ans[0],'元')
print('剩餘可以存入班費共同基金為 ',ans[1],'元')




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


