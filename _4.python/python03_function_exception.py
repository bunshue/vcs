"""
python 之 預設函數

eval()
divmod()
zip()


python 之 Exception
try-except-else-finally


"""


"""
# python 預設函數

range()
dir()
help()


"""

"""
type()
int()
float()
"""

print("python之基本函數")
print("int(8.4)=", int(8.4))
print("bin(14)=", bin(14))
# print('hex(84)=',hex(84))
print("oct(124)=", oct(124))
print("float(6)=", float(6))
print("abs(-6.4)=", abs(-6.4))
print("divmod(58,5)=", divmod(58, 5))
print("pow(3,4)=", pow(3, 4))
print("round(3.5)=", round(3.5))
print("chr(68)=", chr(68))
print("ord('%s')=%d" % ("A", ord("A")))
# print('str(1234)=',str(1234))
print("sorted([5,7,1,8,9])=", sorted([5, 7, 1, 8, 9]))
print("max(4,6,7,12,3)=", max(4, 6, 7, 12, 3))
print("min(4,6,7,12,3)=", min(4, 6, 7, 12, 3))
print("len([5,7,1,8,9])=", len([5, 7, 1, 8, 9]))

print("------------------------------------------------------------")  # 60個

print("int(8.4)=", int(8.4))
print("bin(14)=", bin(14))
# print("hex(84)=", hex(84))
print("oct(124)=", oct(124))
print("float(6)=", float(6))
print("abs(-6.4)=", abs(-6.4))
print("divmod(58,5)=", divmod(58, 5))
print("pow(3,4)=", pow(3, 4))
print("round(3.5)=", round(3.5))
print("chr(68)=", chr(68))
print("ord('%s')=%d" % ("A", ord("A")))
# print("str(1234)=", str(1234))
print("sorted([5,7,1,8,9])=", sorted([5, 7, 1, 8, 9]))
print("max(4,6,7,12,3)=", max(4, 6, 7, 12, 3))
print("min(4,6,7,12,3)=", min(4, 6, 7, 12, 3))
print("len([5,7,1,8,9])=", len([5, 7, 1, 8, 9]))

print("------------------------------------------------------------")  # 60個

x = -10
print("以下輸出abs( )函數的應用")
print(x)  # 輸出x變數
print(abs(x))  # 輸出abs(x)
x = 5
y = 3
print("以下輸出pow( )函數的應用")
print(pow(x, y))  # 輸出pow(x,y)
x = 47.5
print("以下輸出round(x)函數的應用")
print(x)  # 輸出x變數
print(round(x))  # 輸出round(x)
x = 48.5
print(x)  # 輸出x變數
print(round(x))  # 輸出round(x)
x = 49.5
print(x)  # 輸出x變數
print(round(x))  # 輸出round(x)
print("以下輸出round(x,n)函數的應用")
x = 2.15
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)
x = 2.25
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)
x = 2.151
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)
x = 2.251
print(x)  # 輸出x變數
print(round(x, 1))  # 輸出round(x,1)

print("------------------------------------------------------------")  # 60個

r = abs(-10)
print("abs(-10) = ", r)
r = abs(5)
print("abs(5) = ", r)
r = pow(8, 2)
print("pow(8, 2) = ", r)
r = pow(2, 3)
print("pow(2, 3) = ", r)
r = max(9, 3, 12, 32, 81, 92)
print("max(9, 3, 12, 32, 81, 92) = ", r)
r = min(9, 3, 12, 32, 81, 92)
print("min(9, 3, 12, 32, 81, 92) = ", r)
r = round(5.32)
print("round(5.32) = ", r)
r = round(5.52)
print("round(5.52) = ", r)
r = round(3.14568757, 3)
print("round(3.14568757, 3) = ", r)
r = round(3.14568757, 1)
print("round(3.14568757, 1) = ", r)

number = 3.14159
print("四捨五入到小數點後兩位：", round(number, 4))


print('eval() ST------------------------------------------------------------')	#60個


zzz = "123"
n = eval(zzz)

print(type(n))
print('取得數字 :', n)


print("------------------------------------------------------------")  # 60個

print("請輸入數值公式 : ")

numberStr = "3*5"
number = eval(numberStr)
print(f"計算結果 : {number:5.2f}")


print("------------------------------------------------------------")  # 60個



"""
n1, n2, n3 = eval(input("請輸入3個數字："))
average = (n1 + n2 + n3) / 3
print(f"3個數字平均是 {average:6.2f}")
"""

