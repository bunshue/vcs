try:
    n1, n2 = eval(input("輸入2個整數n1,n2: "))
    r = n1 / n2
    print("r=", r)
except:
    print("錯誤: 輸入或運算錯誤!")
else:
    print("Else: 資料輸入正確!")
finally:
    print("Finally: 有輸入資料!")
