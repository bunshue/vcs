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

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

num1 = [1, 3, 5]
num2 = [2, 4, 6]
num3 = num1 + num2           # 字串為主的串列相加
print(num3)

print("------------------------------------------------------------")  # 60個

cars = ['toyota', 'nissan', 'honda']
nums = [1, 3, 5]
carslist = cars * 3           # 串列乘以數字
print(carslist)
numslist = nums * 5           # 串列乘以數字
print(numslist)   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_13.py

# ch6_13.py
James = ['Lebron James',23, 19, 22, 31, 18] # 定義James串列
Love = ['Kevin Love',20, 18, 30, 22, 15]    # 定義Love串列
game3 = James[4] + Love[4]
LKgame = James[0] + ' 和 ' +  Love[0] + '第四場總得分 = ' 
print(LKgame, game3)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_14.py

# ch6_14.py
warriors = ['Curry', 'Durant', 'Iquodala', 'Bell', 'Thompson']
print("2018年初NBA勇士隊主將陣容", warriors)
del warriors[3]                 # 不明原因離隊
print("2018年末NBA勇士隊主將陣容", warriors)
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_15.py

# ch6_15.py
nums1 = [1, 3, 5]
print("刪除nums1串列索引1元素前   = ",nums1)
del nums1[1]
print("刪除nums1串列索引1元素後   = ",nums1)
nums2 = [1, 2, 3, 4, 5, 6]
print("刪除nums2串列索引[0:2]前   = ",nums2)
del nums2[0:2]
print("刪除nums2串列索引[0:2]後   = ",nums2)
nums3 = [1, 2, 3, 4, 5, 6]
print("刪除nums3串列索引[0:6:2]前 = ",nums3)
del nums3[0:6:2]
print("刪除nums3串列索引[0:6:2]後 = ",nums3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_16.py

# ch6_16.py
cars = ['Toyota', 'Nissan', 'Honda']
print("cars串列長度是 = %d" %  len(cars))
if len(cars) != 0:
    del cars[0]
    print("刪除cars串列元素成功")
    print("cars串列長度是 = %d" % len(cars))
else:
    print("cars串列內沒有元素資料")
nums = []
print("nums串列長度是 = %d" % len(nums))
if len(nums) != 0:
    del nums[0]
    print("刪除nums串列元素成功")
else:
    print("nums串列內沒有元素資料")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_17.py

# ch6_17.py
strN = "DeepStone"
strU = strN.upper( )           # 改成大寫
strL = strN.lower( )           # 改成小寫
strT = strN.title( )           # 改成第一個字母大寫其他小寫
print("大寫輸出:",strU,"\n小寫輸出:",strL,"\n第一字母大寫:",strT)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_18.py

# ch6_18.py
strN = " DeepStone "
strL = strN.lstrip( )       # 刪除字串左邊多餘空白
strR = strN.rstrip( )       # 刪除字串右邊多餘空白
strB = strN.lstrip( )       # 先刪除字串左邊多餘空白
strB = strB.rstrip( )       # 再刪除字串右邊多餘空白
strO = strN.strip( )        # 一次刪除頭尾端多餘空白
print("/%s/" % strN)
print("/%s/" % strL)
print("/%s/" % strR)
print("/%s/" % strB)
print("/%s/" % strO)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_19.py

# ch6_19.py
cars = ['bmw', 'benz', 'audi']     
carF = "我開的第一部車是 " + cars[1].title( )
carN = "我現在開的車子是 " + cars[0].upper( )
print(carF)
print(carN)

print("------------------------------------------------------------")  # 60個

cars = ['Honda','Toyota','Ford']     
print("目前串列內容 = ",cars)
print("在索引1位置插入Nissan")
cars.insert(1,'Nissan')
print("新的串列內容 = ",cars)
print("在索引0位置插入BMW")
cars.insert(0,'BMW')
print("最新串列內容 = ",cars)

print("------------------------------------------------------------")  # 60個

cars = ['Honda','Toyota','Ford','BMW']     
print("目前串列內容 = ",cars)
print("使用pop( )刪除串列元素")
popped_car = cars.pop( )          # 刪除串列末端值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ",cars)
print("使用pop(1)刪除串列元素")
popped_car = cars.pop(1)          # 刪除串列索引為1的值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ",cars)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_23.py

# ch6_23.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print("目前串列內容 = ",cars)
print("使用remove( )刪除串列元素")
expensive = 'bmw'
cars.remove(expensive)            # 刪除第一次出現的元素bmw
print("所刪除的內容是: " + expensive.upper( ) + " 因為太貴了" )
print("新的串列內容",cars)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_24.py

# ch6_24.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print("目前串列內容 = ",cars)
# 直接列印cars[::-1]顛倒排序,不更改串列內容
print("列印使用[::-1]顛倒排序\n", cars[::-1])
# 更改串列內容
print("使用reverse( )顛倒排序串列元素")
cars.reverse( )            # 顛倒排序串列
print("新的串列內容 = ",cars)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_25.py

# ch6_25.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列內容 = ",cars)
print("使用sort( )由小排到大")
cars.sort( )            
print("排序串列結果 = ",cars)
nums = [5, 3, 9, 2]
print("目前串列內容 = ",nums)
print("使用sort( )由小排到大")
nums.sort( )            
print("排序串列結果 = ",nums)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_26.py

# ch6_26.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列內容 = ",cars)
print("使用sort( )由大排到小")
cars.sort(reverse=True)            
print("排序串列結果 = ",cars)
nums = [5, 3, 9, 2]
print("目前串列內容 = ",nums)
print("使用sort( )由大排到小")
nums.sort(reverse=True)            
print("排序串列結果 = ",nums)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_27.py

# ch6_27.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列car內容 = ",cars)
print("使用sorted( )由小排到大")
cars_sorted = sorted(cars)            
print("排序串列結果 = ",cars_sorted)
print("原先串列car內容 = ",cars)
nums = [5, 3, 9, 2]     
print("目前串列num內容 = ",nums)
print("使用sorted( )由小排到大")
nums_sorted = sorted(nums)            
print("排序串列結果 = ",nums_sorted)
print("原先串列num內容 = ",nums)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_28.py

# ch6_28.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列car內容 = ",cars)
print("使用sorted( )由大排到小")
cars_sorted = sorted(cars,reverse=True)            
print("排序串列結果    = ",cars_sorted)
print("原先串列car內容 = ",cars)
nums = [5, 3, 9, 2]     
print("目前串列num內容 = ",nums)
print("使用sorted( )由大排到小")
nums_sorted = sorted(nums,reverse=True)            
print("排序串列結果    = ",nums_sorted)
print("原先串列num內容 = ",nums)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_29.py

# ch6_29.py
cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
i = cars.index(search_str)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_str, i))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
j = nums.index(search_val)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_val, j))


print("------------------------------------------------------------")  # 60個

