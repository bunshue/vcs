import sys

print("------------------------------------------------------------")  # 60個

""" fail
import time as t

timestart = t.clock()
for i in range (0,1000):
    for j in range (0,1000):
        n = i * j
timeend = t.clock()
print("執行一百萬次整數運算的時間：" + str(timeend-timestart) + " 秒")
"""

print("------------------------------------------------------------")  # 60個

import time as t

week = ["一", "二", "三", "四", "五", "六", "日"]
dst = ["無日光節約時間", "有日光節約時間"]
time1 = t.localtime()
show = "現在時刻：中華民國 " + str(int(time1.tm_year)-1911) +" 年 "
show += str(time1.tm_mon) + " 月 " + str(time1.tm_mday) + " 日 "
show += str(time1.tm_hour) + " 點 " + str(time1.tm_min) + " 分 "
show += str(time1.tm_sec) + " 秒 星期" + week[time1.tm_wday] + "\n"
show += "今天是今年的第 " + str(time1.tm_yday) + " 天，此地" + dst[time1.tm_isdst]
print(show)

print("------------------------------------------------------------")  # 60個

import time as t

timestart = t.perf_counter() 
for i in range (0,1000):
    for j in range (0,1000):
        n = i * j
timeend = t.perf_counter() 
print("執行一百萬次整數運算的時間：" + str(timeend-timestart) + " 秒")

print("------------------------------------------------------------")  # 60個

"""
import time as t

timestart = t.clock()
for i in range (0,1000):
    for j in range (0,1000):
        n = float(i) * float(j)
timeend = t.clock()
print("執行一百萬次浮點數運算的時間：" + str(timeend-timestart) + " 秒")
"""
print("------------------------------------------------------------")  # 60個

date1 = "2017-8-23"
date1 = "西元 " + date1
date1 = date1.replace("-", " 年 ", 1)
date1 = date1.replace("-", " 月 ", 1)
date1 += " 日"
print(date1)

print("------------------------------------------------------------")  # 60個

import time as t

time1 = t.localtime()
show = "今天是今年的第 " + str(time1.tm_yday) + " 天，屬於"
if time1.tm_yday < 184 : show += "上半年。"
else :  show += "下半年。"
print(show)

print("------------------------------------------------------------")  # 60個

"""
import time as t

timestart = t.perf_counter() ()
for i in range (0,1000):
    for j in range (0,1000):
        n = float(i) * float(j)
timeend = t.perf_counter() ()
print("執行一百萬次浮點數運算的時間：" + str(timeend-timestart) + " 秒")
"""
print("------------------------------------------------------------")  # 60個

time1 = "10:23:41"
time1 = time1.replace(":", " 點 ", 1)
time1 = time1.replace(":", " 分 ", 1)
time1 += " 秒"
print(time1)

print("------------------------------------------------------------")  # 60個

import random as r

list1 = r.sample(range(1,50), 7)
special = list1.pop()
list1.sort()
print("本期大樂透中獎號碼為：", end="")
for i in range(0,6):
    if i == 5:    print(str(list1[i]))
    else:    print(str(list1[i]), end=", ")
print("本期大樂透特別號為：" + str(special))

print("------------------------------------------------------------")  # 60個

import time as t

time1 = t.localtime()
show = "現在時刻："
if time1.tm_hour < 12: 
    show += "上午 "
    hour = time1.tm_hour
else:
    show += "下午 "
    hour = time1.tm_hour - 12
show += str(hour) + " 點 " + str(time1.tm_min) + " 分 "
show += str(time1.tm_sec) + " 秒"
print(show)

print("------------------------------------------------------------")  # 60個

list1=[3,2,1,5] #[3, 2, 1, 5]
list2=sorted(list1,reverse=True)
print(list2)    #[5, 3, 2, 1]
print(list1)    #[3, 2, 1, 5]

print("------------------------------------------------------------")  # 60個

list1 = [1,2,3,4,5,6]
del list1[1]
print(list1) #[1,3,4,5,6]       

print("------------------------------------------------------------")  # 60個

