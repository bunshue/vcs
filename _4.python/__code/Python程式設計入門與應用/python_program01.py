'''

print("姓  名  提取   推論  詮釋")
print("%3s %4.2f %4.2f %4.2f"%("陳大同",89.00, 99.00, 88.00))
print("%3s %4.2f %4.2f %4.2f"%("楊小明",77.50, 89.00, 77.50))
print("%3s %4.2f %4.2f %4.2f"%("陳時雨",66.75, 99.25, 88.50))
print("%3s %4.2f %4.2f %4.2f"%("李婉玲",76.75, 84.50, 88.00))
print("%3s %4.2f %4.2f %4.2f"%("林研時",89.25, 99.50, 89.25))

print("姓  名  提取   推論  詮釋")
print("%3s %4.2f %4.2f %4.2f"%("陳大同",89.00, 99.00, 88.00))
print("%3s %4.2f %4.2f %4.2f"%("楊小明",77.50, 89.00, 77.50))
print("%3s %4.2f %4.2f %4.2f"%("陳時雨",66.75, 99.25, 88.50))
print("%3s %4.2f %4.2f %4.2f"%("李婉玲",76.75, 84.50, 88.00))
print("%3s %4.2f %4.2f %4.2f"%("林研時",89.25, 99.50, 89.25))


print("------------------------------------------------------------")  # 60個

#print
#print("當半徑為%d時，圓面積為%6.2f，圓周長為%6.2f"%(pvalue, result1, result2))
print("當半徑為%d時，圓面積為%6.2f，圓周長為%6.2f"%(pvalue, result1, result2))
print("圓柱的半徑%6.2f長度%6.2f體積為%6.2f"%(pradius,plength,pvolume))

print("------------------------------------------------------------")  # 60個
import os.path
import sys

#filename = input("請輸入檔案名稱:").strip()

if not os.path.isfile(filename):
    print("%filename檔案不存在"%(filename))
    sys.exit()

import os.path
import sys

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch02\ex02_02.py

# Filename: ex02_02.py
# coding=utf-8
chinese = float(input("請輸入國語成績:"))
math = float(input("請輸入數學成績:"))
science = float(input("請輸入自然成績:"))
print("國語成績 %6.2f 數學成績 %6.2f 自然成績 %6.2f 三科總分 %6.2f "%(chinese, math, science, chinese+math+science))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch02\ex02_04.py

# Filename: ex02_04.py
# coding=utf-8
# 邏輯運算式
pvalue = int(input("請輸入年齡:"))
print(pvalue>=30)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch02\ex02_05.py

# Filename: ex02_05.py
# coding=utf-8
# 邏輯運算式
pvalue = int(input("請輸入年齡:"))
if (pvalue>=40 and pvalue<=50):
    print("年齡%d，屬於壯年"%(pvalue))
else:
    print("年齡%d，不屬於壯年"%(pvalue))    

print("------------------------------------------------------------")  # 60個

# Filename: ex03_10.py
# while迴圈數值系統轉換十進位至二進位
pnum = int(input("請輸入需要轉換的十進位數值:"))        
# 宣告儲存資料的串列array to store 
# 二進位的數值binary number 
pbin = [0] * pnum; 
# 轉換至二進位counter for binary array 
i = 0; 
while (pnum > 0):  
    # 儲存餘數至二進位的串列
    pbin[i] = pnum % 2; 
    pnum = int(pnum / 2); 
    i += 1;
# 將串列反向印出
j=i-1    
while (j>-1):
    print(pbin[j], end = "");
    j -= 1;

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch04\ex04_04.py

# Filename: ex04_04.py
# while迴圈數值系統轉換十進位至二進位
pnum = int(input("請輸入需要轉換的十進位數字:"))        
# 宣告儲存資料的串列array to store 
# 二進位的數值binary number 
pbin = [0] * pnum
# 轉換至二進位counter for binary array 
i = 0
while (pnum > 0):  
    # 儲存餘數至二進位的串列
    pbin[i] = pnum % 2
    pnum = int(pnum / 2)
    i += 1
# 將串列反向印出
j=i-1    
while (j>-1):
    print(pbin[j], end = "")
    j -= 1

print("------------------------------------------------------------")  # 60個

list1 = [50,40,20,40,20,60,20,80,90]
print(" 原始串列:",list1)
list1.sort()
list1.reverse()
print(" 由大到小:",list1)

print("------------------------------------------------------------")  # 60個

list1 = []
for i in range(1,7):
    score=int(input("請輸入第%d位學生成績:"%i))
    list1.append(score)
list2 = sorted(list1)
list3 = sorted(list1, reverse=True)
print("原始成績:",list1)
print("由小到大:",list2)
print("由大到小:",list3)

print("------------------------------------------------------------")  # 60個

print("今天是星期二，100天後是星期幾? %d "%(200%7+2))

print("------------------------------------------------------------")  # 60個

print("%4s %4s %8s"%("x","y","x**y"))
print("%4d %4d %8d"%(1,1,1))
print("%4d %4d %8d"%(2,2,4))
print("%4d %4d %8d"%(4,3,64))
print("%4d %4d %8d"%(8,4,4096))

print("------------------------------------------------------------")  # 60個

i=1
while (i<=9):
    j=2
    while (j<=9):        
        print("%d*%d=%2d"%(j,i,i*j), end=" ")
        j=j+1
    print()
    i=i+1

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch03\pex03_03_1.py

# Filename: pex03_031.py
num = int(input("請輸入繪製層數:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print("")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch03\pex03_03_2.py

# Filename: pex03_032.py
num = int(input("請輸入繪製層數:"))   
for i in range(0,num+1,1):
    for j in range(num-i,0,-1):
        print(" ",end="")
    for k in range(0,2*i-1,1):
        print("*",end="")
    print("")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch03\pex03_03_3.py

# Filename: pex03_033.py
num = int(input("請輸入繪製層數:"))
pend = int(num/2+0.5)
for i in range(0,pend+1,1):
    for k in range(0,2*i-1,1):
        print("*",end="")
    print("")
pend = int(num/2)    
for i in range(pend, 0, -1):
    for k in range(0,2*i-1,1):
        print("*",end="")
    print("")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch03\pex03_04_1.py

# Filename: pex03_041.py
num = int(input("請輸入繪製層數:"))
pend = int(num/2+0.5)
for i in range(0,pend+1,1):
    for j in range(num-i,0,-1):
        print(" ",end="")
    for k in range(0,2*i-1,1):
        print("*",end="")
    print("")
pend = int(num/2)    
for i in range(pend, 0, -1):
    for j in range(num-i,0,-1):
        print(" ",end="")
    for k in range(0,2*i-1,1):
        print("*",end="")
    print("")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch03\pex03_04_2.py

# Filename: pex03_042.py
num = int(input("請輸入繪製層數:"))
pend = int(num/2+0.5)
for i in range(1,pend+1,1):
    for j in range(num-i,0,-1):
        print("*",end="")
    for k in range(0,2*i-1,1):
        print(" ",end="")
    for j in range(num-i,0,-1):
        print("*",end="")        
    print("")
pend = int(num/2)    
for i in range(pend, 0, -1):
    for j in range(num-i,0,-1):
        print("*",end="")
    for k in range(0,2*i-1,1):
        print(" ",end="")
    for j in range(num-i,0,-1):
        print("*",end="")
    print("")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch03\pex03_08.py

# Filename: pex03_08.py
pm = float(input("請輸入水的公升數:"))
pinitaltemp = float(input("請輸入水的起始溫度(攝氏):"))
pfinaltemp = float(input("請輸入水的最後溫度(攝氏):"))
pq = pm*(pfinaltemp-pinitaltemp)*4184
print("水的公升數%6.2f起始溫度%6.2f最後溫度%6.2f所需能量(焦耳)%6.2f"%(pm,pinitaltemp,pfinaltemp,pq))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch03\pex03_09.py

# Filename: pex03_09.py
pnum = int(input("請輸入一個整數:"))
print("整數%d"%(pnum),end="")
prev = 0
while(pnum > 0):
    prem = pnum % 10
    prev = (prev*10)+prem
    pnum = pnum //10
print("反轉順序為%d"%(prev))

# Filename: pex03_09.py
pnum = int(input("請輸入一個整數:"))
print("整數:%d"%(pnum))
print("反轉整數為:",end="")
while(pnum != 0):
    print(pnum%10,end="")
    pnum = pnum//10

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch03\pex03_10.py

# Filename: pex03_10.py
pweight = float(input("請輸入體重(英磅)："))
plength = float(input("請輸入身高(英吋)："))
pweight=pweight*0.45359237
plength=plength*0.0254
pbmi=pweight/(plength**2)
print("BMI值為%6.2f"%(pbmi))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch03\pex03_11.py

# Filename: pex03_11.py
x1, y1, x2, y2, x3, y3 = eval(input("請依序輸入三角形的三點座標值:"))
side1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
side2 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5
side3 = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5
s = (side1 + side2 + side3) / 2;
parea = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print("這三角形的面積為%6.2f"%(parea))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch04\pex04_01.py

# Filename: pex04_01.py
list1=[12,88,76,63,23,26]
#第一個元素的索引是0
#最後一個元素的索引是5
print(list1[2])
#76
print(list1[-2])
#23

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch04\pex04_02.py

# Filename: pex04_02.py
pnumbers = []
for i in range(1,4):
    pitems=int(input("請輸入第%d個整數："%i))
    pnumbers.append(pitems)
pnumbers.reverse()
print(pnumbers)    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch04\pex04_03.py

# Filename: pex04_03.py
ps1 = input("請輸入第一個字串：")
ps2 = input("請輸入第二個字串：")
list_ps1 = list(ps1)
list_ps1.sort()
list_ps2 = list(ps2)
list_ps2.sort()
if (list_ps1 == list_ps2):
    print("輸入的二個字串是anagram")
else:
    print("輸入的二個字串不是anagram")    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch04\pex04_04.py

# Filename: pex04_04.py
pscores = []
for i in range(1,6):
    pitems=int(input("請輸入5位中第%d個學生成績："%i))
    pscores.append(pitems)
pabove = 0
paverage = sum(pscores)/len(pscores)
for score in pscores:
    if score >= paverage:
        pabove += 1
print("平均數："+str(paverage))
print("大於或等於平均數的數目："+str(pabove))
print("小於平均數的數目："+str(len(pscores)-pabove))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch04\pex04_05.py

# Filename: pex04_05.py
ps=input("請輸入一個字串：")
pcounts = 0
for word in ps:
    if word == 'a':
        pcounts +=1
print ("輸入的字串中，a出現的次數："+str(pcounts))

print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch01\ex01_02.py

#Filename: ex01_02.py
print("Welcome")
a = 1
b = 2
print(a+b)


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_01.py

# Filename: ex05_01.py
def pmax(n1, n2):
    if n1>n2:
        result = n1
    else:
        result = n2
    return result

n1=int(input("請輸入第1個整數"))
n2=int(input("請輸入第2個整數"))
print("%d與%d這2個整數中，較大的是為%d"%(n1,n2,pmax(n1,n2)))    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_02.py

# Filename: ex05_02.py
def calarea(height, width=6):
    result = height*width
    return result
getarea = calarea(10)
print(getarea)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_03.py

# Filename: ex05_03.py
def calarea(height, width=6):
    result = height*width
    return result
getarea = calarea(10, 7)
print(getarea)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_04.py

# Filename: ex05_04.py
def scope():
    var1 = 1
    print(var1, var2)
var1 = 3
var2 = 4
print(var1, var2)
scope()
print(var1, var2) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_05.py

# Filename: ex05_05.py
def scope():
    global var1
    var1 = 1
    print(var1, var2)
var1 = 3
var2 = 4
print(var1, var2)
scope()
print(var1, var2)  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_06.py

# Filename: ex05_06.py
str1 = "dog"
print(str1.ljust(7))
print(str1.ljust(7,"#"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_07.py

# Filename: ex05_07.py
str1 = "dog"
print(str1.rjust(7,"#"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_08.py

# Filename: ex05_08.py
str1 = "dog"
print(str1.center(7,"#"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_09.py

# Filename: ex05_09.py
str1 = "  This is a dog.  "
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_10.py

# Filename: ex05_10.py
str1 = "I like Python."
print(str1.find("like"))
print(str1.find("Pascal"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_11.py

# Filename: ex05_11.py
str1 = "I like Python."
print(str1.replace("Python","Pascal"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch05\ex05_12.py

# Filename: ex05_12.py
str1 = "I like Python."
print(str1.replace(" ",""))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_01.py

# Filename: ex06_01.py
# 模組與套件
import calendar
print(calendar.month(2018,2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_02.py

# Filename: ex06_02.py
# 模組與套件
import calendar
print(calendar.__file__)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_03.py

# Filename: ex06_03.py
# 模組與套件
import time as t
print(t.time())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_04.py

# Filename: ex06_04.py
# 模組與套件
import time as t
print(t.localtime())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_05.py

# Filename: ex06_05.py
# 模組與套件
import time as t
ptime=t.localtime()
print("目前時間是西元%d年%d月%d日%d點%d分"%(ptime[0],ptime[1],ptime[2],ptime[3],ptime[4]))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_06.py

# Filename: ex06_06.py
# 模組與套件
import time as t
print(t.ctime())
print(t.ctime(t.time()))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_07.py

# Filename: ex06_07.py
# 模組與套件
import time as t
print("程式暫停7秒鐘")
t.sleep(7)
print("程式繼續執行")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_08.py

# Filename: ex06_08.py
# 模組與套件
import time as t
print("開始執行到目前的時間:"+str(t.clock()))
t.sleep(2)
print("程式執行時間經過:"+str(t.clock())+"秒")
t.sleep(3)
print("程式執行時間經過:"+str(t.clock())+"秒")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_09.py

# Filename: ex06_09.py
# 模組與套件
import random as r
print(r.randint(0,10))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_10.py

# Filename: ex06_10.py
# 模組與套件
import random as r
for i in range(0,5):
    print(r.randrange(0,10,2), end=" ")

print("------------------------------------------------------------")  # 60個

import random as r
print(r.random())    

print("------------------------------------------------------------")  # 60個

import random as r
for i in range(0,3):
    print(r.uniform(0,10), end=" ")

print("------------------------------------------------------------")  # 60個

import random as r
str1 = "abcde"
for i in range(0,3):
    print(r.choice(str1), end=" ")

print("------------------------------------------------------------")  # 60個

import random as r
list1 = ['a','b','c','d','e']    
for i in range(0,3):
    print(r.choice(list1), end=" ")

print("------------------------------------------------------------")  # 60個

import random as r
str1 = "abcde"
print(r.sample(str1, 3))    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch06\ex06_16.py

# Filename: ex06_16.py
# 模組與套件
import random as r
list1 = ['a','b','c','d','e']    
print(r.sample(list1, 3))  
'''
print("------------------------------------------------------------")  # 60個