James = ['Lebron James',23, 19, 22, 31, 18] # 定義James串列
games = len(James)                          # 求元素數量
score_Max = max(James[1:games])             # 最高得分
i = James.index(score_Max)                  # 場次
print(James[0], "在第 %d 場得最高分 %d" % (i, score_Max))

print("------------------------------------------------------------")  # 60個

cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
num1 = cars.count(search_str)
print("所搜尋元素 %s 出現 %d 次" % (search_str, num1))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
num2 = nums.count(search_val)
print("所搜尋元素 %s 出現 %d 次" % (search_val, num2))


print("------------------------------------------------------------")  # 60個

char = '-'
lst = ['Silicon', 'Stone', 'Education']
print(char.join(lst))
char ='***'
lst = ['Silicon', 'Stone', 'Education']
print(char.join(lst))
char = '\n'             # 換行字元
lst = ['Silicon', 'Stone', 'Education']
print(char.join(lst))

print("------------------------------------------------------------")  # 60個

James = [['Lebron James','SF','12/30/84'],23,19,22,31,18] # 定義James串列
games = len(James)                                        # 求元素數量
score_Max = max(James[1:games])                           # 最高得分
i = James.index(score_Max)                                # 場次
name = James[0][0]
position = James[0][1]
born = James[0][2]
print("姓名     : ", name)
print("位置     : ", position)
print("出生日期 : ", born)
print("在第 %d 場得最高分 %d" % (i, score_Max))

print("------------------------------------------------------------")  # 60個

cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['ford', 'audi']
print("原先cars1串列內容 = ", cars1)
print("原先cars2串列內容 = ", cars2)
cars1.append(cars2)
print("執行append( )後串列cars1內容 = ", cars1)
print("執行append( )後串列cars2內容 = ", cars2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_34.py

# ch6_34.py
cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['ford', 'audi']
print("原先cars1串列內容 = ", cars1)
print("原先cars2串列內容 = ", cars2)
cars1.extend(cars2)
print("執行extend( )後串列cars1內容 = ", cars1)
print("執行extend( )後串列cars2內容 = ", cars2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_35.py

# ch6_35.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_36.py

# ch6_36.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)
                   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_37.py

# ch6_37.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print(" -- 新增運動項目後 -- ")
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)

print("------------------------------------------------------------")  # 60個

mysports = ['basketball', 'baseball']
friendsports = mysports[:]
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print(" -- 新增運動項目後 -- ")
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)

print("------------------------------------------------------------")  # 60個

string = "Python"
# 正值索引
print(" string[0] = ", string[0],
      "\n string[1] = ", string[1],
      "\n string[2] = ", string[2],
      "\n string[3] = ", string[3],
      "\n string[4] = ", string[4],
      "\n string[5] = ", string[5])
# 負值索引
print(" string[-1] = ", string[-1],
      "\n string[-2] = ", string[-2],
      "\n string[-3] = ", string[-3],
      "\n string[-4] = ", string[-4],
      "\n string[-5] = ", string[-5],
      "\n string[-6] = ", string[-6])
# 多重指定觀念
s1, s2, s3, s4, s5, s6 = string
print("多重指定觀念的輸出測試 = ",s1,s2,s3,s4,s5,s6)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_40.py

# ch6_40.py
string = "Deep Learning"                # 定義字串
print("列印string第1-3元素     = ", string[0:3])
print("列印string第2-4元素     = ", string[1:4])
print("列印string第2,4,6元素   = ", string[1:6:2])
print("列印string第1到最後元素 = ", string[1:])
print("列印string前3元素       = ", string[0:3])
print("列印string後3元素       = ", string[-3:])

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_41.py

# ch6_41.py
string = "Deep Learning"                # 定義字串
strlen = len(string)
print("字串長度", strlen)
maxstr = max(string)
print("字串最大的unicode碼值和字元", ord(maxstr), maxstr)
minstr = min(string)
print("字串最小的unicode碼值和字元", ord(minstr), minstr)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_41_1.py

# ch6_41_1.py
str1 = "Silicon Stone Education"
str2 = "DeepStone"
str3 = "深石數位"

sList1 = str1.split()                       # 字串轉成串列
sList2 = str2.split()                       # 字串轉成串列
sList3 = str3.split()                       # 字串轉成串列
print(str1, " 串列內容是 ", sList1)         # 列印串列
print(str1, " 串列字數是 ", len(sList1))    # 列印字數
print(str2, " 串列內容是 ", sList2)         # 列印串列
print(str2, " 串列字數是 ", len(sList2))    # 列印字數
print(str3, " 串列內容是 ", sList3)         # 列印串列
print(str3, " 串列字數是 ", len(sList3))    # 列印字數



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_41_2.py

# ch6_41_2.py
msg = '''CIA Mark told CIA Linda that the secret USB
had given to CIA Peter'''
print("字串開頭是CIA: ", msg.startswith("CIA"))
print("字串結尾是CIA: ", msg.endswith("CIA"))
print("CIA出現的次數: ",msg.count("CIA"))

print("------------------------------------------------------------")  # 60個

x = 10
y = 10
z = 15
r = 20
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print("x位址 = %d, y位址 = %d, z位址 = %d, r位址 = %d"
      % (id(x), id(y), id(z), id(r)))
r = x                               # r的值將變為10
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print("x位址 = %d, y位址 = %d, z位址 = %d, r位址 = %d"
      % (id(x), id(y), id(z), id(r)))

print("------------------------------------------------------------")  # 60個

x = 10
y = 10
z = 15
r = z - 5
boolean_value = x is y
print("x位址 = %d, y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d, " % (x, y), boolean_value)

boolean_value = x is z
print("x位址 = %d, z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d, " % (x, z), boolean_value)

boolean_value = x is r
print("x位址 = %d, r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d, " % (x, r), boolean_value)

boolean_value = x is not y
print("x位址 = %d, y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d, " % (x, y), boolean_value)

boolean_value = x is not z
print("x位址 = %d, z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d, " % (x, z), boolean_value)

boolean_value = x is not r
print("x位址 = %d, r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d, " % (x, r), boolean_value)

print("------------------------------------------------------------")  # 60個

mysports = ['basketball', 'baseball']
sports1 = mysports          # 拷貝位址
sports2 = mysports[:]       # 拷貝新串列
print("我喜歡的運動 = ", mysports, "位址是 = ", id(mysports))
print("運動 1       = ", sports1,  "位址是 = ", id(sports1))
print("運動 2       = ", sports2,  "位址是 = ", id(sports2))
boolean_value = mysports is sports1
print("我喜歡的運動 is 運動 1     = ", boolean_value)

boolean_value = mysports is sports2
print("我喜歡的運動 is 運動 2     = ", boolean_value)

boolean_value = mysports is not sports1
print("我喜歡的運動 is not 運動 1 = ", boolean_value)

boolean_value = mysports is not sports2
print("我喜歡的運動 is not 運動 2 = ", boolean_value)

print("------------------------------------------------------------")  # 60個

drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)        # 數值初始是0
print(enumerate_drinks)                     # 傳回enumerate物件所在記憶體
print("下列是輸出enumerate物件類型")
print(type(enumerate_drinks))               # 列出物件類型

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_48.py

# ch6_48.py
drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)                # 數值初始是0
print("轉成串列輸出, 初始值是 0 = ", list(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start = 10)    # 數值初始是10
print("轉成串列輸出, 初始值是10 = ", list(enumerate_drinks))










          



print("------------------------------------------------------------")  # 60個


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:
    print(player)
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_4.py

# ch7_4.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:print(player)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_5.py

# ch7_5.py
players = ['curry', 'jordan', 'james', 'durant', 'obama']
for player in players:
    print(player.title( ) + ", it was a great game.")
    print("I can not wait to see your next game, " + player.title( ))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_6.py

# ch7_6.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
print("列印前3位球員")
for player in players[:3]:
    print(player)
print("列印後3位球員")
for player in players[-3:]:
    print(player)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_7.py

# ch7_7.py
n = 5
number1 = list(range(n))
print("當n值是%d時的range( )串列 = " % n, number1)
n = 8
number2 = list(range(n))
print("當n值是%d時的range( )串列 = " % n, number2)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_8.py

# ch7_8.py
n = 5
print("當n值是%d時的range( )串列元素:" % n)
for number in range(n):
    print(number)
n = 8
print("當n值是%d時的range( )串列元素:" % n)
for number in range(n):
    print(number)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_9.py

# ch7_9.py
start = 2
end = 6
number1 = list(range(start, end))
print("當start值是%2d, end值是%2d時的range( )串列 = " % (start, end), number1)
start = -2
end = 3
number2 = list(range(start, end))
print("當start值是%2d, end值是%2d時的range( )串列 = " % (start, end), number2)
start = -5
end = -1
number3 = list(range(start, end))
print("當start值是%2d, end值是%2d時的range( )串列 = " % (start, end), number3)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_10.py

# ch7_10.py
start = 2
end = 6
print("當start值是%d, end值是%d時的range( )串列元素:" % (start, end))
for number in range(start,end):
    print(number)
start = -2
end = 3
print("當start值是%d, end值是%d時的range( )串列元素:" % (start, end))
for number in range(start,end):
    print(number)
start = -5
end = -1
print("當start值是%d, end值是%d時的range( )串列元素:" % (start, end))
for number in range(start,end):
    print(number)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_11.py

# ch7_11.py
start = 2
end = 9
step = 2
number1 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列 = " % (start, end, step), number1)
start = -2
end = 9
step = 3
number2 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列 = " % (start, end, step), number2)
start = 5
end = -5
step = -3
number3 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列 = " % (start, end, step), number3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_12.py

# ch7_12.py
start = 2
end = 9
step = 2
number1 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)
start = -2
end = 9
step = 3
number2 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)
start = 5
end = -5
step = -3
number3 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)

print("------------------------------------------------------------")  # 60個

n = 100
number = list(range(n + 1))
total = sum(number)
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

n = 100
number = list(range(n + 1))
total = sum(number)
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

n = 100
number = list(range(n + 1))       # 建立串列
total = 0                         # 總計
for i in number:
    total += i
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

n = 100
total = 0                         # 總計
for i in range(1, n+1):
    total += i
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

squares = []                     # 建立空串列
n = 100
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    value = num * num            # 元素平方
    squares.append(value)        # 加入串列
print(squares)

print("------------------------------------------------------------")  # 60個

squares = []                     # 建立空串列
n = 100
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    squares.append(num ** 2)     # 加入串列
print(squares)

print("------------------------------------------------------------")  # 60個

n = 100
if n > 10 : n = 10               # 最大值是10
squares = [num ** 2 for num in range(1, n+1)]
print(squares)

print("------------------------------------------------------------")  # 60個

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
    print()         # 換行輸出
    

print("------------------------------------------------------------")  # 60個

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("aa", end="")
    print()                # 換行輸出
    

print("------------------------------------------------------------")  # 60個

print("測試1")
for digit in range(1, 11):
    if digit == 5:
        break
    print(digit, end=', ')
print( )
print("測試2")
for digit in range(0, 11, 2):
    if digit == 5:
        break
    print(digit, end=', ')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_22.py

# ch7_22.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama', 'Kevin', 'Lin']
n = 10
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引
for player in players:
    if index == n:
        break
    print(player, end=" ")
    index += 1                          # 索引加1

print("------------------------------------------------------------")  # 60個

players = [['James', 202],
           ['Curry', 193],
           ['Durant', 205],
           ['Jordan', 199],
           ['David', 211]]
for player in players:
    if player[1] < 200:
        continue
    print(player)

print("------------------------------------------------------------")  # 60個

print("請輸入大於1的整數做質數測試 = 119")

num = 119

if num == 2:                                # 2是質數所以直接輸出
    print("%d是質數" % num)
else:
    for n in range(2, num):                 # 用2 .. num-1當除數測試
        if num % n == 0:                    # 如果整除則不是質數
            print("%d不是質數" % num)
            break                           # 離開迴圈
    else:                                   # 否則是質數
        print("%d是質數" % num)

print("------------------------------------------------------------")  # 60個

i = 1                   # 設定i初始值
while i <= 9:           # 當i大於9跳出外層迴圈
    j = 1               # 設定j初始值
    while j <= 9:       # 當j大於9跳出內層迴圈
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
        j += 1          # 內層迴圈加1
    print()             # 換行輸出
    i += 1              # 外層迴圈加1

print("------------------------------------------------------------")  # 60個

players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama', 'Kevin', 'Lin']
n = 5
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引index
while index < len(players):             # 是否index在串列長度範圍
    if index == n:                      # 是否達到想列出的人數
        break
    print(players[index], end=" ")
    index += 1                          # 索引index加1

print("------------------------------------------------------------")  # 60個

index = 0
while index <= 10:
    index += 1
    if ( index % 2 != 0 ):  # 測試是否奇數
        continue            # 不往下執行
    print(index)            # 輸出偶數
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_35.py

# ch7_35.py
fruits = ['apple', 'orange', 'apple', 'banana', 'apple']
fruit = 'apple'
print("刪除前的fruits", fruits)
while fruit in fruits:      # 只要串列內有apple迴圈就繼續
    fruits.remove(fruit)
print("刪除後的fruits", fruits)

print("------------------------------------------------------------")  # 60個

buyers = [['James', 1030],              # 建立買家購買紀錄
           ['Curry', 893],
           ['Durant', 2050],
           ['Jordan', 990],
           ['David', 2110]]
goldbuyers = []                         # Gold買家串列
vipbuyers =[]                           # VIP買家串列
while buyers:                           # 執行買家分類迴圈分類完成迴圈才會結束
    index_buyer = buyers.pop()
    if index_buyer[1] >= 1000:          # 用1000圓執行買家分類條件
        vipbuyers.append(index_buyer)   # 加入VIP買家串列
    else:
        goldbuyers.append(index_buyer)  # 加入Gold買家串列
