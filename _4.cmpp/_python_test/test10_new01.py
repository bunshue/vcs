# Python 新進測試 01


print('map 的用法')
def pick(x):
    fruits = ['Apple', 'Banana', 'Orange', 'Tomato', 'Pine Apple', 'Berry']
    return fruits[x]

alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]
choices = map(pick, alist)
for choice in choices:
    print(choice)




from sympy import *
x,y,z=symbols('x y z')
init_printing()
Integral(sqrt(1/x),x)



# Python 新進測試 03

# _*_ coding: utf-8 _*_
# 程式 9-1  (Python 3 version)
from urllib.parse import urlparse

url = 'https://www.most.gov.tw/folksonomy/list?menu_id=ba3d22f3-96fd-4adf-a078-91a05b8f0166&filter_uid=none&listKeyword=&pageNum=2&pageSize=18&view_mode=listView&subSite=main&l=ch&tagUid='

uc = urlparse(url)
print("NetLoc:", uc.netloc)
print("Path:", uc.path)

q_cmds = uc.query.split('&')
print("Query Commands:")
for cmd in q_cmds:
    print(cmd)




# Python 新進測試 11

#web = input("請輸入網址：")
web = 'https://www.google.com.tw/'

if web.startswith("http://") or web.startswith("https://"):
    print("輸入的網址格式正確！")
else:
    print("輸入的網址格式錯誤！")
   
    
person = int(input("請輸入學生人數: "))
apple = int(input("請輸入蘋果總數: "))
ret = divmod(apple, person)
print("每個學生可分得蘋果 " + str(ret[0]) + " 個")
print("蘋果剩餘 " + str(ret[1]) + " 個")

listname = ["林大明", "陳阿中", "張小英"]
listchinese = [100, 74, 82]
listmath = [87, 88, 65]
listenglish = [79, 100, 8]
print("姓名     座號  國文  數學  英文")
for i in range(0,3):
    print(listname[i].ljust(5), str(i+1).rjust(3), str(listchinese[i]).rjust(5), str(listmath[i]).rjust(5), str(listenglish[i]).rjust(5))


date1 = "2017-8-23"
date1 = "西元 " + date1
date1 = date1.replace("-", " 年 ", 1)
date1 = date1.replace("-", " 月 ", 1)
date1 += " 日"
print(date1)

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



# Python 新進測試 10


'''
sum = 0

def show(n):
    print("第 " + str(n) + " 次執行迴圈")
    
print('for迴圈測試')
for i in range(1,11):
    show(i)
    sum += i
print("1+2+...+10 = " + str(sum))


pw = input("請輸入密碼：(1234)")
if(pw=="1234"):
    print("歡迎光臨！")
else:
    print("密碼錯誤！")
    
    
nat = input("請輸入國文成績：")
math = input("請輸入數學成績：")
eng = input("請輸入英文成績：")
sum = int(nat) + int(math) + int(eng)  #輸入值需轉換為整數
average = sum / 3
print("成績總分：%d，平均成績：%5.2f" % (sum, average))


money = int(input("請輸入購物金額："))
if(money >= 10000):
    if(money >= 100000):
        print(money * 0.8, end=" 元\n")  #八折
    elif(money >= 50000):
        print(money * 0.85, end=" 元\n")  #八五折
    elif(money >= 30000):
        print(money * 0.9, end=" 元\n")  #九折
    else:
        print(money * 0.95, end=" 元\n")  #九五折
else:
    print(money, end=" 元\n")  #未打折
    
    
    
print("格式化列印")
print("姓名   座號  國文  數學  英文")
print("%3s  %2d   %3d   %3d  %3d" % ("林大明", 1, 100, 87, 79))
print("%3s  %2d   %3d   %3d  %3d" % ("陳阿中", 2, 74, 88, 100))
print("%3s  %2d   %3d   %3d  %3d" % ("張小英", 11, 82, 65, 8))

score = int(input("請輸入成績："))
if(score) >= 90:
    print("優等")
elif(score) >= 80:
    print("甲等")
elif(score) >= 70:
    print("乙等")
elif(score) >= 60:
    print("丙等")
else:
    print("丁等")
    
    
    
n = int(input("請輸入大樓的樓層數："))
print("本大樓具有的樓層為：")
if(n > 3):
    n += 1
for i in range(1, n+1):
    if(i==4):
        continue
    print(i, end=" ")
print()


score = [85, 79, 93]
print("國文成績：%d 分" % score[0])
print("數學成績：%d 分" % score[1])
print("英文成績：%d 分" % score[2])


for i in range(1,10):
    for j in range(1,10):
        product = i * j
        print("%d*%d=%-2d   " % (i, j, product), end="")
    print()



sum = 0
n = int(input("請輸入正整數："))
for i in range(1, n+1):
    sum += i
print("1 到 %d 的整數和為 %d" % (n, sum))
'''

'''
score = []
total = inscore = 0
while(inscore != -1):
    inscore = int(input("請輸入學生的成績："))
    score.append(inscore)
print("共有 %d 位學生" % (len(score) - 1))
for i in range(0, len(score) - 1):
    total += score[i]
average = total / (len(score) - 1)
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))





n = int(input("請輸入大於 1 的整數："))
if(n == 2):
    print("2 是質數！")
else:
    for i in range(2, n):
        if(n % i == 0):
            print("%d 不是質數！" % n)
            break
    else:
        print("%d 是質數！" % n)



total = person = score = 0
while(score != -1):
    person += 1
    total += score
    score = int(input("請輸入第 %d 位學生的成績：" % person))
average = total / (person - 1)
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))


'''


















