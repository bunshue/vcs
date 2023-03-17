# 各種python專用的語法

print('try-except-finally 的用法')

try:
    print(n)
    print('變數 n 存在!, 此行不會被執行到')
except:
    print('變數 n 不存在!')
finally:
    print('一定會執行的程式區塊')

n=2
try:
    n+=1
except:
    print("變數 n 不存在!")
else:
    print("n=",n) # n=3


try:
    print(n)
except Exception as e:
    print(e)

try:
    a=int(input("請輸入第一個整數："))
    b=int(input("請輸入第二個整數："))
    r = a + b
    print("r=",r)
except:
    print("發生輸入非數值的錯誤!")
    
    
print('try-except 的用法')

while True:
    try:
        age = int(input("What is your age?"))
        break
    except:
        print("Please enter a number")

if age < 15:
    print("You are too young")

print('try-except 的用法')
import os, sys
try:
    os.remove('hello.txt')
except Exception as e:
    print(e)
    e_type, e_value, e_tb = sys.exc_info()
    print("種類：{}\n訊息：{}\n資訊：{}".format(e_type, e_value, e_tb))

def div(a,b):
    return a/b

print(div(6,2))  # 3.0
try:
    print(div(3,0)) #中止程式
except Exception as e:
    print(e)
    e_type, e_value, e_tb = sys.exc_info()
    print("種類：{}\n訊息：{}\n資訊：{}".format(e_type, e_value, e_tb))


print('冪次方的寫法')
z=10
print(z)
z = z**0.5    #冪次方的寫法
print(z)