dict1 = {"A":"內向穩重", "B":"外向樂觀", "O":"堅強自信", "AB":"聰明自然"}
name = "O"
blood = dict1.get(name)
if blood == None:  
    print("沒有「" + name + "」血型！")
else:  
    print(name + " 血型的個性為：" + str(dict1[name]))

print("------------------------------------------------------------")  # 60個

dict1 = {"林小明":85, "曾山水":93, "鄭美麗":67}
name = "鄭美麗"
if name in dict1:  
    print(name + "的成績為 " + str(dict1[name]))
else:  
    score = input("輸入學生分數：")
    dict1[name] = score
    print("字典內容：" + str(dict1))

print("------------------------------------------------------------")  # 60個

dict1={"金牌":26, "銀牌":34, "銅牌":30}
item1 = dict1.items()
for name, num in item1:
    print("得到的 %s 數目為 %d 面" % (name, num))

print("------------------------------------------------------------")  # 60個

dict1={"金牌":26, "銀牌":34, "銅牌":30}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("得到的 %s 數目為 %d 面" % (listkey[i], listvalue[i]))

print("------------------------------------------------------------")  # 60個

person = 7
apple = 52
ret = divmod(apple, person)
print("每個學生可分得蘋果 " + str(ret[0]) + " 個")
print("蘋果剩餘 " + str(ret[1]) + " 個")

print("------------------------------------------------------------")  # 60個

listname = ["林大明", "陳阿中", "張小英"]
listchinese = [100, 74, 82]
listmath = [87, 88, 65]
listenglish = [79, 100, 8]
print("姓名     座號  國文  數學  英文")
for i in range(0,3):
    print(listname[i].ljust(5), str(i+1).rjust(3), str(listchinese[i]).rjust(5), str(listmath[i]).rjust(5), str(listenglish[i]).rjust(5))

print("------------------------------------------------------------")  # 60個

def disp_data(): # 顯示串列的自訂程序
    for item in datas:
        print(item,end=" ")
    print()        

# 主程式
datas=[3,5,2,1]  
print("排序前：",end=" ")
disp_data() # 顯示排序前串列
n=len(datas)-1 # 串列長度-1

for i in range(0,n): 
    for j in range(0,n-i):         
        if (datas[j]>datas[j+1]): # 由小到大排序
            datas[j],datas[j+1]=datas[j+1],datas[j] # 兩數互換

print("排序後：",end=" ")  
disp_data()  # 顯示排序後串列 

print("------------------------------------------------------------")  # 60個

def disp_data(): # 顯示串列的自訂程序
    for item in datas:
        print(item,end=" ")
    print()        

# 主程式
datas=[3,5,2,1]  
print("排序前：",end=" ")
disp_data() # 顯示排序前串列
n=len(datas)-1 # 串列長度-1

for i in range(0,n): 
    for j in range(0,n-i):      
        print("i=%d j=%d" %(i,j))
        if (datas[j]>datas[j+1]): # 由大到小排序
            print("%d,%d 互換後" %(datas[j],datas[j+1]) ,end="：")
            datas[j],datas[j+1]=datas[j+1],datas[j] # 兩數互換
        print(datas)

print("排序後：",end=" ")  
disp_data()  # 顯示排序後串列 

print("------------------------------------------------------------")  # 60個

dict1 = {"春季":"暖和", "夏季":"炎熱", "秋季":"涼爽", "冬季":"寒冷"}
name = "春季"
feeling = dict1.get(name)
if feeling == None:  
    print("沒有「" + name + "」季節！")
else:  
    print(name + "的天氣為 " + str(dict1[name]))

print("------------------------------------------------------------")  # 60個

dict1 = {"電視":15000, "冰箱":23000, "冷氣":28000}
name = "冰箱"
if name in dict1:  
    print(name + "的價格為 " + str(dict1[name]))
else:  
    price = input("輸入電器價格：")
    dict1[name] = price
    print("字典內容：" + str(dict1))

print("------------------------------------------------------------")  # 60個

dict1 = {"水瓶座":"活潑善變", "雙魚座":"迷人保守", "白羊座":"天生勇者", "金牛座":"熱情敏感"}
item1 = dict1.items()
for name, nature in item1:
    print("%s 的性格特癥為 %s" % (name, nature))

