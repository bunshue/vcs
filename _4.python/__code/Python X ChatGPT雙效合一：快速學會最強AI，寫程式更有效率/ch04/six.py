value=int(input("請任意輸入一個整數："))
if value%2==0 or value%3==0: #判斷是否為2或3的倍數
    if value%6!=0:
         print("符合所要的條件")
    else:
         print("不符合所要的條件") #為6的倍數 
else:
    print("不符合所要的條件")
