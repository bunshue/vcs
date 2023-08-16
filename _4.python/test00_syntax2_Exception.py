# 各種python專用的語法 Exception

try:
    n1, n2 = eval(input("輸入2個整數n1,n2: "))
    r = n1 / n2
    print("r=", r)
except ZeroDivisionError:
    print("錯誤! 除以0")
except SyntaxError:
    print("錯誤! 數字需逗號分隔")
except:
    print("錯誤: 輸入或運算錯誤!")
else:
    print("Else: 資料輸入正確!")
finally:
    print("Finally: 有輸入資料!")


print('------------------------------------------------------------')	#60個




try:
    fp = open("myfile.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("錯誤! myfile.txt檔案不存在!")



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