content = """Welcome to Python
屏東縣好山好水好風光
Item Response Theory
"""
f=open("file.txt","w")
f.write(content)
f.close()

print("------------------------------------------------------------")  # 60個

with open("file.txt","r") as f:
    for line in f:
        print(line, end="")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_03.py

# Filename: ex08_03.py
f=open('file.txt','r',encoding='UTF-8')
for line in f:
    print(line, end="")
f.close() 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_04.py

# Filename: ex08_04.py
f=open('file.txt','r')
str1=f.read(7)
print(str1)
f.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_05.py

# Filename: ex08_05.py
f=open('file.txt','r')
str=f.readlines()
print(str)
f.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_06.py

# Filename: ex08_06.py
f=open('file_u8.txt','r',encoding='UTF-8')
str=f.readlines()
print(str)
f.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_07.py

# Filename: ex08_07.py
f=open('file_u8.txt','r',encoding='UTF-8')
str=f.readlines()
print(str)
f.close()

f=open('file_u8.txt','r',encoding='UTF-8')
str1=f.read(7)
print(str1)
f.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_08.py

# Filename: ex08_08.py
f=open('file_u8.txt','r',encoding='UTF-8-sig')
print(f.readline())
print(f.readline())
print(f.readline(5))
print(f.readline(8))
f.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_09.py

