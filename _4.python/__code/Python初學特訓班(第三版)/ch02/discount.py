money = int(input("請輸入購物金額："))
if(money >= 10000):
    if(money >= 100000):
        print(str(money * 0.8), end=" 元\n")  #八折
    elif(money >= 50000):
        print(str(money * 0.85), end=" 元\n")  #八五折
    elif(money >= 30000):
        print(str(money * 0.9), end=" 元\n")  #九折
    else:
        print(str(money * 0.95), end=" 元\n")  #九五折
else:
    print(str(money), end=" 元\n")  #未打折