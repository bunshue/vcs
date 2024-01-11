import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\CalculateSalary.py

#設置底薪(BaseSalary)、結案獎金件數(Case)、職位獎金(OfficeBonus)
BaseSalary = 25000
CaseBonus = 1000
OfficeBonus = 5000


#請輸入職位名稱(Engineer)、結案獎金金額(CaseAmount)變數
Engineer = str(input("請輸入職位名稱："))
Case = int(input("請輸入結案案件數(整數)："))


#計算獎金function
def CalculateCase(case, caseBonus):
    return case * caseBonus

def CalculateSalary(baseSalary, officeBonus):
    return baseSalary + officeBonus

CaseAmount = CalculateCase(Case, CaseBonus)
SalaryAmount = CalculateSalary(BaseSalary, OfficeBonus)

print("該工程師薪資：", CaseAmount + SalaryAmount)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExCalendar.py

import calendar

y = int(input("請輸入年份:"))
m = int(input("請輸入月份:"))
ys = int(input("列印n年內為閏年的月曆:"))
notLeap = []

calendar.setfirstweekday(calendar.SUNDAY)

for i in range(ys):
    if calendar.isleap(y+i) == True:
        print("\n")
        calendar.prmonth(y+i, m)
    else:
        notLeap.append(y+i)

print("\n以下非閏年:", notLeap)
print("{}到{}期間有幾個閏年:{}".format(y, y+ys, calendar.leapdays(y, y+ys)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExMath.py

import math
x = 10
y = -2

z = math.fabs(x / y)
h = math.factorial(z)

if math.isnan(h) == False:
    print("計算後數值：", h)
    print("最大公約數：", math.gcd(h, x))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExRandomSort.py

import random
name = ["小明", "小黃", "小紅", "小綠", "小白"]

print("抽取一個元素：", random.choice(name))

print("抽取三個元素：", random.sample(name, 3))

print("抽取三個元素：", random.shuffle(name))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExRandrange.py

import random

print("任一整數", random.randrange(100))

print("任一整數", random.randrange(52, 100))

print("奇數", random.randrange(1, 100, 2))

print("偶數", random.randrange(0, 100, 2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExTime.py

import time

t = time.time()
tLocal = time.localtime(t)

print("轉換時間形式(年/月/日)：", time.strftime("%Y/%m/%d", tLocal))
print("轉換時間形式(年/月/日 時:分:秒)：", time.asctime (tLocal))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\GetParam.py

import sys
if len(sys.argv) < 0:
    print("未有外部傳入參數")
else:
    print("Python版本號：", sys.version)
    print("作業系統：", sys.platform)

    for n in range(len(sys.argv)):
        print("param" + str(n) + "：", sys.argv[n])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\import.py

import random

for i in range(5):
    a = random.randint(1,10) #隨機取得整數
    print(a,end=' ')
print()
#給定items數列的初始值
word = ['apple','bird','tiger','happy','quick']
random.shuffle(word)  #使用shuffle函數打亂字的順序
print(word)#將打亂後字依序輸出

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