# Filename: ex08_09.py
try:
    print(varn)
except:
    print("變數不存在!") 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_10.py

# Filename: ex08_10.py
try:
    print(varn)
except NameError:
    print("變數不存在!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_11.py

# Filename: ex08_11.py
try:
    print(varn)
except Exception as error:
    print(error)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_12.py

# Filename: ex08_12.py
import logging
try:
    print(varn)
except Exception as error:
    logging.exception(error)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_13.py

# Filename: ex08_13.py
try:   
    print("welcome")
except NameError:
    print("變數不存在!")
finally:
    print("程式執行結束例外處理區塊")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch08\ex08_14.py

# Filename: ex08_14.py
while True:
    try:
        x = int(input("請輸入一個數字: "))
        break
    except ValueError:
        print("抱歉!!您所輸入並非是有效的數字，請再輸入一次...")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_01.py

# Filename: ex09_01.py
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_02.py

# Filename: ex09_02.py
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
pLabel1= tk.Label(win, text="難度計算過程", fg="black", bg="silver", font=("新細明體",12),padx=20,pady=10 )
pLabel1.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_03.py

# Filename: ex09_03.py
def cal():
    textvar.set("計算完成")    
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
textvar=tk.StringVar()
pButton1 = tk.Button(win, textvariable=textvar, command=cal, padx=20, pady=10)
textvar.set("開始計算")
pButton1.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_04.py

# Filename: ex09_04.py
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
ptext = tk.Text(win)
ptext.insert(tk.INSERT, "床前明月光\n")
ptext.insert(tk.INSERT, "疑是地上霜\n")
ptext.insert(tk.INSERT, "舉頭望明月\n")
ptext.insert(tk.INSERT, "低頭思故鄉\n")
ptext.pack()
ptext.config(state=tk.DISABLED)
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_05.py

# Filename: ex09_05.py
def checkpw():
    pmsg.set("輸入的密碼:"+ppw.get())
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
ppw = tk.StringVar()
pmsg = tk.StringVar()
pLabel = tk.Label(win, text="請輸入密碼:")
pLabel.pack()
pEntry = tk.Entry(win, textvariable=ppw)
pEntry.pack()
pButton = tk.Button(win, text="登入", command=checkpw)
pButton.pack()
pLabmsg = tk.Label(win, textvariable=pmsg)
pLabmsg.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_06.py

# Filename: ex09_06.py
def checkpw():
    pmsg.set("輸入的密碼:"+ppw.get())
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
ppw = tk.StringVar()
pmsg = tk.StringVar()
pLabel = tk.Label(win, text="請輸入密碼:")
pLabel.pack(padx=20, pady=5)
pEntry = tk.Entry(win, textvariable=ppw)
pEntry.pack(padx=20, pady=5)
pButton = tk.Button(win, text="登入", command=checkpw)
pButton.pack(padx=20, pady=5)
pLabmsg = tk.Label(win, textvariable=pmsg)
pLabmsg.pack(padx=20, pady=5)
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_07.py

# Filename: ex09_07.py
def checkpw():
    pmsg.set("輸入的密碼:"+ppw.get())
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
frame1 = tk.Frame(win)
frame1.pack(padx=20, pady=10)
ppw = tk.StringVar()
pmsg = tk.StringVar()
pLabel = tk.Label(frame1, text="請輸入密碼:")
pLabel.pack()
pEntry = tk.Entry(frame1, textvariable=ppw)
pEntry.pack()
frame2 = tk.Frame(win)
frame2.pack(padx=20, pady=10)
pButton = tk.Button(frame2, text="登入", command=checkpw)
pButton.pack()
pLabmsg = tk.Label(frame2, textvariable=pmsg)
pLabmsg.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_08.py

# Filename: ex09_08.py
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
text1 = tk.StringVar(value='GUI1')
ent1 = tk.Entry(win, textvariable=text1, width=15, justify=tk.CENTER)
ent1.grid(row=0, column=0, padx=5, pady=5)
text2 = tk.StringVar(value='GUI2')
ent2 = tk.Entry(win, textvariable=text2, width=15, justify=tk.CENTER)
ent2.grid(row=0, column=2, padx=5, pady=5, sticky=tk.N)
text3 = tk.StringVar(value='GUI3')
ent3 = tk.Entry(win, textvariable=text3, width=15, justify=tk.CENTER)
ent3.grid(row=1, column=1, padx=5, pady=5)
win.mainloop()
'''
print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_09.py

# Filename: ex09_09.py
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
text1 = tk.StringVar(value='GUI1')
ent1 = tk.Entry(win, textvariable=text1, width=15, justify=tk.CENTER)
ent1.place(relx=0.5, rely=0.5, anchor="center")
text2 = tk.StringVar(value='GUI2')
ent2 = tk.Entry(win, textvariable=text2, width=15, justify=tk.CENTER)
ent2.place(relx=0.1, rely=0.2, anchor="nw")
text3 = tk.StringVar(value='GUI3')
ent3 = tk.Entry(win, textvariable=text3, width=15, justify=tk.CENTER)
ent3.place(relx=0.1, rely=0.7, anchor="w")
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_10.py

# Filename: ex09_10.py
import tkinter as tk
import tkinter.font as tkfont
def radbut_click():
    selected_item = area.get()
    lab_result.config(text=AREA_OPTIONS[selected_item][0])
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
AREA_OPTIONS=(('屏東縣',0),('高雄市',1),('台南市',2),('台東縣',3))
area = tk.IntVar()
area.set(0)
for item, value in AREA_OPTIONS:
    radbut = tk.Radiobutton(win, text=item, variable=area, value=value, command=radbut_click, font=default_font)
    radbut.pack()
lab_result = tk.Label(win, font=default_font, fg='black')
lab_result.pack(padx=10, pady=(5,10))       
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_11.py

# Filename: ex09_11.py
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
def combox_select(event):
    selected_area = event.widget.get()
    lab_result.config(text=selected_area)
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
AREA_OPTIONS=('屏東縣','高雄市','台南市','台東縣')
area = tk.StringVar()
combox = ttk.Combobox(win, value=AREA_OPTIONS, textvariable=area, font=default_font)
combox.bind('<<ComboboxSelected>>', combox_select)
combox.current(0)
combox.pack(padx=10, pady=10)
lab_result = tk.Label(win, font=default_font, fg='black', width=18)
lab_result.pack(padx=10, pady=(5,10))       
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_12.py

# Filename: ex09_12.py
import tkinter as tk
import tkinter.font as tkfont
def spinbox_select():
    selected_month = month.get()
    lab_result.config(text=selected_month)    
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
month = tk.IntVar()
month.set(1)
spinbox = tk.Spinbox(win, from_=1, to=12, textvariable=month, command=spinbox_select, font=default_font)
spinbox.pack(padx=10, pady=10)
lab_result = tk.Label(win, font=default_font, fg='black')
lab_result.pack(padx=10, pady=(5,10))    
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_13.py

# Filename: ex09_13.py
import tkinter as tk
import tkinter.font as tkfont
def but_click():
    selected_options = ''
    if asia.get():
        selected_options += chkbut_asia.cget('text')
    if america.get():
        selected_options += chkbut_america.cget('text')
    if europe.get():
        selected_options += chkbut_europe.cget('text')
    if aferica.get():
        selected_options += chkbut_aferica.cget('text')
    lab_result.config(text=selected_options)   
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
asia = tk.IntVar()
chkbut_asia = tk.Checkbutton(win, text='亞洲',variable=asia,anchor=tk.W)
chkbut_asia.pack(padx=90, pady=5, fill=tk.X)
america = tk.IntVar()
chkbut_america = tk.Checkbutton(win, text='美洲',variable=america,anchor=tk.W)
chkbut_america.pack(padx=90, pady=5, fill=tk.X)
europe = tk.IntVar()
chkbut_europe = tk.Checkbutton(win, text='歐洲',variable=europe,anchor=tk.W)
chkbut_europe.pack(padx=90, pady=5, fill=tk.X)
aferica = tk.IntVar()
chkbut_aferica = tk.Checkbutton(win, text='非洲',variable=aferica,anchor=tk.W)
chkbut_aferica.pack(padx=90, pady=5, fill=tk.X)
but = tk.Button(win, text='確定', command=but_click, font=default_font, padx=15)
but.pack(padx=10, pady=5)
lab_result = tk.Label(win, font=default_font, fg='black', width=20)
lab_result.pack(padx=10, pady=(5,10))
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_14.py

# Filename: ex09_14.py
import tkinter as tk
import tkinter.messagebox as tkmessagebox
import tkinter.font as tkfont
def Cal():
    tkmessagebox.showinfo(title="計算", message="計算資料中的試題難度")
def View():
    tkmessagebox.showinfo(title="檢視", message="檢視計算的結果")    
def About():
    tkmessagebox.showinfo(title="關於我們", message="程式設計者:屏東大學教育學系陳新豐")
def Exit():
    win.destroy() 
def main():
    global win
    win = tk.Tk()
    win.geometry("800x600")
    win.title("試題與測驗分析程式")
    default_font = tkfont.nametofont('TkDefaultFont')
    default_font.configure(size=15)
    menubar = tk.Menu(win)
    win.config(menu=menubar)
    menu_file = tk.Menu(menubar, tearoff = 0)
    menu_cal  = tk.Menu(menubar, tearoff = 0)
    menu_help = tk.Menu(menubar, tearoff = 0)    
    menubar.add_cascade(label='檔案', menu=menu_file)
    menubar.add_cascade(label='計算', menu=menu_cal)
    menubar.add_cascade(label='Help', menu=menu_help)
    menu_file.add_command(label='結束', command=Exit)
    menu_cal.add_command(label='計算', command=Cal)
    menu_cal.add_command(label='檢視', command=View)
    menu_help.add_command(label='關於', command=About)
    win.mainloop()
main()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_15.py

# Filename: ex09_15.py
import tkinter as tk
import tkinter.font as tkfont
win = tk.Tk()
win.geometry("400x300")
win.title("圖形顯示")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
photo = tk.PhotoImage(file='python.PNG')
gs = tk.Canvas(win)
gs.create_image(60,120,image=photo)
gs.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_16.py

# Filename: ex09_16.py
import tkinter as tk
import tkinter.font as tkfont
win = tk.Tk()
win.geometry("400x300")
win.title("幾何圖形")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
photo = tk.PhotoImage(file='python.PNG')
gs = tk.Canvas(win,width=400,height=300)
gs.pack()
gs.create_rectangle(50,20,150,80)
gs.create_rectangle(80,60,200,100,fill='#FF0000')
gs.create_line(200,200,220,200)
gs.create_line(200,160,320,160,fill='#FF0000')                     
win.mainloop()

print("------------------------------------------------------------")  # 60個

from __future__ import unicode_literals
from pytube import YouTube

import tkinter as tk
import youtube_dl
import os

def Downmp4():
    yt = YouTube()
    yt.url = purl.get()
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    fvideo = yt.get("mp4", "360p")    
    fvideo.download(fpath)

def Downmp3():
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    os.chdir(fpath)    
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([purl.get()])

#main program
#製作2個視窗
win=tk.Tk()
win.geometry("600x400")
win.title("MP4與MP3下載")

frame1 = tk.Frame(win, width=600)
frame1.pack()

label1 = tk.Label(frame1, text="網址:")
label1.grid(row=0, column=0)
#label1.pack()
label2 = tk.Label(frame1, text="路徑:")
label2.grid(row=1, column=0)
#label2.pack()
#網址
purl  = tk.StringVar()
#路徑
ppath = tk.StringVar()

entry1 = tk.Entry(frame1, textvariable = purl, width=60)
entry1.grid(row=0, column=1)
#entry1.pack()
entry2 = tk.Entry(frame1, textvariable = ppath, width=60)
ppath.set("d:\music")
entry2.grid(row=1, column=1)
#entry2.pack()

btn1 = tk.Button(frame1, text="mp4", command=Downmp4)
#btn1.pack()
btn1.grid(row=2, column=1)
btn2 = tk.Button(frame1, text="mp3", command=Downmp3)
#btn2.pack()
btn2.grid(row=3, column=1)
#注意事項
label3 = tk.Label(frame1, text="本程式使用時請注意時間，保護眼睛。")
label3.grid(row=4, column=1)

win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch10\ex102\ex10_20.py

#filename:ex10_20.py
#MP3播放器
def choose():
    global playsong
    message.set("\n播放歌曲：" + choice.get())
    playsong=choice.get()
def pausemp3(): 
    mixer.music.pause() 
    message.set("\n暫停播放 {}".format(playsong))   
def increase():
    global volume
    volume +=0.1
    if volume>=1.0:
        volume=1.0
    mixer.music.set_volume(volume) 
def decrease():
    global volume
    volume -=0.1
    if volume<=0.2:
        volume=0.2
    mixer.music.set_volume(volume)  
def playmp3():
    global status,playsong,preplaysong
    if playsong==preplaysong:
        if not mixer.music.get_busy():
            mixer.music.load(playsong)
            mixer.music.play(loops=-1) 
        else:
            mixer.music.unpause() 
        message.set("\n正在播放：{}".format(playsong))
    else:
        playnewmp3()
        preplaysong=playsong 
def playnewmp3():
    global playsong
    mixer.music.stop()
    mixer.music.load(playsong)   
    mixer.music.play(loops=-1)  
    message.set("\n正在播放：{}".format(playsong))
def stopmp3():
    mixer.music.stop()
    message.set("\n停止播放") 
def loadmp3():
    global volume
    global playsong
    global preplaysong
    global choice
    global pdir
    frame1 = tk.Frame(win)
    frame1.pack()
    mp3files = []
    mp3files = glob.glob(pdir.get()+"*.mp3")
    playsong=preplaysong = ""
    index = 0
    volume= 0.8
    choice = tk.StringVar()    
    for mp3 in mp3files:  
        prbutton = tk.Radiobutton(frame1,text=mp3,variable=choice,value=mp3,command=choose)
        if(index==0):     
            prbutton.select()
            playsong=preplaysong=mp3
        prbutton.grid(row=index, column=0, sticky="w")
        index += 1      
    message.set("\n讀取檔案")
def exitmp3():
    mixer.music.stop()
    win.destroy() 
import tkinter as tk
from pygame import mixer
import glob
mixer.init()
win=tk.Tk()
win.geometry("640x380")
win.title("MP3播放程式")
labeltitle = tk.Label(win, text="\nMP3播放程式", fg="blue",font=("標楷體",12))
labeltitle.pack()
frame0 = tk.Frame(win)
frame0.pack()
pdir = tk.StringVar()
plabel1 = tk.Label(frame0, text="請輸入目錄:", width=8)
plabel1.grid(row=0, column=0, padx=5, pady=5)
pentry = tk.Entry(frame0, textvariable=pdir, width=12)
pdir.set('music/')
pentry.grid(row=0, column=1, padx=5, pady=5)   
button1 = tk.Button(frame0, text="播放", width=8,command=playmp3)
button1.grid(row=1, column=0, padx=5, pady=5)
button2 = tk.Button(frame0, text="暫停", width=8,command=pausemp3)
button2.grid(row=1, column=1, padx=5, pady=5)
button3 = tk.Button(frame0, text="調大音量", width=8,command=increase)
button3.grid(row=1, column=2, padx=5, pady=5)
button4 = tk.Button(frame0, text="調小音量", width=8,command=decrease)
button4.grid(row=1, column=3, padx=5, pady=5)
button5 = tk.Button(frame0, text="停止", width=8,command=stopmp3)
button5.grid(row=1, column=4, padx=5, pady=5)
button7 = tk.Button(frame0, text="讀取檔案", width=8,command=loadmp3)
button7.grid(row=1, column=5, padx=5, pady=5)
button6 = tk.Button(frame0, text="結束", width=8,command=exitmp3)
button6.grid(row=1, column=6, padx=5, pady=5)
win.protocol("WM_DELETE_WINDOW", exitmp3)   
message = tk.StringVar()
message.set("\n播放歌曲：")
plabel2 = tk.Label(win, textvariable=message,fg="blue",font=("標楷體",10))
plabel2.pack() 
plabel3 = tk.Label(win, text="\n")
plabel3.pack()   
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch10\ex103\ex10_30.py

# Filename: ex10_30.py
import tkinter as tk
import tkinter.messagebox as tkmessagebox
import tkinter.filedialog as tkfiledialog
import tkinter.font as tkfont
def Cal():
    options = {}
    options['filetypes'] = [("allfiles","*"),("text","*.txt")]
    options['initialdir'] = "c:\\"
    options['multiple'] = False
    options['title'] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)    
    if fs:
        f = open(fs.name,'r')
        fc = f.readlines()
        f.close()
        fo = open('output.txt','w')
        fo.write("試題分析結果\n")
        pitem = int(fc[0][0:3])
        fo.write('題數:'+str(pitem)+'\n')
        pmiss = fc[0][4:5]
        fo.write('缺失:'+pmiss+'\n')
        pomit = fc[0][6:7]
        fo.write('遺漏:'+pomit+'\n')
        pid   = int(fc[0][8:10])
        fo.write('ID長度:'+str(pid)+'\n')
        pans  = fc[1]
        fo.write('答案:'+pans)
        pnum  = len(fc)-2
        fo.write('人數:'+str(pnum)+'\n')        
        psitem = []
        for j in range(0, pitem, 1):
            psitem.append(0)
        for i in range(0,pnum, 1):            
            for j in range(0,pitem, 1):                
                if (fc[2+i][pid+j]==pans[j]):                    
                    psitem[j] = psitem[j]+1                
        for j in range(0, pitem):
            fo.write('第'+str(j+1).rjust(2,'0')+'題，難度值p='+str(round(psitem[j]/pnum,2)).ljust(4,'0')+'\n')
        fo.close()
        tkmessagebox.showinfo(title="試題分析", message="分析完成")
    else:   
	     print ("沒有選擇檔案")
def View():
    options = {}
    options['filetypes'] = [("allfiles","*")]
    options['initialdir'] = "c:\\"
    options['multiple'] = False
    options['title'] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)    
    if fs:        
        f = open(fs.name,'r')
        fc= f.readlines()
        f.close()
        ptext = tk.Text(win, width=800, height=600)        
        for i in range(0, len(fc), 1):
            ptext.insert(tk.INSERT, fc[i])        
        ptext.pack()
        ptext.config(state=tk.DISABLED)       
    else:   
	     print ("沒有選擇檔案")
def About():
    tkmessagebox.showinfo(title="關於我們", message="程式設計者:屏東大學教育學系陳新豐")
def Exit():
    win.destroy() 
def main():
    global win    
    win = tk.Tk()
    win.geometry("800x600")
    win.title("試題與測驗分析程式")
    default_font = tkfont.nametofont('TkDefaultFont')
    default_font.configure(size=15)
    menubar = tk.Menu(win)
    win.config(menu=menubar)
    menu_file = tk.Menu(menubar, tearoff = 0)
    menu_cal  = tk.Menu(menubar, tearoff = 0)
    menu_help = tk.Menu(menubar, tearoff = 0)    
    menubar.add_cascade(label='檔案', menu=menu_file)
    menubar.add_cascade(label='計算', menu=menu_cal)
    menubar.add_cascade(label='Help', menu=menu_help)
    menu_file.add_command(label='結束', command=Exit)
    menu_cal.add_command(label='計算', command=Cal)
    menu_cal.add_command(label='檢視', command=View)    
    menu_help.add_command(label='關於', command=About)
    win.mainloop()
main()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch05\ex05_06.py

# Filename: pex05_06.py
pnum = int(input("請輸入要轉換的十進位數字:"))
presult=""
while(pnum!=0):
    pdata=str(pnum%2)
    presult="".join([pdata,presult])
    pnum=pnum//2
print("轉換為二進位數字為:%s"%presult)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch05\ex05_07.py

# Filename: ex05_07.py
str1 = "dog"
print(str1.ljust(7))
print(str1.ljust(7,"#"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch05\ex05_08.py

# Filename: ex05_08.py
str1 = "dog"
print(str1.rjust(7,"#"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch05\ex05_09.py

# Filename: ex05_09.py
str1 = "dog"
print(str1.center(7,"#"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch05\ex05_10.py

# Filename: ex05_10.py
str1 = "  This is a dog.  "
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch05\ex05_11.py

# Filename: ex05_11.py
str1 = "I like Python."
print(str1.find("like"))
print(str1.find("Pascal"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch05\ex05_12.py

# Filename: ex05_12.py
str1 = "I like Python."
print(str1.replace("Python","Pascal"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch05\ex05_13.py

# Filename: ex05_13.py
str1 = "I like Python."
print(str1.replace(" ",""))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch06\ex06_082.py

# Filename: ex06_082.py
# 模組與套件 clock() python3.8後改為perf_counter()
import time as t
#print("開始執行到目前的時間:"+str(t.clock()))
print("開始執行到目前的時間:"+str(t.perf_counter()))
t.sleep(2)
print("程式執行時間經過:"+str(t.perf_counter())+"秒")
t.sleep(3)
print("程式執行時間經過:"+str(t.perf_counter())+"秒")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch07\ex07_02.py

# Filename: ex07_02.py
# 泡沫排序
def printdata():
    for item in pdata:
        print(item, end=" ")
    print()
# main program
pdata=[7,2,6,4]
print("泡沫排序前:",end=" ")
printdata()
n=len(pdata)-1

for i in range(0,n):
    for j in range(0,n-i):
        print("i=%d j=%d"%(i,j))
        if (pdata[j]>pdata[j+1]):
            print("%d, %d 互換後"%(pdata[j],pdata[j+1]), end="->")
            pdata[j],pdata[j+1]=pdata[j+1],pdata[j]
            print(pdata)
            
print("泡沫排序後:", end=" ")
printdata()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch08\ex08_07.py

# Filename: ex08_07.py
f=open('file_u8.txt','r',encoding='UTF-8-sig')
str=f.readlines()
print(str)
f.close()

f=open('file_u8.txt','r',encoding='UTF-8-sig')
str1=f.read(7)
print(str1)
f.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch08\ex08_13.py

# Filename: ex08_13.py
try:   
    print(varn)
except NameError:
    print("變數不存在!")
finally:
    print("程式執行結束例外處理區塊")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch09\ex09_91.py

import tkinter as tk
import tkinter.messagebox as tkmessagebox
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")

tkmessagebox.askokcancel(title="對話方塊", message="askokcancel")

win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch09\ex09_92.py

def checknum():
    pmsg.set("Small")
import tkinter as tk
import random as r
# create gui interface
win = tk.Tk()
win.geometry("400x300")
win.title("Guess Number")
ans=r.randint(0,100)
#print(ans)
#input guess number
pL1 = tk.Label(win, text="Please enter number:")
pL1.pack()
while (True):
    pnum = tk.StringVar()
    pE1 = tk.Entry(win, textvariable=pnum)
    pE1.pack()
    pB1 = tk.Button(win, text="OK", command=checknum)
    pB1.pack()

pmsg = tk.StringVar()
pL2 = tk.Label(win, textvariable=pmsg)
pL2.pack()

#num=121
#while (num!=ans):
#    num=int(input("please enter guess number:"))
#    if (num==ans):
#        break
#    if (num>ans):
#        print("bigger")
#    else:
#        print("smaller")   
#print("you are win")    

win.mainloop()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch10\ex101\ex10_11.py

from __future__ import unicode_literals
from pytube import YouTube

import tkinter as tk
import youtube_dl
import os

def Downmp4():
    #yt = YouTube()
    #yt.url = purl.get()
    yt = YouTube('%s'%purl.get())
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    #fvideo = yt.get("mp4", "360p")    
    fvideo = yt.streams.filter(file_extension='mp4', res='360p').first()
    fvideo.download(fpath)

def Downmp3():
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    os.chdir(fpath)    
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([purl.get()])

#main program
#製作2個視窗
win=tk.Tk()
win.geometry("600x400")
win.title("MP4與MP3下載")

frame1 = tk.Frame(win, width=600)
frame1.pack()

label1 = tk.Label(frame1, text="網址:")
label1.grid(row=0, column=0)
#label1.pack()
label2 = tk.Label(frame1, text="路徑:")
label2.grid(row=1, column=0)
#label2.pack()
#網址
purl  = tk.StringVar()
#路徑
ppath = tk.StringVar()

entry1 = tk.Entry(frame1, textvariable = purl, width=60)
entry1.grid(row=0, column=1)
#entry1.pack()
entry2 = tk.Entry(frame1, textvariable = ppath, width=60)
ppath.set("d:\music")
entry2.grid(row=1, column=1)
#entry2.pack()

btn1 = tk.Button(frame1, text="mp4", command=Downmp4)
#btn1.pack()
btn1.grid(row=2, column=1)
btn2 = tk.Button(frame1, text="mp3", command=Downmp3)
#btn2.pack()
btn2.grid(row=3, column=1)
#注意事項
label3 = tk.Label(frame1, text="本程式使用時請注意時間，保護眼睛。")
label3.grid(row=4, column=1)

win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch10\ex101\ex10_20.py

from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=BRcudpJzy1I")
stream = yt.streams.filter(file_extension='mp4', res='360p').first()
stream.download("d:\\music")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\DHT\DHT_01.py

# ex11_06.py


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\DHT\DHT_02.py

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:32:34 2018

@author: chensf
"""

from machine import pin
import dht
d = dht.DHT11(Pin(2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_01.py

import serial
ser = serial.Serial('COM7')  # open serial port
print(ser.port)
print(ser.baudrate)
print(ser.bytesize)
print(ser.parity)
print(ser.timeout)
ser.close()             # close port

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_02.py

# ex11_02.py
import pyfirmata
pin = 13
port = 'COM7'
board=pyfirmata.Arduino(port)
board.digital[pin].write(1)
board.digital[pin].write(0)
board.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_03.py

import pyfirmata

board = pyfirmata.Arduino('COM7')
it = pyfirmata.util.Iterator(board)
it.start()

sw = board.get_pin('d:12:i')
led = board.get_pin('d:10:o')
led_s = False
while True:
    value = sw.read() 
    if value == 1:
        led.write(1)
    else:
        led.write(0)
board.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_03_1.py

import pyfirmata
from time import sleep

board = pyfirmata.Arduino('COM7')
it = pyfirmata.util.Iterator(board)
it.start()

sw = board.get_pin('d:12:i')
led = board.get_pin('d:10:o')
led_s = False
while True:
    value = sw.read() 
    sleep(0.05)
    if value == 1:
        if (led_s == True):
            led.write(0)
            led_s = False            
        else:
            led.write(1)
            led_s = True
#    else:
#        led.write(0)
board.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_03_2.py

import pyfirmata

board = pyfirmata.Arduino('COM7')
it = pyfirmata.util.Iterator(board)
it.start()

sw = board.get_pin('d:12:i')
led = board.get_pin('d:10:o')
led_s = False
while True:
    value = sw.read() 
    if value == 1:
        led.write(1)
    else:
        led.write(0)
board.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_03_3.py

import pyfirmata
#from time import sleep
pin_led=10
pin_button=12
LEDState=False
port = 'COM7'
board=pyfirmata.Arduino(port)
print(board.digital[pin_button].read())
button = board.get_pin('d:12:i')
button.enable_reporting
iterator = pyfirmata.util.Iterator(board)
iterator.start()
print(button.read())

#for i in range(100):
#    print ("Button state: %s" % button.read())
#    # The return values are: True False, and None
#    if str(button.read()) == 'True':
#        print ("Button pressed")
#    elif str(button.read()) == 'False':
#        print ("Button not pressed")
#    else:
#        print ("Button was never pressed")
#    board.pass_time(0.5)
#while True:
##    if (board.digital[pin_button].read()==None):
##        sleep(0.05)
##        if (board.digital[pin_button].read()==None):
##            LEDState=not(LEDState)
##            print('改變',LEDState)
##            #board.digital[pin_led].write(LEDState)
##            sleep(0.2)
##            while (board.digital[pin_button].read()==None):
##                sleep(0.01)
##                print('等待',board.digital[pin_button].read())
#    pvalue = board.digital[pin_button].read()
#    print(pvalue)
#    while pvalue is None:
#        pass
#    if pvalue is True:
#        print("Pressed")
#    else:
#        print("no Pressed")
##        
##    if (board.digital[pin_button].read() == None):
##        print("Pressed!")
##        board.digital[pin_button].write(None)
##        print(board.digital[pin_button].read())
##    board.pass_time(1)    
board.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_04.py

import pyfirmata
from time import sleep

board = pyfirmata.Arduino('COM7')
it = pyfirmata.util.Iterator(board)
it.start()

sw = board.get_pin('d:12:i')
led = board.get_pin('d:10:o')
LEDState = False
while True:
    value = sw.read() 
    sleep(0.05)
    if value == 1:
        if (LEDState == True):
            led.write(0)
            led_s = False            
        else:
            led.write(1)
            led_s = True
board.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_05.py

# ex11_05.py 利用按鈕控制LED燈
import tkinter
import pyfirmata
from time import sleep
pin=10
port = 'COM7'
board=pyfirmata.Arduino(port)
sleep(5)
top=tkinter.Tk()
top.minsize(300,20)
def onPress():
    board.digital[pin].write(1)
def offPress():
    board.digital[pin].write(0)
onButton=tkinter.Button(top,text="打開LED燈",command=onPress)
offButton=tkinter.Button(top,text="關閉LED燈",command=offPress)
onButton.pack()
offButton.pack()
top.mainloop()
board.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_06.py

import serial
ser = serial.Serial('COM7',115200)  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port
#while True:
#    print(ser.readline())
    
    
    
import pyfirmata
from time import sleep
pin=11
port = 'COM51'
board=pyfirmata.Arduino(port)
while True:
    board.digital[pin].write(1)
    sleep(0.2)
    board.digital[pin].write(0)
    sleep(0.2)
board.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_07.py

import tkinter
import pyfirmata
from time import sleep
pin=10
port = 'COM7'
board=pyfirmata.Arduino(port)
sleep(5)
top=tkinter.Tk()
top.minsize(300,20)
def onPress():
    board.digital[pin].write(1)
def offPress():
    board.digital[pin].write(0)
onButton=tkinter.Button(top,text="on",command=onPress)
offButton=tkinter.Button(top,text="off",command=offPress)
onButton.pack()
offButton.pack()
top.mainloop()
board.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\ex11_08.py

#led燈閃爍，亮10次
import pyfirmata
from time import sleep
pin=12
port = 'COM51'
board=pyfirmata.Arduino(port)
for i in range(1,10):
    board.digital[pin].write(1)
    sleep(0.2)
    board.digital[pin].write(0)
    sleep(0.2)
board.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\sound_01.py

# sound_01.py

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch11\sound_02.py

#!/usr/bin/python

# This code is supporting material for the book
# Python Programming for Arduino
# by Pratik Desai
# published by PACKT Publishing

from pyfirmata import Arduino
from time import sleep


# This function performs buzzer patterns according to given parameters
def buzzerPattern(pin, recurrence, pattern):
    # Defining patterns by array of time delays
    pattern1 = [0.8, 0.2,0.6, 0.8,0.7,0.5,0.7]
    pattern2 = [0.2, 0.8]
    flag = True

    # Running the loop for given repetition
    for i in range(recurrence):
        if pattern == 1:
            p = pattern1
        elif pattern == 2:
            p = pattern2
        else:
            print ("Please enter valid pattern. 1 or 2.")
            exit

        # Follow pattern p to turn the buzzer on/off for time delay
        for delay in p:
            if flag is True:
                # Buzzer is on
                board.digital[pin].write(1)
                flag = False
                sleep(delay)

            else:
                # Buzzer is off
                board.digital[pin].write(0)
                flag = True
                sleep(delay)

    # Silent buzzer at the end of the pattern repetition
    board.digital[pin].write(0)
    board.exit()


# Setting up the Arduino board
port = 'COM7'
board = Arduino(port)
# Need to give some time to pyFirmata and Arduino to synchronize
sleep(5)

notes = [ 261, 294, 330, 349, 392, 440, 494, 523 ]
# Execute the 'buzzerPattern' function with custom parameters
#buzzerPattern(10, 2, 1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch12\ex12_01.py

from microbit import *
while True:
	display.show(Image('11111:22222:33333:44444:55555'))
	sleep(2000)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch12\ex12_02.py

from microbit import *
while True:
	display.show([Image.HEART, Image.HEART_SMALL])
	sleep(2000)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch12\ex12_03.py

from microbit import *
compass.calibrate()
while True:
	needle = ((15 - compass.heading()) // 30) % 12
	display.show(Image.ALL_CLOCKS[needle])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch12\ex12_04.py

from microbit import *
while True:
	display.scroll(str(temperature()))
	sleep(500)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch13\ex13_01.py

#顯示畫圖 03/16/2021
from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_01.py

# Filename: pex04_02.py
#ps = input("請輸入一串列的整數，數目之間利用空白分隔：") 
#pitems = ps.split() 
#pnumbers = [ eval(x) for x in pitems ] 
pnumbers = []
for i in range(1,4):
    pitems=int(input("請輸入第%d個整數："%i))
    pnumbers.append(pitems)
pnumbers.reverse()
print(pnumbers)    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_02.py

# Filename: pex05_02.py
ps = input("請輸入一串列的整數，數目之間利用空白分隔：") 
pitems = ps.split() 
pnumbers = [ eval(x) for x in pitems ] 
pnumbers.reverse()
print(pnumbers)    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_03.py

# Filename: pex05_03.py
ps = input("請輸入一串列的整數，數目之間利用空白分隔：") 
pitems = ps.split()
pscores = [ eval(x) for x in pitems ]
pabove = 0
paverage = sum(pscores)/len(pscores)
for score in pscores:
    if score >= paverage:
        pabove += 1
print("平均數："+str(paverage))
print("大於或等於平均數的數目："+str(pabove))
print("小於平均數的數目："+str(len(pscores)-pabove))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_04.py

# Filename: pex05_04.py
def check_anagram(s1, s2):
    list_s1 = list(s1)
    list_s1.sort()
    list_s2 = list(s2)
    list_s2.sort()
    return (list_s1 == list_s2)

ps1 = input("請輸入第一個字串：")
ps2 = input("請輸入第二個字串：")
if (check_anagram(ps1,ps2)):
    print("輸入的二個字串是anagram")
else:
    print("輸入的二個字不是anagram")    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_05.py

# Filename: pex05_05.py
def fgcd(numbers):
    g = numbers[0]
    for i in range(1, len(numbers)):
        g = fgcd2(g, numbers[i])
    return g
def fgcd2(n1, n2):
    g = 1 
    k = 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            g = k 
        k += 1
    return g

ps = input("請輸入一串列的整數，數值之間以空白間隔即可：") 
pitems = ps.split()
pnumbers = [ eval(x) for x in pitems ]    
print("串列整數", pnumbers,"的GCD為",fgcd(pnumbers))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_06.py

# Filename: pex05_06.py
def sumdigits(n):
    ptemp = abs(n)
    psum = 0
    while ptemp != 0:
        pre = ptemp % 10
        psum = psum+pre
        ptemp = ptemp // 10
    return psum

pnum = int(input("請輸入一個整數："))
print("整數%d，其中每一位數值的和為%d"%(pnum, sumdigits(pnum)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_07.py

# Filename: pex05_07.py
def freverse(n):
    while n != 0:
        pre = n % 10
        print(pre, end = "")
        n = n // 10

pnum = int(input("請輸入一個整數："))
freverse(pnum)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_08.py

# Filename: pex05_08.py
def ctof(pc):
    presult = pc*9/5+32
    return presult

ptemp = float(input("請輸入攝氏溫度:"))
print("攝氏溫度%6.2f轉換為華氏溫度為%6.2f"%(ptemp,ctof(ptemp)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_09.py

# Filename: pex05_09.py
def pdistance(px1,py1,px2,py2):
    presult=(px1-px2)**2+(py1-py2)**2
    presult=presult**0.5    
    return presult

x1 = float(input("請輸入x1的座標值:"))
y1 = float(input("請輸入y1的座標值:"))
x2 = float(input("請輸入x2的座標值:"))
y2 = float(input("請輸入y2的座標值:"))
print("第一點(%6.2f,%6.2f)與第二點(%6.2f,%6.2f)之間的距離是%6.2f"%(x1,y1,x2,y2,pdistance(x1,y1,x2,y2)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_10.py

# Filename: pex05_10.py
def isprime(n):
    for pd in range(2, n // 2 + 1):
        if n % pd == 0:
            return False
    return True

pnumber = int(input("請輸入一個整數："))
if (isprime(pnumber)):   
    print("輸入整數%d是質數"%pnumber)
else:    
    print("輸入整數%d不是質數"%pnumber)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_11.py

# Filename: pex05_11.py
def isprime(n):
    for pd in range(2, n // 2 + 1):
        if n % pd == 0:
            return False
    return True

for i in range(2, 100):
    if (isprime(i)):
        print("%3d"%i)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_12.py

# Filename: pex05_12.py
def phi(n):
    presult = 0
    ptemp = 1
    for i in range(1, n + 1, 1):
        presult = presult+ptemp/(2 * i - 1) 
        ptemp = -1*ptemp
    presult = 4*presult
    return presult

print(phi(900))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch05\pex05_13.py

# Filename: pex05_13.py
def DtoS(num,ctype):
    presult=""
    while(num!=0):
        pdata=str(num%ctype)
        presult="".join([pdata,presult])
        num=num//ctype
    return(presult)

pnum = int(input("請輸入要轉換的十進位數字:"))
ptype = int(input("請輸入要轉換的進位系統(2,8):")) 
strl=DtoS(pnum,ptype)
print(strl)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch06\pex06_01.py

# Filename: pex06_01.py
import random as r
while True:
    inkey = input("請按任意鍵後再按Enter鍵擲骰子，若要結束請直接按Enter鍵。")
    if len(inkey)>0:
        num=r.randint(1,6)
        print("亂數產生的骰子點數："+str(num))
    else:
        print("擲骰子點數結束。")
        break

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch06\pex06_02.py

# Filename: pex06_02.py
import random as r
list1 = r.sample(range(1,50),7)
print(list1)
special = list1.pop()
print(special)
list1.sort()
print("本期大樂透中獎號碼為:", end="")
for i in range(0,6):
    if (i==5):
        print(str(list1[i]))
    else:
        print(str(list1[i]), end=",")
print("本期大樂透特別號為:"+str(special))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch06\pex06_03.py

# Filename: pex06_03.py
import time as t
week = ["一","二","三","四","五","六","日"]
dst = ["無日光節約時間","有日光節約時間"]
time1 = t.localtime()
show = "現在時刻:"+"\n"
show += "中華民國"+str(int(time1.tm_year)-1911)+"年"
show += str(time1.tm_mon)+"月"+str(time1.tm_mday)+"日"
show += str(time1.tm_hour)+"時"+str(time1.tm_min)+"分"
show += str(time1.tm_sec)+"秒 星期"+week[time1.tm_wday]+"\n"
show += "今天是今年的第"+str(time1.tm_yday)+"天，此地"+dst[time1.tm_isdst]
print(show)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch06\pex06_04.py

# Filename: pex06_04.py
import time as t
timestart = t.clock()
for i in range(0,5000):
    for j in range(0,1000):
        n=i*j
timeend = t.clock()
print("執行五百萬次整數運算的時間:"+str(timeend-timestart)+"秒")        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch06\pex06_05.py

# Filename: pex06_05.py
import random as r
for i in range(0,7):
    print(r.choice("ABCDEFGHIJKLMN"), end=",")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch06\pex06_06.py

# Filename: pex06_06.py
import random as r
pnumber = r.randint(0, 100)
print("請猜測電腦隨機產生的亂數為何？")
pok = -1
while pok != pnumber:
    pok = int(input("請輸入你所猜測的整數："))
    if pok == pnumber:
        print("Yes, 你猜對了",pnumber)
    elif pok > pnumber:
        print("No, 你猜的數字太大了")
    else:
        print("No, 你猜的數字太小了")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch07\pex07_01.py

# Filename: pex07_01.py
pnum = ["055","816","292","891","491","437"]
pno = input("請輸入中獎者的號碼：")
pisfound=False
for i in range(len(pnum)):
    if (pnum[i]==pno):
        pisfound=True
        break
if (pisfound==True):
    print("中獎者的號碼為：",pnum[i])
else:
    print("抱歉，無此中獎號碼!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch07\pex07_02.py

# Filename: pex07_02.py
# 泡沫排序
def printdata():
    for item in pdata:
        print(item, end=" ")
    print()
# main program
# input data
pdata = []
while True:
    pinkey = input("請輸入數字[ENTER]結束：")
    if len(pinkey)>0:
        pdata.append(int(pinkey))
    else:
        break
print("泡沫排序前:",end=" ")
printdata()
n=len(pdata)-1
for i in range(0,n):
    for j in range(0,n-i):
        if (pdata[j]<pdata[j+1]):
            pdata[j],pdata[j+1]=pdata[j+1],pdata[j]
print("泡沫排序後:", end=" ")
printdata()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch07\pex07_03.py

# Filename: pex07_03.py
def printdata(pdata):
    for item in pdata:
        print(item, end=" ")
    print()
def insert_search(pdata):
    for i in range(1, len(pdata)): #第一個元素固定，從第二個開始
        tmp = int(pdata[i])
        j = i - 1 #固定元素的前一個數字
        while j >= 0 and tmp < int(pdata[j]):
            pdata[j + 1] = pdata[j] #值向右
            j = j - 1
        pdata[ j + 1 ] = str(tmp)
    return pdata      
# main program
pdata = ["055","816","292","891","491","437"]
print("原始資料:",end=" ")
printdata(pdata)
pdata = insert_search(pdata)
print("排序資料:", end=" ")
printdata(pdata)
# 開始搜尋
n=len(pdata)-1
isfound=False
min=0
max=n
c=0
no = input("請輸入中獎者的號碼：")
while (min<=max):
    mid=int((min+max)/2)
    c += 1
    if (int(pdata[mid])==int(no)):
        isfound=True
        break
    if (int(pdata[mid])>int(no)):
        max=mid-1
    else:
        min=mid+1
if (isfound==True):
    print("第%d個號碼，號碼為%s:"%(c,pdata[mid]))
else:
    print("無此中獎號碼！")
print("共比對%d次"%(c))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch07\pex07_04.py

# Filename: pex07_04.py
def movedisk(n, dfrom , dto, daux):
    if n==1:
        print("移動",n,"從",dfrom,"到",dto)
    else:
        movedisk(n-1,dfrom, daux, dto)
        print("移動",n,"從",dfrom,"到",dto)
        movedisk(n-1, daux, dto, dfrom)        
#main program
pnum = int(input("請輸入需要移動幾個圓盤："))
print("移動圓盤的過程如下所示：")
movedisk(pnum,'A','B','C')            

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch07\pex07_05.py

# Filename: pex07_05.py
def freverse(n):
    if n != 0:
       print(n % 10, end = "")
       n = n // 10
       freverse(n)
#main program       
pnum = int(input("請輸入一個整數："))
freverse(pnum)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch08\pex08_01.py

# Filename: pex08_01.py
pfile = input("請輸入讀取檔案名稱：").strip()
pinfile = open(pfile, "r")
ps = pinfile.read()  
print(str(len(ps)) + " 字元數") 
print(str(len(ps.split())) + " 單字數") 
print(str(len(ps.split('\n'))) + " 行數") 
pinfile.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch08\pex08_02.py

# Filename: pex08_02.py
from random import randint
import os.path

pfile = input("請輸入檔名：").strip()
if os.path.isfile(pfile):
    print("此檔案已經存在，程式終止")
else:
    poutfile = open(pfile, "w")
        
    for i in range(100):
        print(randint(0, 999), file = poutfile, end = " ")
       
    poutfile.close()
        
    pinfile = open(pfile, "r")
    ps = pinfile.read()
    
    pnumber = [eval(items) for items in ps.split()]
    pnumber.sort()
        
    for i in range(len(pnumber)):
        print(pnumber[i], end = " ")
            
    pinfile.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch08\pex08_03.py

# Filename: pex08_03.py
try:
    pnumber = int(input("請輸入一個整數："))
    print("所輸入的整數%d"%pnumber)
except Exception as ex:
    print("異常例外：", ex) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch09\pex09_01.py

# Filename: pex09_01.py
def checkp():
    p3.set(p2.get()/(p1.get()*p1.get()/10000))
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("計算BMI程式")
frame1 = tk.Frame(win)
frame1.pack(padx=20, pady=10)
p1 = tk.IntVar()
p2 = tk.IntVar()
p3 = tk.DoubleVar()
pLabel = tk.Label(frame1, text="請輸入身高(公分)")
pLabel.pack()
pEn1 = tk.Entry(frame1, textvariable=p1)
pEn1.pack()
pLabe2 = tk.Label(frame1, text="請輸入體重(公斤)")
pLabe2.pack()
pEn2 = tk.Entry(frame1, textvariable=p2)
pEn2.pack()
pButton = tk.Button(frame1, text="計算BMI", command=checkp)
pButton.pack()
pLmsg = tk.Label(frame1, textvariable=p3)
pLmsg.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\習題\ch10\pex10_01.py

# Filename:pex10_01.py
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def openFile(): 
    filenameforReading = askopenfilename()
    infile = open(filenameforReading, "r")
    text.insert("end", infile.read()) # Read all from the file
    infile.close()  # Close the input file
    
def saveFile():
    filenameforWriting = asksaveasfilename()
    outfile = open(filenameforWriting, "w")
    # Write to the file
    outfile.write(text.get(1.0, "end")) 
    outfile.close() # Close the output file
    
window = tk.Tk()
window.title("簡易文字編輯器")
        
# Create a menu bar
menubar = tk.Menu(window)
window.config(menu = menubar) # Display the menu bar
        
# create a pulldown menu, and add it to the menu bar
operationMenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = operationMenu)
operationMenu.add_command(label = "Open", command = openFile)
operationMenu.add_command(label = "Save", command = saveFile)
        
# Add a tool bar frame 
frame0 = tk.Frame(window) # Create and add a frame to window
frame0.grid(row = 1, column = 1, sticky = "W")
        
# Create images
opneImage = tk.PhotoImage(file = "open.gif")
saveImage = tk.PhotoImage(file = "save.gif")
        
tk.Button(frame0, image = opneImage, command = openFile).grid(
                row = 1, column = 1, sticky = "W")
tk.Button(frame0, image = saveImage, command = saveFile).grid(
                row = 1, column = 2)
        
frame1 = tk.Frame(window) # Hold editor pane
frame1.grid(row = 2, column = 1)
        
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = "right", fill = "y")
text = tk.Text(frame1, width = 40, height = 20, wrap = "word",
               yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)
        
window.mainloop() # Create an event loop

print("------------------------------------------------------------")  # 60個

'''