print("VIP 買家資料", vipbuyers)
print("Gold買家資料", goldbuyers)

print("------------------------------------------------------------")  # 60個

drinks = ["coffee", "tea", "wine"]

# 解析enumerate物件
for drink in enumerate(drinks):             # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)

print("****************")   

# 解析enumerate物件
for drink in enumerate(drinks, 10):         # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)

print("------------------------------------------------------------")  # 60個

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

numbers1 = (1, 2, 3, 4, 5)      # 定義元組元素是整數
fruits = ('apple', 'orange')    # 定義元組元素是字串
mixed = ('James', 50)           # 定義元組元素是不同型態資料
val_tuple = (10,)               # 只有一個元素的元祖
print(numbers1)
print(fruits)
print(mixed)
print(val_tuple)
# 列出元組資料型態
print("元組mixed資料型態是: ",type(mixed))

print("------------------------------------------------------------")  # 60個

numbers1 = (1, 2, 3, 4, 5)      # 定義元組元素是整數
fruits = ('apple', 'orange')    # 定義元組元素是字串
val_tuple = (10,)               # 只有一個元素的元祖
print(numbers1[0])              # 以中括號索引值讀取元素內容
print(numbers1[4])
print(fruits[0],fruits[1])
print(val_tuple[0])
x, y = ('apple', 'orange')      # 有趣的應用也可以用x,y=fruits
print(x,y)

print("------------------------------------------------------------")  # 60個

keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
for key in keys:
    print(key)

print("------------------------------------------------------------")  # 60個

fruits = ('apple', 'orange')        # 定義元組元素是水果
print("原始fruits元組元素")
for fruit in fruits:
    print(fruit)

fruits = ('watermelon', 'grape')    # 定義新的元組元素
print("\n新的fruits元組元素")
for fruit in fruits:
    print(fruit)

print("------------------------------------------------------------")  # 60個

fruits = ('apple', 'orange', 'banana', 'watermelon', 'grape')
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])
print(fruits[-2:])
print(fruits[0:5:2])

print("------------------------------------------------------------")  # 60個

keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
print("keys元組長度是 %d " % len(keys))

print("------------------------------------------------------------")  # 60個

keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
list_keys = list(keys)              # 將元組改為串列
list_keys.append('secret')          # 增加元素
print("列印元組", keys)
print("列印串列", list_keys)

print("------------------------------------------------------------")  # 60個

keys = ['magic', 'xaab', 9099]      # 定義串列元素是字串與數字
tuple_keys = tuple(keys)            # 將串列改為元組
print("列印串列", keys)
print("列印元組", tuple_keys)

print("------------------------------------------------------------")  # 60個

tup = (1, 3, 5, 7, 9)
print("tup最大值是", max(tup))
print("tup最小值是", min(tup))

print("------------------------------------------------------------")  # 60個

drinks = ("coffee", "tea", "wine")
enumerate_drinks = enumerate(drinks)                # 數值初始是0
print("轉成元組輸出, 初始值是 0 = ", tuple(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start = 10)    # 數值初始是10
print("轉成元組輸出, 初始值是10 = ", tuple(enumerate_drinks))

print("------------------------------------------------------------")  # 60個

drinks = ("coffee", "tea", "wine")
# 解析enumerate物件
for drink in enumerate(drinks):             # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("****************")   
# 解析enumerate物件
for drink in enumerate(drinks, 10):         # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)

print("------------------------------------------------------------")  # 60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)         # 執行zip
print(type(zipData))                # 列印zip資料類型
player = list(zipData)              # 將zip資料轉成串列
print(player)                       # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30']
zipData = zip(fields, info)         # 執行zip
print(type(zipData))                # 列印zip資料類型
player = list(zipData)              # 將zip資料轉成串列
print(player)                       # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)         # 執行zip
print(type(zipData))                # 列印zip資料類型
player = list(zipData)              # 將zip資料轉成串列
print(player)                       # 列印串列

f, i = zip(*player)                 # 執行unzip
print("fields = ", f)
print("info   = ", i)

print("------------------------------------------------------------")  # 60個

import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個

fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
del fruits['西瓜']
print("新fruits字典內容:", fruits)
   

print("------------------------------------------------------------")  # 60個

fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
fruits.clear( )
print("新fruits字典內容:", fruits)
 

print("------------------------------------------------------------")  # 60個

soldier0 = {}           # 建立空字典
print("空小兵字典", soldier0)
soldier0['tag'] = 'red'
soldier0['score'] = 3
print("新小兵字典", soldier0)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_13.py

# ch9_13.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
cfruits = fruits.copy( )
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_14.py

# ch9_14.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
empty_dict = {}
print("fruits字典元素數量     = ", len(fruits))
print("noodles字典元素數量    = ", len(noodles))
print("empty_dict字典元素數量 = ", len(empty_dict))

print("------------------------------------------------------------")  # 60個

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
print("Stephen Curry是 %s 的球員" % players['Stephen Curry'])
print("Kevin Durant是 %s 的球員" % players['Kevin Durant'])
print("Paul Gasol是 %s 的球員" % players['Paul Gasol']) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_17.py

# ch9_17.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name, team in players.items( ):
    print("\n姓名: ", name)
    print("隊名: ", team)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_18.py

# ch9_18.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name in players.keys( ):
    print("姓名: ", name)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_19.py

# ch9_19.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name in players:
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_20.py

# ch9_20.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name in sorted(players.keys( )):
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_21.py

# ch9_21.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for team in players.values( ):
    print(team)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_21_1.py

# ch9_21_1.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for team in set(players.values( )):
    print(team)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_22.py

# ch9_22.py
soldier0 = {'tag':'red', 'score':3, 'speed':'slow'}         # 建立小兵
soldier1 = {'tag':'blue', 'score':5, 'speed':'medium'}
soldier2 = {'tag':'green', 'score':10, 'speed':'fast'}
armys = [soldier0, soldier1, soldier2]                      # 小兵組成串列
for army in armys:                                          # 列印小兵
    print(army)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_23.py

# ch9_23.py
armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
for soldier in armys[:3]:
    print(soldier)
# 列印小兵數量
print("小兵數量 = ", len(armys))

print("------------------------------------------------------------")  # 60個

armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
print("前3名小兵資料")
for soldier in armys[:3]:
    print(soldier)
# 更改編號36到38的小兵
for soldier in armys[35:38]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'blue'
        soldier['score'] = 5
        soldier['speed'] = 'medium'
# 列印編號35到40的小兵
print("列印編號35到40小兵資料")
for soldier in armys[34:40]:
    print(soldier)

print("------------------------------------------------------------")  # 60個

# 建立內含字串的字典
sports = {'Curry':['籃球', '美式足球'],
          'Durant':['棒球'],
          'James':['美式足球', '棒球', '籃球']}
# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items( ):
          print("%s 喜歡的運動是: " % name)
# 列印value,這是串列
          for sport in favorite_sport:
              print("   ", sport)

print("------------------------------------------------------------")  # 60個

# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}}
# 列印內含字典的字典
for account, account_info in wechat_account.items( ):
    print("使用者帳號 = ", account)                   # 列印鍵(key)
    name = account_info['last_name'] + " " + account_info['first_name']
    print("姓名       = ", name)                      # 列印值(value)
    print("城市       = ", account_info['city'])      # 列印值(value)


print("------------------------------------------------------------")  # 60個

# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}}
# 列印字典元素個數
print("wechat_account字典元素個數       ", len(wechat_account))
print("wechat_account['cshung']元素個數 ", len(wechat_account['cshung']))
print("wechat_account['kevin']元素個數  ", len(wechat_account['kevin']))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_29.py

# ch9_29.py
# 將串列轉成字典
seq1 = ['name', 'city']         # 定義串列
list_dict1 = dict.fromkeys(seq1)
print("字典1 ", list_dict1)
list_dict2 = dict.fromkeys(seq1, 'Chicago')
print("字典2 ", list_dict2)
# 將元組轉成字典
seq2 = ['name', 'city']         # 定義元組
tup_dict1 = dict.fromkeys(seq2)
print("字典3 ", tup_dict1)
tup_dict2 = dict.fromkeys(seq2, 'New York')
print("字典4 ", tup_dict2)

print("------------------------------------------------------------")  # 60個

fruits = {'Apple':20, 'Orange':25}
ret_value1 = fruits.get('Orange')
print("Value = ", ret_value1)
ret_value2 = fruits.get('Grape')
print("Value = ", ret_value2)
ret_value3 = fruits.get('Grape', 10)
print("Value = ", ret_value3)

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

langs = {'Python', 'C', 'Java', 'Python', 'C'}
print(type(langs))
print(langs)

print("------------------------------------------------------------")  # 60個

# 集合由整數所組成
integer_set = {1, 2, 3, 4, 5}
print(integer_set)
# 集合由不同資料型態所組成
mixed_set = {1, 'Python', (2, 5, 10)}
print(mixed_set)
# 集合的元素是不可變的所以程式第6行所設定的元組元素改成
# 第10行串列的寫法將會產生錯誤
# mixed_set = { 1, 'Python', [2, 5, 10]}

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_4.py

# ch10_4.py
x = {}                      # 這是建立空字典非空集合
print("列印     = ", x)
print("列印類別 = ", type(x))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_5.py

# ch10_5.py
empty_dict = {}                      # 這是建立空字典
print("列印類別 = ", type(empty_dict))
empty_set = set()                    # 這是建立空集合
print("列印類別 = ", type(empty_set))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_6.py

# ch10_6.py
x = set('DeepStone mean Deep Learning')
print(x)
print(type(x))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_7.py

# ch10_7.py
# 表達方式1
fruits = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits)
print(x)
# 表達方式2
y = set(['apple', 'orange', 'apple', 'banana', 'orange'])
print(y)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_8.py

