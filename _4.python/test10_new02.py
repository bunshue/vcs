import os
import sys
import time
import random
import numpy as np

print("------------------------------------------------------------")  # 60個

file = open("temp.txt", "w+")

file.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

file.flush()

print("寫入之後的游標位置：", file.tell())

print('往後跳16拜')
file.seek(16, 0)

print('擷取至位置26')
file.truncate(26)

print('讀出來')
print(file.read())

file1=open("temp.txt","r")
text=file1.read(1) #以read()方法讀取檔案
print(text)
text=file1.read(3) #以read()方法讀取檔案
print(text)
text=file1.read(2) #以read()方法讀取檔案
print(text)
text=file1.read(2) #以read()方法讀取檔案
print(text)
file1.close()


print("------------------------------------------------------------")  # 60個

for _ in range(10):
    aa = random.randint(1,10)
    print(aa)

print('顯示模組的所有名稱dir()')
print(dir(random))
print("------------------------------------------------------------")  # 60個

print("ccccc")

s1 = "lion"
s2 = "mouse"

print(id(s1))
print(id(s2))

s2 = "lions"

print(id(s1))
print(id(s2))

print("------------------------------------------------------------")  # 60個

str = "{1} * {0} = {2}"
a = 3
b = "5"
print(str.format(a, b, a * int(b)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch02\date.py

year=2023
month=12
day=27
print("日期：%s-%s-%s" %(year, month, day))

print("------------------------------------------------------------")  # 60個

Val=170
print("Val的八進位數=%o" %Val)#以%o格式化字元輸出
print("Val的十六進位數=%x" %Val)#以%x格式化字元輸出 

print("------------------------------------------------------------")  # 60個

weight=123
print("您在月球上體重為：%.5f 公斤" %(weight * 0.17))

print("------------------------------------------------------------")  # 60個

company="藍海科技股份有限公司"
year=27
print("{}已成立公司 {} 年" .format (company, year))

print("------------------------------------------------------------")  # 60個

print("{0:10}收入：{1:_^12}".format("Axel", 52000))
print("{0:10}收入：{1:>12}".format("Michael", 87000))
print("{0:10}收入：{1:*<12}".format("May", 36000))

print("------------------------------------------------------------")  # 60個

num = 168
print ("數字 %s 的浮點數：%5.1f" % (num,num))
print ("數字 %s 的八進位：%o" % (num,num))
print ("數字 %s 的十六進位：%x" % (num,num))
print ("數字 %s 的二進位：%s" % (num,bin(num)))

print("------------------------------------------------------------")  # 60個

print("編號 姓名    底薪  業務獎金 加給補貼")
print("%3d %3s %6d %6d %6d" %(801,"朱正富",32000,10000,5000))
print("%3d %3s %6d %6d %6d" %(805,"曾自強",35000,8000,7000))
print("%3d %3s %6d %6d %6d" %(811,"陳威動",43000,15000,6000))

print("------------------------------------------------------------")  # 60個

print(type(23))  #輸出結果 <class 'int'>
print(type(3.14)) #輸出結果 <class 'float'>
print(type("happy birthday")) #輸出結果 <class 'str'>
print(type(True)) #輸出結果 <class 'bool'>

print("------------------------------------------------------------")  # 60個

num1=30
print(num1)
num1="happy"
print(num1)
a=b=12
print(a,b)
name,salary,weight="陳大富",60000,85.7
print(name,salary,weight)

print("------------------------------------------------------------")  # 60個

x = 15; y = 10
print(x & y)  
print(x ^ y)   
print(x | y)  
print(~x)

print("------------------------------------------------------------")  # 60個


x=1234
print("共需花費: %d 元" % x)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

phrase = ["三陽開泰", "事事如意", "五福臨門"]
for index, x in enumerate(phrase):
    print ("{0}--{1}".format(index, x))

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

total=0
for count in range(1, 100, 2): 
    total += count #將數值累加
print("數值1~100之間的奇數累計=",total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch05\prime.py

n=int(input("請輸入n的值,n表示2~n之間的所有質數:"))
i=2;
while i<=n:
    no_prime=0
    for j in range(2,i,1):
        if i%j==0:
            no_prime=1
            break  #跳出迴圈
    if no_prime==0:
        print("%d " %i); #輸出質數
    i+=1

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch05\rev.py

n=int(input("請輸入任一整數:"))
print("反向輸出的結果:",end="")
while n!=0:
    print("%d" %(n%10),end="") #求出餘數值
    n//=10
print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch05\sigma.py

k=int(input("請輸入k值："))
sigma=0
for n in range(int(k)+1):
    if(n % 2!=0): #如果n是奇數
        sigma += float(-1/(2*n+1))
    else:  #如果n是偶數
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch05\sum.py

total=0
for count in range(1, 101): #數值1~100
    total += count #將數值累加
print("數字1累加到100的總和=",total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch05\table.py

for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch05\while.py

x, y = 1, 10
while x < y:
    print(x, end = ' ')
    x += 1


print("------------------------------------------------------------")  # 60個



X = [1, 2,3, 4,5]
Y = [1, 4,9,16,25]
Z = list(zip(X, Y))   #zip : 兩串或更多串資料，同編號放一起的動作
print(Z)


X, Y = zip(*Z)  #Z裡面的點一個一個拿出來
print(X)
print(Y)


print("------------------------------------------------------------")  # 60個



a = [1, 2, 3]
b = ['a', 'b', 'c']
c = zip(a, b)
print(list(c)) # 输出 [(1, 'a'), (2, 'b'), (3, 'c')]


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





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