print("------------------------------------------------------------")  # 60個

dict1 = {"水瓶座":"活潑善變", "雙魚座":"迷人保守", "白羊座":"天生勇者", "金牛座":"熱情敏感"}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("%s 的性格特癥為 %s" % (listkey[i], listvalue[i]))

print("------------------------------------------------------------")  # 60個

ret = divmod(10000, 350)
print("可維持生活 " + str(ret[0]) + " 天")
print("生活費剩餘 " + str(ret[1]) + " 元")

print("------------------------------------------------------------")  # 60個

listname = ["鍾明達", "鄭廣月", "何美麗"]
list1 = [34210, 23600, 145000, 54300]
list2 = [9000, 23900, 83400, 132000]
list3 = [186500, 127800, 100000, 45000]
list4 = [78900, 125000, 90000, 8000]
print("姓名       第一季  第二季  第三季   第四季")
for i in range(0,3):
    print(listname[i].ljust(5), str(list1[i]).rjust(7), str(list2[i]).rjust(7), str(list3[i]).rjust(7), str(list4[i]).rjust(7))

print("------------------------------------------------------------")  # 60個

import random as r

list1 = r.sample(range(0,10), 4)
list1.sort()
print("本期四星彩中獎號碼為：", end="")
for i in range(0,4):
    if i == 3:    print(str(list1[i]))
    else:    print(str(list1[i]), end=", ")

print("------------------------------------------------------------")  # 60個

def disp_data(): # 顯示串列的自訂程序
    for item in datas:
        print(item,end=" ")
    print()        

# 主程式
datas=datas=[2,3,5,7,1]  
print("排序前：",end=" ")
disp_data() # 顯示排序前串列
n=len(datas)-1 # 串列長度-1

for i in range(0,n): 
    for j in range(0,n-i):         
        if (datas[j]<datas[j+1]): # 由大到小排序
            datas[j],datas[j+1]=datas[j+1],datas[j] # 兩數互換

print("排序後：",end=" ")  
disp_data()  # 顯示排序後串列 

print("------------------------------------------------------------")  # 60個

numbers = [21, 4, 35, 1, 8, 7, 3, 6, 9]
odd_numbers = []
for number in numbers:
    if (number % 2 != 0): #將奇數放入 odd_numbers 串列
        odd_numbers.append(number)
print(odd_numbers)

print("------------------------------------------------------------")  # 60個

numbers = [1, 2, 3, 4, 2, 7, 3, 2, 3]
numbers2 = []
for number in numbers:
    n = numbers2.count(number)  #計算出現次數
    if (n == 0): #將不重複數字放入 numbers2 串列
        numbers2.append(number)
print(numbers2)

print("------------------------------------------------------------")  # 60個

monthname = {1:'JAN', 2:'FEB', 3:'MAR', 4:'APR', 5:'MAY', 6:'JUN', 7:'JUL', 8:'AUG', 9:'SEP', 10:'OCT', 11:'NOV', 12:'DEC'}
m = 3
print("{}月份的英文簡寫為 {}：".format(m, monthname[m]))

print("------------------------------------------------------------")  # 60個

cnum = {0:"零", 1:"壹", 2:"貮", 3:"參", 4:"肆", 5:"伍", 6:"陸", 7:"柒", 8:"捌", 9:"玖"}
num = "1234"
for n in num:
    print(cnum[int(n)], end="")

print("------------------------------------------------------------")  # 60個

dict1 = {"台北市":6, "新北市":2, "桃園市":5, "台中市":8, "台南市":3, "高雄市":9}
name = "新北市"
PM25 = dict1.get(name)
if PM25 == None:  
    print("六都中沒有「" + name + "」城市！")
else:  
    print(name + " 今天的 PM2.5 值為：" + str(dict1[name]))

print("------------------------------------------------------------")  # 60個

dict1 = {"鼠":"親切和藹", "牛":"保守努力", "虎":"熱情大膽", "兔":"溫柔仁慈"}
for name, nature in dict1.items():
    print("生肖屬 %s 的性格特癥為 %s" % (name, nature))