# ch10_8.py
cities = set(('Beijing', 'Tokyo', 'Beijing', 'Taipei', 'Tokyo'))
print(cities)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_9.py

# ch10_9.py
fruits1 = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits1)                # 將串列轉成集合
fruits2 = list(x)               # 將集合轉成串列
print("原先串列資料fruits1 = ", fruits1)
print("新的串列資料fruits2 = ", fruits2)

print("------------------------------------------------------------")  # 60個

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
both = math & physics
print("同時參加數學與物理夏令營的成員 ",both)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}         # 定義集合A
B = {3, 4, 5, 6, 7}         # 定義集合B
# 將intersection( )應用在A集合
AB = A.intersection(B)      # A和B的交集
print("A和B的交集是 ", AB)
# 將intersection( )應用在B集合
BA = B.intersection(A)      # B和A的交集
print("B和A的交集是 ", BA)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_12.py

# ch10_12.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
allmember = math | physics
print("同時參加數學與物理夏令營的成員 ",allmember)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}             # 定義集合A
B = {3, 4, 5, 6, 7}             # 定義集合B
# 將union( )應用在A集合
AorB = A.union(B)               # A和B的聯集
print("A和B的聯集是 ", AorB)    
# 將union( )應用在B集合
BorA = B.union(A)               # B和A的聯集
print("B和A的聯集是 ", BorA)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_14.py

# ch10_14.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_only = math - physics
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only)
physics_only = physics - math
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",physics_only)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}             # 定義集合A
B = {3, 4, 5, 6, 7}             # 定義集合B
# 將difference( )應用在A集合
A_B = A.difference(B)           # A-B的差集
print("A-B的差集是 ", A_B)    
# 將difference( )應用在B集合
B_A = B.difference(A)           # B-A的差集
print("B-A的差集是 ", B_A)

print("------------------------------------------------------------")  # 60個

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_sydi_physics = math ^ physics
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
# 將symmetric_difference( )應用在A集合
A_sydi_B = A.symmetric_difference(B)    # A和B的對稱差集
print("A和B的對稱差集是 ", A_sydi_B)    
# 將symmetric_difference( )應用在B集合
B_sydi_A = B.symmetric_difference(A)    # B和A的對稱差集
print("B和A的對稱差集是 ", B_sydi_A)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
C = {1, 2, 3, 4, 5}                     # 定義集合C
# 列出A與B集合是否相等                              
print("A與B集合相等", A == B)
# 列出A與C集合是否相等                             
print("A與C集合相等", A == C)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
C = {1, 2, 3, 4, 5}                     # 定義集合C
# 列出A與B集合是否相等                             
print("A與B集合不相等", A != B)
# 列出A與C集合是否不相等                              
print("A與C集合不相等", A != C)          

print("------------------------------------------------------------")  # 60個

# 方法1
fruits = set("orange")
print("字元a是屬於fruits集合?", 'a' in fruits)
print("字元d是屬於fruits集合?", 'd' in fruits)
# 方法2
cars = {"Nissan", "Toyota", "Ford"}
boolean = "Ford" in cars
print("Ford in cars", boolean)
boolean = "Audi" in cars
print("Audi in cars", boolean)

print("------------------------------------------------------------")  # 60個

# 方法1
fruits = set("orange")
print("字元a是不屬於fruits集合?", 'a' not in fruits)
print("字元d是不屬於fruits集合?", 'd' not in fruits)
# 方法2
cars = {"Nissan", "Toyota", "Ford"}
boolean = "Ford" not in cars
print("Ford not in cars", boolean)
boolean = "Audi" not in cars
print("Audi not in cars", boolean)

print("------------------------------------------------------------")  # 60個

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

def greeting( ):
    """我的第一個Python函數設計"""
    print("Python歡迎你")
    print("祝福學習順利")
    print("謝謝")

# 以下的程式碼也可稱主程式
greeting( )
greeting( )
greeting( )
greeting( )
greeting( )


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_2.py

