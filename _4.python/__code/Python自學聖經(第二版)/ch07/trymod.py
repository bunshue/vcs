try:
    a=int(input("請輸入第一個整數："))
    b=int(input("請輸入第二個整數："))
    r = a % b    
except ValueError:
    print("發生輸入非數值的錯誤!")   
except Exception as e:
    print("發生",e,"的錯誤，包括分母為 0 的錯誤!")
else:
    print("r=",r)
finally:
    print("一定會執行的程式區塊")    