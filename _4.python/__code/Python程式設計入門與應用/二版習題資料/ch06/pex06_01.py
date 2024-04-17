# Filename: pex06_01.py
import random as r
while True:
    inkey = input("請按任意鍵後再按Enter鍵擲骰子，若要結束請直接按Enter鍵。")
    if len(inkey)>0:
        num=r.randint(1,6)
        print("亂數產生的骰子點數："+str(num))
    else:
        print("擲骰子點數結束。")
        break