# ch11_2.py
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi,", name, "Good Morning!")
greeting('Nelson')

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")
greeting('Nelson')

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")

print("------------------------------------------------------------")  # 60個

def interest(interest_type, subject):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print( )

interest('旅遊', '敦煌')
interest('程式設計', 'Python')

print("------------------------------------------------------------")  # 60個

def interest(interest_type, subject):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print( )

interest(interest_type = '旅遊', subject = '敦煌')  # 位置正確
interest(subject = '敦煌', interest_type = '旅遊')  # 位置更動

print("------------------------------------------------------------")  # 60個

def interest(interest_type, subject = '敦煌'):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print( )

interest('旅遊')                                     # 傳遞一個參數
interest(interest_type = '旅遊')                     # 傳遞一個參數
interest('旅遊', '張家界')                           # 傳遞二個參數
interest(interest_type = '旅遊', subject = '張家界') # 傳遞二個參數
interest(subject = '張家界', interest_type = '旅遊') # 傳遞二個參數
interest('閱讀', '旅遊類')                # 傳遞二個參數,不同的主題

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")

ret_value = greeting('Nelson')
print("greeting( )傳回值 = ", ret_value)
print(ret_value, " 的 type  = ", type(ret_value))

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
    return                      # Python將自動回傳None
ret_value = greeting('Nelson')
print("greeting( )傳回值 = ", ret_value)
print(ret_value, " 的 type  = ", type(ret_value))

print("------------------------------------------------------------")  # 60個

def mutifunction(x1, x2):
    """ 加, 減, 乘, 除四則運算 """
    addresult = x1 + x2
    subresult = x1 - x2
    mulresult = x1 * x2
    divresult = x1 / x2
    return addresult, subresult, mulresult, divresult

x1 = x2 = 10
add, sub, mul, div = mutifunction(x1, x2)
print("加法結果 = ", add)
print("減法結果 = ", sub)
print("乘法結果 = ", mul)
print("除法結果 = ", div)

print("------------------------------------------------------------")  # 60個

def guest_info(firstname, middlename, lastname, gender):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = lastname + middlename + firstname + '先生歡迎你'
    else:
        welcome = lastname + middlename + firstname + '小姐歡迎妳'
    return welcome

info1 = guest_info('宇', '星', '洪', 'M')
info2 = guest_info('雨', '冰', '洪', 'F')
print(info1)
print(info2)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_15.py

# ch11_15.py
def guest_info(firstname, lastname, gender, middlename = ''):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = lastname + middlename + firstname + '先生歡迎你'
    else:
        welcome = lastname + middlename + firstname + '小姐歡迎妳'
    return welcome

info1 = guest_info('濤', '劉', 'M')
info2 = guest_info('雨', '洪', 'F', '冰')
print(info1)
print(info2)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_16.py

# ch11_16.py
def build_vip(id, name):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    return vip_dict

member = build_vip('101', 'Nelson')
print(member)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_17.py

# ch11_17.py
def build_vip(id, name, tel = ''):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    if tel:
        vip_dict['Tel'] = tel
    return vip_dict

member1 = build_vip('101', 'Nelson')
member2 = build_vip('102', 'Henry', '0952222333')
print(member1)
print(member2)


print("------------------------------------------------------------")  # 60個

def product_msg(customers):
    str1 = '親愛的: '
    str2 = '本公司將在2020年12月20日北京舉行產品發表會'
    str3 = '總經理:深石敬上'
    for customer in customers:
        msg = str1 + customer + '\n' + str2 + '\n' + str3
        print(msg, '\n')

members = ['Damon', 'Peter', 'Mary']
product_msg(members)

print("------------------------------------------------------------")  # 60個

def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print("菜單: ", current_meal)
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)

def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***", "\n")
    for served_meal in served:
        print(served_meal)

unserved = ['大麥克', '勁辣雞腿堡', '麥克雞塊']   # 所點餐點
served = []                                       # 已服務餐點

# 列出餐廳處理前的點餐內容
show_unserved_meal(unserved)                      # 列出未服務餐點
show_served_meal(served)                          # 列出已服務餐點

# 餐廳服務過程
kitchen(unserved, served)                         # 餐廳處理過程
print("\n", "=== 廚房處理結束 ===", "\n")

# 列出餐廳處理後的點餐內容
show_unserved_meal(unserved)                      # 列出未服務餐點
show_served_meal(served)                          # 列出已服務餐點


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_21.py

# ch11_21.py
def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print("菜單: ", current_meal)
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)

def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***", "\n")
    for served_meal in served:
        print(served_meal)

order_list = ['大麥克', '勁辣雞腿堡', '麥克雞塊']   # 所點餐點
served_list = []                                    # 已服務餐點

# 列出餐廳處理前的點餐內容
show_unserved_meal(order_list)                      # 列出未服務餐點
show_served_meal(served_list)                       # 列出已服務餐點

# 餐廳服務過程
kitchen(order_list, served_list)                    # 餐廳處理過程
print("\n", "=== 廚房處理結束 ===", "\n")

# 列出餐廳處理後的點餐內容
show_unserved_meal(order_list)                      # 列出未服務餐點
show_served_meal(served_list)                       # 列出已服務餐點


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_22.py

# ch11_22.py
def kitchen(unserved, served):
    """ 將所點的餐點轉為已經服務 """
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print("菜單: ", current_meal)
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)

def show_order_meal(unserved):
    """ 顯示所點的餐點 """
    print("=== 下列是所點的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***", "\n")
    for served_meal in served:
        print(served_meal)

order_list = ['大麥克', '勁辣雞腿堡', '麥克雞塊']   # 所點餐點
served_list = []                                    # 已服務餐點

# 列出餐廳處理前的點餐內容
show_order_meal(order_list)                         # 列出所點的餐點
show_served_meal(served_list)                       # 列出已服務餐點

# 餐廳服務過程
kitchen(order_list[:], served_list)                 # 餐廳處理過程
print("\n", "=== 廚房處理結束 ===", "\n")

# 列出餐廳處理後的點餐內容
show_order_meal(order_list)                         # 列出所點的餐點
show_served_meal(served_list)                       # 列出已服務餐點

print("------------------------------------------------------------")  # 60個

def make_icecream(*toppings):
    # 列出製作冰淇淋的配料
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_24.py

