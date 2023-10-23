import random as r #為random模組取別名
for j in range(6): #以迴圈執行6次
    print(r.randint(1,42), end=' ')#產生1-42的整數亂數
print() #換行1
for j in range(3): #以迴圈執行3次
    print(r.uniform(1,10), end=' ')#產生1-10間的亂數
