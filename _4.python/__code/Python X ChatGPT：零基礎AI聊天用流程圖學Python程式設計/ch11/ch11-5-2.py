try:
    n1, n2 = eval(input("輸入2個整數n1,n2: "))
    r = n1 / n2
    print("r=", r)
except ZeroDivisionError:
    print("錯誤! 除以0")
except SyntaxError:
    print("錯誤! 數字需逗號分隔")
except:
    print("錯誤! 輸入錯誤!")