# ch11_24.py
def make_icecream(icecream_type, *toppings):
    # 列出製作冰淇淋的配料
    print("這個 ", icecream_type, " 冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream('香草', '草莓醬')
make_icecream('芒果', '草莓醬', '葡萄乾', '巧克力碎片')

print("------------------------------------------------------------")  # 60個

def build_dict(name, age, **players):
    # 建立NBA球員的字典資料
    info = {}           # 建立空字典
    info['Name'] = name
    info['Age'] = age
    for key, value in players.items( ):
        info[key] = value
    return info         # 回傳所建的字典

player_dict = build_dict('James', '32',
                         City = 'Cleveland',
                         State = 'Ohio')

print(player_dict)      # 列印所建字典

print("------------------------------------------------------------")  # 60個

def factorial(n):
    # 計算n的階乘, n 必須是正整數
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

value = 3
print(value, " 的階乘結果是 = ", factorial(value))
value = 5
print(value, " 的階乘結果是 = ", factorial(value))

print("------------------------------------------------------------")  # 60個

def printmsg( ):
    # 函數本身沒有定義變數, 只有執行列印全域變數功能
    print("函數列印: ", msg)    # 列印全域變數

msg = 'Global Variable'         # 設定全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數

print("------------------------------------------------------------")  # 60個

print("111")
def printmsg( ):
    # 函數本身有定義變數, 將執行列印區域變數功能
    msg = 'Local Variable'      # 設定區域變數
    print("函數列印: ", msg)    # 列印區域變數

msg = 'Global Variable'         # 這是全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數

print("------------------------------------------------------------")  # 60個

print("222")
def defmsg( ):
    msg = 'pringmsg variable'

def printmsg( ):
    print(msg)      # 列印defmsg( )函數定義的區域變數

printmsg( )         # 呼叫printmsg( )

print("------------------------------------------------------------")  # 60個

print("333")

def defmsg( ):
    msg = 'pringmsg variable'

print(msg)         # 主程式列印區域變數產生錯誤

print("------------------------------------------------------------")  # 60個

def printmsg():
    global msg
    msg = "Java"        # 更改全域變數
    print("更改後: ", msg)
msg = "Python"
print("更改前: ", msg)
printmsg()

print("------------------------------------------------------------")  # 60個

# 定義lambda函數
square = lambda x: x ** 2

# 輸出平方值
print(square(10))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_32.py

# ch11_32.py
# 使用一般函數
def square(x):
    value = x ** 2
    return value

# 輸出平方值
print(square(10))

print("------------------------------------------------------------")  # 60個

# 定義lambda函數
product = lambda x, y: x * y

# 輸出相乘結果
print(product(5, 10))

print("------------------------------------------------------------")  # 60個

def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)     # 傳回filter object

# 輸出奇數串列
print("奇數串列: ",[item for item in filter_object])





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_35.py

# ch11_35.py
def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)     # 傳回filter object
oddlist = [item for item in filter_object]
# 輸出奇數串列
print("奇數串列: ",oddlist)

print("------------------------------------------------------------")  # 60個

mylist = [5, 10, 15, 20, 25, 30]

oddlist = list(filter(lambda x: (x % 2 == 1), mylist))

# 輸出奇數串列
print("奇數串列: ",oddlist)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_37.py

# ch11_37.py
mylist = [5, 10, 15, 20, 25, 30]

squarelist = list(map(lambda x: x ** 2, mylist))

# 輸出串列元素的平方值
print("串列的平方值: ",squarelist)

print("------------------------------------------------------------")  # 60個

def fun(arg):
    pass

print("------------------------------------------------------------")  # 60個

def fun(arg):
    pass

print("列出fun的type類型   :      ", type(fun))
print("列出lambda的type類型:      ", type(lambda x:x))
print("列出內建函數abs的type類型: ", type(abs))

print("------------------------------------------------------------")  # 60個


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'       # 定義屬性
    def motto(self):            # 定義方法
        return "以客為尊"

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'       # 定義屬性
    def motto(self):            # 定義方法
        return "以客為尊"

userbank = Banks()              # 定義物件userbank
print("目前服務銀行是 ", userbank.title)
print("銀行服務理念是 ", userbank.motto())

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def get_balance(self):                  # 獲得存款餘額
        return self.balance

hungbank = Banks('hung', 100)               # 定義物件hungbank
print(hungbank.name.title( ), " 存款餘額是 ", hungbank.get_balance())

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
hungbank.get_balance()                      # 獲得存款餘額                
hungbank.save_money(300)                    # 存款300元
hungbank.get_balance()                      # 獲得存款餘額
hungbank.withdraw_money(200)                # 提款200元
hungbank.get_balance()                      # 獲得存款餘額

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
johnbank = Banks('john', 300)               # 定義物件johnbank
hungbank.get_balance()                      # 獲得hung存款餘額                
johnbank.get_balance()                      # 獲得john存款餘額
hungbank.save_money(100)                    # hung存款100
johnbank.withdraw_money(150)                # john提款150
hungbank.get_balance()                      # 獲得hung存款餘額                
johnbank.get_balance()                      # 獲得john存款餘額

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = 0                    # 設定開戶金額是0
        self.title = "Taipei Bank"          # 設定銀行名稱

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung')                    # 定義物件hungbank
print("目前開戶銀行 ", hungbank.title)      # 列出目前開戶銀行
hungbank.get_balance()                      # 獲得hung存款餘額                
hungbank.save_money(100)                    # hung存款100
hungbank.get_balance()                      # 獲得hung存款餘額                

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = 0                    # 設定開戶金額是0
        self.title = "Taipei Bank"          # 設定銀行名稱

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung')                    # 定義物件hungbank
hungbank.get_balance()
hungbank.balance = 10000                    # 類別外直接竄改存款餘額
hungbank.get_balance()

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

hungbank = Banks('hung')                    # 定義物件hungbank
hungbank.get_balance()
hungbank.balance = 10000                    # 類別外直接竄改存款餘額
hungbank.get_balance()

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))
        
hungbank = Banks('hung')                    # 定義物件hungbank
usdallor = 50
print(usdallor, " 美金可以兌換 ", hungbank.usa_to_taiwan(usdallor), " 台幣") 

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

class Shilin_Banks(Banks):
    # 定義士林分行
    pass
       
hungbank = Shilin_Banks('hung')             # 定義物件hungbank
hungbank.save_money(500)
hungbank.get_balance()

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   # 獲得銀行名稱
        return self.__title

class Shilin_Banks(Banks):
    # 定義士林分行
    pass

hungbank = Shilin_Banks('hung')             # 定義物件hungbank
print("我的存款銀行是: ", hungbank.bank_title())

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.title = "Taipei Bank"          # 設定公有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   # 獲得銀行名稱
        return self.title

class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.title = "Taipei Bank - Shilin Branch"  # 定義分行名稱

jamesbank = Banks('James')                  # 定義Banks類別物件
print("James's banks = ", jamesbank.title)  # 列印銀行名稱
hungbank = Shilin_Banks('Hung')             # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.title)   # 列印銀行名稱

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   # 獲得銀行名稱
        return self.__title

class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.title = "Taipei Bank - Shilin Branch"  # 定義分行名稱
    def bank_title(self):                   # 獲得銀行名稱
        return self.title

jamesbank = Banks('James')                  # 定義Banks類別物件
print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
hungbank = Shilin_Banks('Hung')             # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.bank_title())   # 列印銀行名稱

print("------------------------------------------------------------")  # 60個