print("------------------------------------------------------------")  # 60個

rate = {'USD':28.02, 'JPY':0.2513, 'CNY':4.24}
TWD = float("123.456")
print("台幣{:.2f}元等於美金{:.2f}元, 日幣{:.2f}元, 人民幣{:.2f}元".format(TWD, TWD/rate['USD'], TWD/rate['JPY'], TWD/rate['CNY']))

print("------------------------------------------------------------")  # 60個

def change(n,coin): # 換硬幣
    m = n // coin   # 硬幣數
    return m    

money=[50,10,5,1]
n=int(input("請輸入換幣金額："))
while (n>0):
    for i in range(len(money)):
        coin = money[i]
        if (n >= coin):
            m = change(n,coin) # 換硬幣
            print("{}元 * {}個" .format(coin,m))
            n= n % coin

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\NNNNNN\Python零基礎入門班(第三版)學習資源\Python零基礎入門班(第三版)\綜合演練\ch08\ch08_ex1.py

def disp_scores(): # 顯示串列的自訂程序
    for score in scores:
        print(score,end=" ")
    print()

scores = []
while True:
    inscore = input("請輸入學生的成績：")
    if (inscore==""):
        break
    # 將成績轉為數值後加入 scores 串列中
    scores.append(int(inscore))  
    
print("排序前：",end=" ")
disp_scores()   # 顯示排序前串列
n=len(scores)-1 # 串列長度-1

for i in range(0,n): 
    for j in range(0,n-i):         
        if (scores[j]<scores[j+1]): # 由大到小排序
            scores[j],scores[j+1]=scores[j+1],scores[j] # 兩數互換    

print("成績由大到小排序：",end="") 
disp_scores() # 顯示排序後串列

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\NNNNNN\Python零基礎入門班(第三版)學習資源\Python零基礎入門班(第三版)\綜合演練\ch08\ch08_ex2.py

num=[67,12,9,52,91,3]
datas=[]

for i in range(0,3):     
    no = int(input("請輸入第 " + str(i+1) + " 個號碼："))
    # 將號碼轉為數值後加入 datas 串列中
    datas.append(no)  

n=0
for i in range(0,3): 
    for j in range(len(num)):   #逐一比對搜尋 
        if (num[j]==datas[i]):  #號碼相符 
            n+=1
            break               #結束比對

if (n>0):
    print("恭喜您，中了",n,"個號碼!")
else:
    print("可惜，您未中獎！") 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\NNNNNN\Python零基礎入門班(第三版)學習資源\Python零基礎入門班(第三版)\綜合演練\ch08\ch08_ex3.py

names=["David","Lily","Chiou","Bear","Shantel","Cynthia"]
n=len(names)-1 # 串列長度-1
for i in range(0,n): 
    for j in range(0,n-i):         
        if (names[j]>names[j+1]): # 由小到大排序
            names[j],names[j+1]=names[j+1],names[j] # 互換  
                
while True:     
    name = input("請輸入中獎者的名單(Enter結束)：")
    if (name==""):
        break    

    IsFound=False
    min=0
    max=n    
    while(min<=max):
        mid=int((min+max)/2)
        if (names[mid].upper()==name.upper()):  #姓名相符 
            IsFound=True
            break
        if (names[mid].upper()>name.upper()): #如果中間值大於輸入值 
           max=mid-1      #使用較小的一半區域繼續比對 
        else:             #如果中間值不大於輸入值 
           min=mid+1      #使用較大的一半區域繼續比對 
           
    if (IsFound==True):
        print("恭喜您，",name,"中獎了!")
    else:
        print("可惜，",name,"未中獎！")   

print("------------------------------------------------------------")  # 60個




