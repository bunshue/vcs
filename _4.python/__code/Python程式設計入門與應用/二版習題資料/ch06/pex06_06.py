# Filename: pex06_06.py
import random as r
pnumber = r.randint(0, 100)
print("請猜測電腦隨機產生的亂數為何？")
pok = -1
while pok != pnumber:
    pok = int(input("請輸入你所猜測的整數："))
    if pok == pnumber:
        print("Yes, 你猜對了",pnumber)
    elif pok > pnumber:
        print("No, 你猜的數字太大了")
    else:
        print("No, 你猜的數字太小了")