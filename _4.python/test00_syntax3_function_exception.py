"""
python 之 預設函數

python 之 Exception


"""

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

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

import sys

print('------------------------------------------------------------')	#60個

def division(x, y):
    try:                        # try - except指令
        ans =  x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")
    else:
        return ans              # 傳回正確的執行結果

print('除法結果 :', division(10, 2))          # 列出10/2
print('除法結果 :', division(5, 0))           # 列出5/0
print('除法結果 :', division(6, 3))           # 列出6/3

print('------------------------------------------------------------')	#60個
def division(x, y):
    try:                        # try - except指令
        return x / y
    except Exception:           # 通用錯誤使用
        print("通用錯誤發生")

print('除法結果 :', division(10, 2))          # 列出10/2
print('除法結果 :', division(5, 0))           # 列出5/0
print('除法結果 :', division('a', 'b'))       # 列出'a' / 'b'
print('除法結果 :', division(6, 3))           # 列出6/3

print('------------------------------------------------------------')	#60個

def division(x, y):
    try:                             # try - except指令
        return x / y
    except:                          # 捕捉所有異常
        print("異常發生")
    finally:                         # 離開函數前先執行此程式碼
        print("階段任務完成")

print('除法結果 :', division(10, 2),"\n")          # 列出10/2
print('除法結果 :', division(5, 0),"\n")           # 列出5/0
print('除法結果 :', division('a', 'b'),"\n")       # 列出'a' / 'b'
print('除法結果 :', division(6, 3),"\n")           # 列出6/3

print('------------------------------------------------------------')	#60個


filename = 'file_not_found.txt'             # 設定欲開啟的檔案
try:
    with open(filename) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print("找不到 %s 檔案" % filename)
else:
    print(data)                 # 輸出變數data相當於輸出檔案

print('------------------------------------------------------------')	#60個

print('try-except-finally 的用法')

try:
    print(n)
    print('變數 n 存在!, 此行不會被執行到')
except:
    print('變數 n 不存在!')
finally:
    print('一定會執行的程式區塊')

print('------------------------------------------------------------')	#60個

number1 = 3
number2 = 5

try:
    result = number1 / number2
    print('Result is ' + str(result))
except ZeroDivisionError:
    print('Division by zero!')
except SyntaxError:
    print('A comma may be missing in the input')
except:
    print('Something wrong in the input')
else:
    print('No exceptions')
finally:
    print('The finally clause is executed')

print('------------------------------------------------------------')	#60個

n = 2
try:
    n += 1
except:
    print('變數 n 不存在!')
else:
    print('n =', n) # n = 3

try:
    print(n)
except Exception as e:
    print(e)

try:
    #a = int(input('請輸入第一個整數：'))
    #b = int(input('請輸入第二個整數：'))
    a = 3
    b = 5
    r = a + b
    print('r =', r)
except:
    print('發生輸入非數值的錯誤!')

print('------------------------------------------------------------')	#60個

print('try-except 的用法')

while True:
    try:
        #age = int(input('What is your age?'))
        age = 20
        break
    except:
        print('Please enter a number')

if age < 15:
    print('You are too young')

print('try-except 的用法')
import os, sys
try:
    os.remove('hello.txt')
except Exception as e:
    print(e)
    e_type, e_value, e_tb = sys.exc_info()
    print('種類：{}\n訊息：{}\n資訊：{}'.format(e_type, e_value, e_tb))

def div(a,b):
    return a / b

print(div(6,2))  # 3.0
try:
    print(div(3,0)) #中止程式
except Exception as e:
    print(e)
    e_type, e_value, e_tb = sys.exc_info()
    print('種類：{}\n訊息：{}\n資訊：{}'.format(e_type, e_value, e_tb))

print('------------------------------------------------------------')	#60個

try:
    "1" + 2
except SyntaxError:
    print("SyntaxError - 語法錯誤")
except TypeError:
    print("TypeError - 型態錯誤")
except NameError:
    print("NameError - 該變數未宣告")
except IndexError:
    print("IndexError - 指定索引位置錯誤")
else:
    print("無發生任何異常")
finally:
    print("finally - 不管有沒發生異常都會執行")

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

