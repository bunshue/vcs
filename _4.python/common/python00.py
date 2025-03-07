"""
====================
各種python專用的語法
====================
"""


print("---- python語言區 --------------------------------------------------------")  # 60個


print(globals())

print("__file__ : 此檔案長檔名")
print(__file__)
print(__file__.upper())  # 長檔名轉大寫
print(__file__.lower())  # 長檔名轉小寫

print("__name__ : 目前所在模組名")
print(__name__)
# print(__name__._version)

print("selenium模組的版本")
import selenium

print(selenium.__version__)

# import somemodule as sm	#幫模組取個別名

print(sys.argv)
# print (s.argv)

# 打印使用說明
print(__doc__)

print(__name__)

import pandas
import pandas as pd

print(pandas.__name__)
print(pd.__name__)

if __name__ == "__main__":
    print("happy new year !!")


# 使用dir()內置函數返回一個包含一個模塊中定義名稱的字符串的排序列表。
# 該列表包含在一個模塊中定義的所有模塊，變量和函數的名稱。

# 查看 math
import math

content = dir(math)
print("math 模組所支援的指令 : " + str(content))

# 查看 serial
import serial

content = dir(serial)
print("serial 模組所支援的指令 : " + str(content))

print("------------------------------------------------------------")  # 60個

print("global: ", list(globals().keys()))
print("進入 local:", locals())
print("離開 local:", locals().keys())

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("設定變數")
ROWS, COLUMNS = 19, 4
print(ROWS)
print(COLUMNS)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("冪次方的寫法")
z = 10
print(z)
z = z**0.5  # 冪次方的寫法
print(z)

print("------------------------------------------------------------")  # 60個

person = int(input("請輸入學生人數: "))
apple = int(input("請輸入蘋果總數: "))
ret = divmod(apple, person)
print("每個學生可分得蘋果 " + str(ret[0]) + " 個")
print("蘋果剩餘 " + str(ret[1]) + " 個")

print("------------------------------------------------------------")  # 60個

date1 = "2017-8-23"
date1 = "西元 " + date1
date1 = date1.replace("-", " 年 ", 1)
date1 = date1.replace("-", " 月 ", 1)
date1 += " 日"
print(date1)

print("------------------------------------------------------------")  # 60個


sum = 0


def show(n):
    print("第 " + str(n) + " 次執行迴圈")


print("for迴圈測試")
for i in range(1, 11):
    show(i)
    sum += i
print("1 + 2 + ... + 10 =" + str(sum))

print("------------------------------------------------------------")  # 60個

score = [75, 100, 9]
print("國文成績：%d 分" % score[0])
print("數學成績：%d 分" % score[1])
print("英文成績：%d 分" % score[2])

print("------------------------------------------------------------")  # 60個

for i in range(2, 10):
    for j in range(1, 10):
        product = i * j
        print("%d * %d = %-2d   " % (i, j, product), end="")
    print()

print("------------------------------------------------------------")  # 60個

print("求1~N的正整數的和")
sum = 0
# n = int(input('請輸入正整數：'))
n = 1234
for i in range(1, n + 1):
    sum += i
print("1 到 %d 的整數和為 %d" % (n, sum))

print("------------------------------------------------------------")  # 60個

print("求是否為質數")
# n = int(input('請輸入大於 1 的整數：'))
n = 12377
if n == 2:
    print("2 是質數！")
else:
    for i in range(2, n):
        if n % i == 0:
            print("%d 不是質數！" % n)
            break
    else:
        print("%d 是質數！" % n)

print("------------------------------------------------------------")  # 60個

total = person = score = 0
while score != -1:
    person += 1
    total += score
    score = int(input("請輸入第 %d 位學生的成績：" % person))
average = total / (person - 1)
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))

print("------------------------------------------------------------")  # 60個

score = []
total = inscore = 0
while inscore != -1:
    inscore = int(input("請輸入學生的成績："))
    score.append(inscore)
print("共有 %d 位學生" % (len(score) - 1))
for i in range(0, len(score) - 1):
    total += score[i]
average = total / (len(score) - 1)
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))

print("------------------------------------------------------------")  # 60個

nat = input("請輸入國文成績：")
math = input("請輸入數學成績：")
eng = input("請輸入英文成績：")
sum = int(nat) + int(math) + int(eng)  # 輸入值需轉換為整數
average = sum / 3
print("成績總分：%d，平均成績：%5.2f" % (sum, average))

print("------------------------------------------------------------")  # 60個

score = int(input("請輸入成績："))
if score >= 90:
    print("優等")
elif score >= 80:
    print("甲等")
elif score >= 70:
    print("乙等")
elif score >= 60:
    print("丙等")
else:
    print("丁等")

print("------------------------------------------------------------")  # 60個

# pw = input('請輸入密碼：(1234)')
pw = "1234"
if pw == "1234":
    print("歡迎光臨！")
else:
    print("密碼錯誤！")

password = "123"
# pAttempt = input('Enter the password:(123) ')
pAttempt = "123"
while pAttempt != password:
    print("Password incorrect")
    pAttempt = input("Enter the password: ")
print("Password correct")

print("------------------------------------------------------------")  # 60個

personName = "lion"
anObject = "mouse"
place = "cat dog"
story = (
    personName
    + " was walking through "
    + place
    + ". "
    + place
    + " was not usually very interesting. "
    + personName
    + " spotted a small "
    + anObject
    + ". Suddenly the "
    + anObject
    + " jumped up and ran away. "
    + personName
    + " decided not to go to "
    + place
    + " again."
)
print(story)

print("------------------------------------------------------------")  # 60個

age = 70
if 18 <= age <= 59:
    print("票價為1800元")
elif 60 <= age:
    print("票價為1000元")
else:
    print("無法賣出電影票")

print("------------------------------------------------------------")  # 60個

pointcard = True
count = 5
if pointcard == True and count == 5:
    print("感謝您的長久惠顧，此次為1000元優惠價")

counter = 0
while counter < 5:
    print(counter)
    counter = counter + 1

while True:
    print("揮拳")
    print("腳踢")
    break
    print("必殺奧義")

power = 2

while True:
    print("揮拳")
    print("腳踢")
    print("必殺奧義")
    power = power - 1
    if power == 0:
        break

print("------------------------------------------------------------")  # 60個

print("多重指定 Multiple Assignment")

x, y, z = 123, 456, 789

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
