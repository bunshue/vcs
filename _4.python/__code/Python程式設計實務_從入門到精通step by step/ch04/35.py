value=int(input("請任意輸入一個整數："))
if value%5==0 or value%7==0: #判斷是否為5或7的倍數
    if value%35 !=0:
         print("符合所要的條件")
    else:
         print("不符合所要的條件") 
else:
    print("不符合所要的條件")