string = "1,2,3"
#請輸入三個數值，以逗點隔開
num1, num2, num3 = eval(string)
total = num1 + num2 + num3
print('數值合計：', total)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("測試 eval()")

numberStr = "12.34*56.78"
print("數值公式 :", numberStr)
number = eval(numberStr)
print("計算結果 : %5.2f" % number)

numberStr = "1234*5678"
print("數值公式 :", numberStr)
number = eval(numberStr)
print("計算結果 : %5.2f" % number)


x = eval("123456789")

print("------------------------------------------------------------")  # 60個




print('eval() SP------------------------------------------------------------')	#60個

print('divmod() ST------------------------------------------------------------')	#60個

quotient, remainder = divmod(1234, 100)   # 商和餘數
print("商")
print(quotient)
print("餘數")
print(remainder)

print('------------------------------------------------------------')	#60個

print("divmod的寫法")

dist = 384400  # 地球到月亮距離
speed = 1225  # 馬赫速度每小時1225公里
total_hours = dist // speed  # 計算小時數
days, hours = divmod(total_hours, 24)  # 商和餘數
print("總供需要天數")
print(days)
print("小時數")
print(hours)

#same
data = divmod(total_hours, 24)  # 商和餘數
#print("divmod傳回的資料型態是 : ", type(data))
print(f"總共需要 {data[0]} 天")
print(f"{data[1]} 小時")

print("------------------------------------------------------------")  # 60個

money=1234
num=7
ans=divmod(money,num)
print('每一位同學的平均退費為',ans[0],'元')
print('剩餘可以存入班費共同基金為 ',ans[1],'元')

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('divmod() SP------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('try-except-else-finally ST------------------------------------------------------------')	#60個

input_string = "5, 13"
try:
    #n1, n2 = eval(input("輸入2個整數n1,n2: "))
    n1, n2 = eval(input_string)
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





print('------------------------------------------------------------')	#60個




print('try-except-else-finally SP------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30", "Chicago"]
zipData = zip(fields, info)  # 執行zip
# print(type(zipData))                # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30"]
zipData = zip(fields, info)  # 執行zip
# print(type(zipData))                # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30", "Chicago"]
zipData = zip(fields, info)  # 執行zip
# print(type(zipData))                # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

f, i = zip(*player)  # 執行unzip
print("fields = ", f)
print("info   = ", i)

print("------------------------------------------------------------")  # 60個

fields = ["台北", "台中", "高雄"]
info = [80000, 50000, 60000]
zipData = zip(fields, info)  # 執行zip
sold_info = tuple(zipData)  # 將zip資料轉成元組
for city, sales in sold_info:
    print(f"{city} 銷售金額是 {sales}")

print("------------------------------------------------------------")  # 60個


def find_common_prefix(strs):
    prefix = []
    for c in zip(*strs):
        if len(set(c)) == 1:
            prefix.append(c[0])
        else:
            break
    return "".join(prefix)


print(find_common_prefix(["expensive", "export", "experience"]))

print("------------------------------------------------------------")  # 60個

X = [1, 2, 3, 4, 5]
Y = [1, 4, 9, 16, 25]
Z = list(zip(X, Y))  # zip : 兩串或更多串資料，同編號放一起的動作
print(Z)


X, Y = zip(*Z)  # Z裡面的點一個一個拿出來
print(X)
print(Y)

print("------------------------------------------------------------")  # 60個

a = [1, 2, 3]
b = ["a", "b", "c"]
c = zip(a, b)
print(list(c))  # 输出 [(1, 'a'), (2, 'b'), (3, 'c')]


loc = ([1, 2, 3, 4], [11, 12, 13, 14])
for i in zip(*loc):
    print(i)


x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
t = (x, y, z)
print(t)
for i in zip(*t):
    print(i)


# 4-3-3 在 list 生成式用 zip() 同時走訪多個容器

a = [1, -2, 3, -4, 5]
b = [9, 8, -7, -6, -5]

print([[x, y] for x, y in zip(a, b)])
print([x + y for x, y in zip(a, b)])

print("------------------------------------------------------------")  # 60個

a = [1, -2, 3, -4, 5]

b = [9, 8, -7, -6, -5]

print([x + y for x, y in zip(a, b) if x + y >= 0])


# 4-3-4 以巢狀 list 生成式產生複合 list

a = [1, 2, 3]

b = ["A", "B"]

print([[x, y] for x in a for y in b])


print("------------------------------------------------------------")  # 60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30", "Chicago"]
zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30"]
zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30", "Chicago"]
zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

f, i = zip(*player)  # 執行unzip
print("fields = ", f)
print("info   = ", i)



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


