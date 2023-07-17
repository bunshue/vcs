try:
    a=int(input("請輸入第一個整數："))
    b=int(input("請輸入第二個整數："))
    r = a % b    
except(ValueError,ZeroDivisionError) as e:
    print("發生{} 0 的錯誤!" .format(e))   
else:
    print("r=",r)