class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name, animal_age ):
        self.name = animal_name # 紀錄動物名稱
        self.age = animal_age   # 紀錄動物年齡

    def run(self):              # 輸出動物 is running
        print(self.name.title(), " is running")

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet ' + dog_name.title(), dog_age)

mycat = Animals('lucy', 5)      # 建立Animals物件以及測試
print(mycat.name.title(), ' is ', mycat.age, " years old.")
mycat.run()

mydog = Dogs('lily', 6)         # 建立Dogs物件以及測試
print(mydog.name.title(), ' is ', mydog.age, " years old.")
mydog.run()

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父的資產 """
    def __init__(self):
        self.grandfathermoney = 10000
    def get_info1(self):
        print("Grandfather's information")

class Father(Grandfather):      # 父類別是Grandfather
    """ 定義父親的資產 """
    def __init__(self):
        self.fathermoney = 8000
        super().__init__()
    def get_info2(self):
        print("Father's information")

class Ivan(Father):             # 父類別是Father
    """ 定義Ivan的資產 """
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()
    def get_info3(self):
        print("Ivan's information")
    def get_money(self):        # 取得資產明細
        print("\nIvan資產: ", self.ivanmoney,
              "\n父親資產: ", self.fathermoney,
              "\n祖父資產: ", self.grandfathermoney)

ivan = Ivan()
ivan.get_info3()                # 從Ivan中獲得
ivan.get_info2()                # 流程 Ivan -> Father
ivan.get_info1()                # 流程 Ivan -> Father -> Grandtather
ivan.get_money()                # 取得資產明細

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch12\ch12_16.py

# ch12_16
class Father():
    """ 定義父親的資產 """
    def __init__(self):
        self.fathermoney = 10000
   
class Ira(Father):                                  # 父類別是Father
    """ 定義Ira的資產 """
    def __init__(self):
        self.iramoney = 8000
        super().__init__()
   
class Ivan(Father):                                 # 父類別是Father
    """ 定義Ivan的資產 """
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()   
    def get_money(self):                            # 取得資產明細
        print("Ivan資產: ", self.ivanmoney,
              "\n父親資產: ", self.fathermoney,
              "\nIra資產 : ", Ira().iramoney)        # 注意寫法

ivan = Ivan()
ivan.get_money()                                    # 取得資產明細

print("------------------------------------------------------------")  # 60個

class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name):
        self.name = animal_name         # 紀錄動物名稱
    def which(self):                    # 回傳動物名稱
        return 'My pet ' + self.name.title()
    def action(self):                   # 動物的行為
        return ' sleeping'

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name):       # 紀錄動物名稱
        super().__init__(dog_name.title())
    def action(self):                   # 動物的行為
        return ' running in the street'

class Monkeys():
    """猴子類別, 這是其他類別 """
    def __init__(self, monkey_name):    # 紀錄動物名稱
        self.name = 'My monkey ' + monkey_name.title()
    def which(self):                    # 回傳動物名稱
        return self.name
    def action(self):                   # 動物的行為
        return ' running in the forest'
    
def doing(obj):                         # 列出動物的行為
    print(obj.which(), "is", obj.action())
    
my_cat = Animals('lucy')                # Animals物件
doing(my_cat)
my_dog = Dogs('gimi')                   # Dogs物件
doing(my_dog)
my_monkey = Monkeys('taylor')           # Monkeys物件
doing(my_monkey)

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action2(self):      # 定義action2()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Ivan(Father, Uncle):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action3(self):      # 定義action3()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Ivan(Father, Uncle):
    """ 定義Ivan類別 """
    def action4(self):
        print("Ivan")

ivan = Ivan()
ivan.action4()              # 順序 Ivan
ivan.action3()              # 順序 Ivan -> Father
ivan.action2()              # 順序 Ivan -> Father -> Uncle
ivan.action1()              # 順序 Ivan -> Father -> Uncle -> Grandfather

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    pass
        
class Father(Grandfather):
    """ 定義父親類別 """
    pass

class Ivan(Father):
    """ 定義Ivan類別 """
    def fn(self):
        pass

grandfather = Grandfather()
father = Father()
ivan = Ivan()
print("grandfather物件類型: ", type(grandfather))
print("father物件類型     : ", type(father))
print("ivan物件類型       : ", type(ivan))
print("ivan物件fn方法類型 : ", type(ivan.fn))

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    pass
        
class Father(Grandfather):
    """ 定義父親類別 """
    pass

class Ivan(Father):
    """ 定義Ivan類別 """
    def fn(self):
        pass

grandfa = Grandfather()
father = Father()
ivan = Ivan()
print("ivan屬於Ivan類別: ", isinstance(ivan, Ivan))
print("ivan屬於Father類別: ", isinstance(ivan, Father))
print("ivan屬於GrandFather類別: ", isinstance(ivan, Grandfather))
print("father屬於Ivan類別: ", isinstance(father, Ivan))
print("father屬於Father類別: ", isinstance(father, Father))
print("father屬於Grandfather類別: ", isinstance(father, Grandfather))
print("grandfa屬於Ivan類別: ", isinstance(grandfa, Ivan))
print("grandfa屬於Father類別: ", isinstance(grandfa, Father))
print("grandfa屬於Grandfather類別: ", isinstance(grandfa, Grandfather))

print("------------------------------------------------------------")  # 60個


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

print('開始計時')
starttime = int(time.time())    # 起始秒數

print("------------------------------------------------------------")  # 60個

import random           # 導入模組random

n = 3
for i in range(n):
    print("1-100     : ", random.randint(1, 100))

for i in range(n):
    print("500-1000  : ", random.randint(500, 1000))

for i in range(n):
    print("2000-3000 : ", random.randint(2000, 3000))

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random

min, max = 1, 100                   # 隨機數最小與最大值設定
num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
print(num)

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print(random.choice(fruits))

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random

porker = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(porker)              # 將次序打亂重新排列
print(porker)

print("------------------------------------------------------------")  # 60個

import time                         # 導入模組time

print("計算1970年1月1日00:00:00至今的秒數 = ", int(time.time()))

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random
import time                         # 導入模組time

min, max = 1, 10
ans = random.randint(min, max)      # 隨機數產生答案
print(ans)

print("------------------------------------------------------------")  # 60個

import time                         # 導入模組time

print(time.asctime())               # 列出目前系統時間 

print("------------------------------------------------------------")  # 60個

import time                         # 導入模組time

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

print("------------------------------------------------------------")  # 60個

print("目前Python版本是: ", sys.version)

print("------------------------------------------------------------")  # 60個

import calendar

print("2020年是否潤年", calendar.isleap(2020))    
print("2021年是否潤年", calendar.isleap(2021))

print("------------------------------------------------------------")  # 60個

import calendar

print(calendar.month(2020,1))

print("------------------------------------------------------------")  # 60個

import calendar

print(calendar.calendar(2020))

print("------------------------------------------------------------")  # 60個

endtime = int(time.time())  # 結束秒數
print("所花時間: ", endtime - starttime, " 秒")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