fruits = ["香蕉","蘋果","橘子","鳳梨","西瓜"]
while True:
    print("串列元素有：",fruits)
    fruit = input("請輸入要刪除的水果(Enter 結束)：")
    if (fruit==""):
        break
    n = fruits.count(fruit) 
    if (n>0):  # 串列元素存在
        fruits.remove(fruit)
    else:
        print(fruit,"不在串列中!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\NNNNNN\Python零基礎入門班(第三版)學習資源\Python零基礎入門班(第三版)\各章範例\ch05\sequential.py




scores = []

scores.append(int(inscore))  

scores2=sorted(scores,reverse=True) # 由大到小排序
print("成績由大到小排序：",scores2) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\NNNNNN\Python零基礎入門班(第三版)學習資源\Python零基礎入門班(第三版)\各章範例\ch05\tespy

innum = 0
list1 = []
while(innum != -1):
    innum = int(input("請輸入電費 (-1：結束)："))
    list1.append(innum)
list1.pop()
print("共輸入 %d 個數" % len(list1))
print("最多電費為：%d" % max(list1))
print("最少電費為：%d" % min(list1))
print("電費總和為：%d" % sum(list1))
print("電費由大到小排序為：{}".format(sorted(list1, reverse=True)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\NNNNNN\Python零基礎入門班(第三版)學習資源\Python零基礎入門班(第三版)\各章範例\ch07\startswith.py


print("------------------------------------------------------------")  # 60個

print("姓名    成績")
print("%-4s  %3d" % (name1, score1))
print("%-4s  %3d" % (name2, score2))


colors = ["紅","橙","黃","綠","藍"]
while True:
    print("顏色有：",colors)
    color = input("請輸入要刪除的顏色(Enter 結束)：")
    if (color==""):
        break
    n = colors.count(color) 
    if (n>0):  # 串列元素存在
        colors.remove(color)
    else:
        print(color,"不在串列中!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\NNNNNN\Python零基礎入門班(第三版)學習資源\Python零基礎入門班(第三版)\延伸練習\ch05\sorted1_cl.py

scores = []
while True:
    inscore = input("請輸入學生的成績：")
    if (inscore==""):
        break
    # 將成績轉為數值後加入 scores 串列中
    scores.append(int(inscore))  

scores2=sorted(scores,reverse=False) # 由小到大排序
print("成績由小到大排序：",scores2) 

print("------------------------------------------------------------")  # 60個

innum = 0
list1 = []
for i in range(0,4):
    innum = int(input("請輸入第 " + str(i+1) + " 個月的支出金額："))
    list1.append(innum)
print("支出最多的金額為：%d" % max(list1))
print("支出最少的金額為：%d" % min(list1))
print("支出的總額為：%d" % sum(list1))
print("支出金額由小到大排序為：{}".format(sorted(list1)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\NNNNNN\Python零基礎入門班(第三版)學習資源\Python零基礎入門班(第三版)\延伸練習\ch08\binary_cl.py


fruits = ["香蕉","蘋果","橘子","鳳梨","s"]
while True:
    fruit = input("請輸入喜歡的水果(Enter 結束)：")
    if (fruit==""):
        break
    n = fruits.count(fruit) 
    if (n>0):  # 串列元素存在
        p=fruits.index(fruit)
        print("%s 在串列中的第 %d 項" %(fruit,p+1))
    else:
        print(fruit,"不在串列中!")

print("------------------------------------------------------------")  # 60個


scores = []
names= []
for i in range(1,4):
    name = input("請輸入第 " + str(i) + " 同學的姓名：")
    inscore = int(input("請輸入第 " + str(i) + " 同學的成績："))
    # 將姓名、成績加入 names、scores 串列中
    names.append(name)
    scores.append(inscore)    
scores2=sorted(scores,reverse=True) # 由大到小排序 
# 取得最大數在 scores 串列的索引位置
n = scores.index(scores2[0])  
print("姓名： %s    成績： %d" %(names[n],scores[n])) 


innum = 0
list1 = []
for i in range(0,4):
    innum = int(input("請輸入第 " + str(i+1) + " 位同學分數："))
    list1.append(innum)
print("最高分為：%d" % max(list1))
print("最低分為：%d" % min(list1))
print("總分為：%d" % sum(list1))
print("平均為：%6.2f" % (sum(list1)/4))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\NNNNNN\Python零基礎入門班(第三版)學習資源\Python零基礎入門班(第三版)\綜合演練\ch07\ch07_ex4.py

