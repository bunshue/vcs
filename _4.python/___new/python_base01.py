"""
跟著阿才學Python從基礎到網路爬蟲應用


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch01\first.py

# -*- 第一個 Python 範例 -*-
"""
撰寫日期：2019-12-18
開發人員: 蔡文龍
程式版本：v1.0
"""
print("歡迎光臨 Python 的世界")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch02\in.py

print("1" in "123")  # 字串搜尋：判斷 "1" 是否在 "123" 內，成立顯示True
print("13" in "123")  # 字串搜尋：判斷 "13" 是否在 "123" 內，不成立顯示False
print("M" in "ASP.NET MVC")  # 字串搜尋：判斷 "M" 是否在 "ASP.NET MVC" 內，成立顯示True
print(7 not in [1, 2, 3])  # 串列搜尋：判斷 7 是否不在串列內，成立顯示True
print(1 not in [1, 2, 3])  # 串列搜尋：判斷 1 是否不在串列內，不成顯示False

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch02\type01.py

num = 15  # 以十進制表示15
num0b = 0b1111  # 以二進制表示15
num0o = 0o17  # 以八進制表示15
num0x = 0xF  # 以十六進制表示15
print(num)  # 印出15，print()函式可印出指定的資料
print(num0b)  # 印出15
print(num0o)  # 印出15
print(num0x)  # 印出15

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch02\type02.py

name = "小明"  # 也可以撰寫成 name="小明"，name為字串變數
score = 87.5  # score為浮點數變數
gender = True  # gender為布林變數
print("姓名 =", name)
print("分數 =", score)
print("性別(男:True, 女:False) =", gender)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch02\type03.py

name = "小明"  # 也可以撰寫成 name="小明"，name為字串變數
score = 87.5  # score為浮點數變數
gender = True  # gender為布林變數
print("姓名 =", name)
print("分數 =", score)
print("性別(男:True, 女:False) =", gender)
print("姓名name變數型別 =", type(name))
print("分數score變數型別 =", type(score))
print("性別gender變數型別 =", type(gender))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\format01.py

print("{:<5}".format(123))  # 顯示123ΔΔ
print("{:>5}".format(123))  # 顯示ΔΔ123
print("{:^6}".format(123))  # 顯示Δ123ΔΔ
print("{:@<6}".format(123))  # 顯示123@@@

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\format02.py

print("{:#b}".format(12345))  # 顯示0b11000000111001
print("{:#o}".format(12345))  # 顯示0o30071
print("{:#x}".format(12345))  # 顯示0x3039

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\format03.py

print("{:d}".format(12345))  # 顯示整數資料12345
print("{:7d}".format(12345))  # 設寬度為7,寬度有剩時補空格，顯示ΔΔ12345
print("{:s}".format("ABCDE"))  # 顯示字串資料，顯示ABCDE
print("{:>7s}".format("ABCDE"))  # 設寬度為7,寬度有剩時補空格，顯示ΔΔABCDE
print("{:f}".format(1234.567))  # 小數位數預設6位，顯示1234.567000
print("{:f}".format(-123.45))  # 小數位數預設6位，顯示-123.450000
print("{:.2f}".format(12.345))  # 指定小數位數2位,第3位四捨五入，顯示12.35
print("{:8.2f}".format(-12.3456))  # 指定總寬度8位,小數3位，顯示ΔΔ-12.35
print("{:3.1f}".format(123.45))  # 指定寬度為3且小數1位，寬度不足時全部顯示123.5
print("{:8.0f}".format(-1234.56))  # 指定小數位數0位,第1位四捨五入，顯示ΔΔΔ-1235
print("{:8.0f}".format(1234.56))  # 指定小數位數0位,第1位四捨五入，顯示ΔΔΔΔ1235
print("{:e}".format(123.4))  # 科學記號小數部分6位,小數位數不足補0 顯示1.234000e+02
print("{:10.2e}".format(12345.6))  # 指定總寬度10,小數2位，顯示ΔΔ1.23e+04


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\input01.py

name = input("輸入姓名：")
print("Hi!{}您好!".format(name))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\input02.py

amount = int(input("請輸入需繳費金額:"))
money = int(input("請輸入付款金額:"))

change = temp = money - amount  # change與temp為找零
n500 = change // 500  # change除於500取得500元張數再指定給n500
change = change % 500  # 求500元張數後剩於的找零
n100 = change // 100  # change除於100取得100元張數再指定給n100
change = change % 100  # 求100元張數後剩於的找零
n50 = change // 50  # change除於50取得50元個數再指定給n50
change = change % 50  # 求50元張數後剩於的找零
n10 = change // 10  # change除於10取得10元個數再指定給n10
change = change % 10  # 求10元張數後剩於的找零
n5 = change // 5  # change除於5取得5元個數再指定給n5
change = change % 5  # 求5元張數後剩於的找零
n1 = change // 1  # change除於1取得1元個數再指定給n1
print("收您{}元，找您{}元".format(money, temp))  # 顯示繳費金額與找零金額
print(
    "500元{}張\n100元{}張\n 50元{}個\n 10元{}個\n  5元{}個\n  1元{}個".format(
        n500, n100, n50, n10, n5, n1
    )
)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print01.py

print("HOW", "ARE", "YOU")  # 顯示 "HOW ARE YOU"
greeting = "HOW ARE YOU?"
print(greeting)  # 顯示greeting變數的結果 "HOW ARE YOU?"
print("1+1=", 1 + 1)  # 顯示 1+1 運算式結果 2
print("HOW", "ARE", "YOU", sep="!")  # 顯示"HOW!ARE!YOU"
print("HOW", "ARE", "YOU", end="?")  # 顯示"HOW ARE YOU?"

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print02.py

print("早起的鳥兒'有蟲吃'\n")
print('晚起的鳥兒"被蟲吃"')
print("火影忍者\t博人傳")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print03.py

print("%07d" % 12345)  # 空格補零		ð 0012345
print("%-7d" % 12345)  # 靠左對齊		ð 12345ΔΔ
print("%#o" % 12345)  # 顯示八進制符號	ð 0x30071
print("%#x" % 12345)  # 顯示十六進制符號	ð 0x3039
print("% d" % 12345)  # 保留一個空格		ð Δ12345

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print04.py

print("%d" % (12345))  # 顯示整數資料		ð12345
print("%7d" % (12345))  # 設寬度為7,寬度有剩時補空格	ðΔΔ12345
print("%-7d" % (-12345))  # 靠左對齊,寬度有剩時補空格	ð-12345Δ
print("%07d" % (12345))  # 設寬度為7,寬度有剩時補0	ð0012345
print("%4d" % (-12345))  # 設寬度為3,寬度不足時全部顯示ð-12345
print("%c" % ("Y"))  # 顯示字元「Y」	ð Y
print("%4c" % ("Y"))  # 寬度為4有剩補空格	ðΔΔΔY
print("%c" % (97))  # 97的ASCII碼為a	ð a
print("%s" % ("ABCDE"))  # 顯示字串資料	ð ABCDE
print("%7s" % ("ABCDE"))  # 設寬度為7,寬度有剩時補空格	ðΔΔABCDE
print("%4s" % ("ABCDE"))  # 設寬度為4,寬度不足時全部顯示ð ABCDE
print("%6.3s" % ("ABCDE"))  # 設寬度為6並只顯示3字元	ðΔΔΔABC

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print05.py

print("%f" % 1234.567)  # 小數位數預設6位	ð1234.567000
print("%f" % -123.45)  # 小數位數預設6位	ð-123.450000
print("%.2f" % 12.345)  # 設小數位數2位,第3位四捨五入	ð12.35
print("%8.2f" % -12.3456)  # 設總寬度8位,小數3位		ðΔΔ-12.35
print("%3.1f" % 123.45)  # 設寬度為3且小數1位，寬度不足時全部顯示	ð123.5
print("%8.0f" % -1234.56)  # 設小數位數0位,第1位四捨五入	ðΔΔΔ-1235
print("%8.0f" % 1234.56)  # 設小數位數0位,第1位四捨五入	ðΔΔΔΔ1235
print("%e" % 123.4)  # 科學記號小數部分6位,小數位數不足補0 ð1.234000e+02
print("%10.2e" % 12345.6)  # 設總寬度10,小數2位	ðΔΔ1.23e+04


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch03\print06.py

print("%4s%6s%4s%4s" % ("玩家", "體力", "職業", "技能"))
print("=========================")
print("%3s%8d%4s%4s" % ("王大明", 88, "騎士", "劈砍"))
print("%3s%8d%4s%4s" % ("李小王", 10, "新手", "無"))
print("%3s%8d%4s%4s" % ("林老大", 100, "團長", "斬殺"))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if01.py

score = 89
show = "不及格"  # 預設show字串變數是"不及格"
if score > 60:
    show = "Pass"
print("成績", show)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if02.py

score = 59
if score >= 60:
    show = "Pass"  # score大於等於60，show指定為 "Pass"
else:
    show = "不及格"  # score小於60，show指定為 "不及格"
print("成績", show)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if03.py

uid = input("請輸入帳號：")
pw = input("請輸入密碼：")
if uid == "dtc" and pw == "168":
    show = "帳密正確，歡迎進入系統"
else:
    show = "帳密錯誤，無法使用系統"
print(show)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if04.py

score = int(input("請輸入成績："))  # 輸入成績再轉成整數並指定給score
if score >= 0 and score <= 100:  # 判斷score是否介於0~100之間
    if score >= 60:
        show = "Pass"  # score大於等於60 指定show為 "Pass"
    else:
        show = "不及格"  # score小於60 指定show為 "不及格"
else:
    show = "應介於0~100之間"  # score沒有介於0~100之間 ， show指定為 "應介於0~100之間
print("成績", show)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if05.py

score = int(input("請輸入成績："))  # 輸入成績再轉成整數並指定給score
if score >= 0 and score <= 100:  # 判斷score是否介於0~100之間
    if score >= 90:
        show = "優等"  # score介於100~90時，show指定 "優等"
    elif score >= 80:
        show = "甲等"  # score介於89~80時，show指定 "甲等"
    elif score >= 70:
        show = "乙等"  # score介於79~70時，show指定 "乙等"
    elif score >= 60:
        show = "丙等"  # score介於69~60時，show指定 "丙等"
    else:
        show = "不及格"  # score介於59~0時，show指定 "不及格"
else:
    show = "應介於0~100之間"
print("成績", show)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch04\if06.py

print("==動物英文單字查詢==")
print("1. 獅子")
print("2. 老虎")
print("3. 大象")
print("4. 免子")
num = int(input("請輸入選項編號："))  # 輸入數字轉成整數並指定給num

if num >= 1 and num <= 4:  # 判斷num是否介於1~4之間
    if num == 1:
        show = "獅子：lion"  # num等於1，show指定 "獅子：lion"
    elif num == 2:
        show = "老虎：tiger"  # num等於2，show指定 "老虎：tiger""
    elif num == 3:
        show = "大象：elephant"  # num等於3，show指定 "大象：elephant"
    elif num == 4:
        show = "免子：rabbit"  # num等於4，show指定 "免子：rabbit"
else:
    show = "選項應介於1~4之間"

print(show)  # 顯示show的結果

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\list01.py

name = ["小明", "小華", "小強", "小莉"]
score = [67, 56, 12, 99]
print(name)  # 印出 ['小明', '小華', '小強', '小莉']
print(score)  # 印出 [67, 56, 12, 99]


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\list02.py

name = ["小明", "小華", "小強", "小莉"]
score = [67, 56, 12, 99]
print("{}的成績 {}".format(name[0], score[0]))
print("{}的成績 {}".format(name[1], score[1]))
print("{}的成績 {}".format(name[2], score[2]))
print("{}的成績 {}".format(name[3], score[3]))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\list03.py

name = ["小明", "小華", "小強", "小莉"]
score = [67, 56, 12, 99]
for i in range(4):
    print("{}的成績 {}".format(name[i], score[i]))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\list04.py

listSport = ["爬山", "游泳", "跑步"]
print(listSport[0])  # 顯示"爬山"
print(listSport[-3])  # listSport[-3] 表示串列listSport倒數第3個串列元素，顯示 "爬山"
print(listSport[2])  # listSport[2] 表示串列listSport第3個串列元素，顯示 "跑步"
print(listSport[-1])  # listSport[-1] 表示l串列istSport倒數第1個串列元素，顯示 "跑步"

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\list05.py

listSport = ["爬山", "游泳", "跑步", "舉重", "飛輪", "跳水", "瑜珈"]
print(listSport[1:5])  # [1:5] 表示第2到第5個串列元素，顯示 ['游泳', '跑步', '舉重', '飛輪']
print(listSport[:4])  # [:4] 表示第1到第4個串列元素，顯示['爬山', '游泳', '跑步', '舉重']
print(listSport[1:6:2])  # [1:6:2] 表示第2、4、6個串列元素，顯示['游泳', '舉重', '跳水']
print(listSport[6:1:-2])  # [6:1:-2] 表示第7、5、3個串列元素，顯示['瑜珈', '飛輪', '跑步']
print(listSport[1::2])  # [1::2] 表示第2、4、6個串列元素，顯示['游泳', '舉重', '跳水']

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\listfunc01.py

listScore = [78, 45, 99, 56, 96]
count = len(listScore)
avg = sum(listScore) / count
print("%d 位學生成績：%s" % (count, listScore))
print("最高成績： %d" % max(listScore))
print("最低成績： %d" % min(listScore))
print("加總成績： %d" % sum(listScore))
print("平均成績： %d" % avg)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\listfunc02.py

listScore = []
listScore.append(int(input("第 1 位學生成績：")))
listScore.append(int(input("第 2 位學生成績：")))
listScore.append(int(input("第 3 位學生成績：")))
listScore.append(int(input("第 4 位學生成績：")))

print("成績列表：", listScore)
listScore.sort()
print("遞增排序：", listScore)
listScore.reverse()
print("遞減排序：", listScore)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\product01.py

pid = ["E01", "E02", "E03", "E04"]
name = ["碁峰可樂", "阿才肉乾", "龍哥豆漿", "五香牛肉"]
price = [100, 690, 25, 300]
num = int(input("查詢第幾項產品(1~4)："))
if num >= 1 and num <= 4:
    index = num - 1
    print("編號：%s" % pid[index])
    print("品名：%s" % name[index])
    print("單價：%d" % price[index])
else:
    print("無第 %d 項產品" % num)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\product02.py

product = [
    ["E01", "碁峰可樂", 100],
    ["E02", "阿才肉乾", 690],
    ["E03", "龍哥豆漿", 25],
    ["E04", "五香牛肉", 300],
]
num = int(input("查詢第幾項產品(1~4)："))
if num >= 1 and num <= 4:
    index = num - 1
    print("編號：%s" % product[index][0])
    print("品名：%s" % product[index][1])
    print("單價：%d" % product[index][2])
else:
    print("無第 %d 項產品" % num)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\tlist01.py

member = [
    ["E01", "王小明", "男", 25000],
    ["E02", "曾美麗", "女", 18000],
    ["E03", "莊聰明", "男", 20000],
]
print("會員表共 %d 筆記錄" % len(member))
print("會員表共 %d 個欄位" % len(member[0]))
print(member[0])  # 印出第1筆會員記錄
print(member[1])  # 印出第2筆會員記錄
print(member[2])  # 印出第3筆會員記錄


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\tlist02.py

member = [None, None, None]  # 建立member二維串列，串列中的三個元素為None
member[0] = ["E01", "王小明", "男", 25000]
member[1] = ["E02", "曾美麗", "女", 18000]
member[2] = ["E03", "莊聰明", "男", 20000]
print("會員表共 %d 筆記錄" % len(member))
print("會員表共 %d 個欄位" % len(member[0]))
print(member[0])
print(member[1])
print(member[2])


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch05\tlist03.py

member = [
    ["E01", "王小明", "男", 25000],
    ["E02", "曾美麗", "女", 18000],
    ["E03", "莊聰明", "男", 20000],
]
print("會員表共 %d 筆記錄" % len(member))
print("會員表共 %d 個欄位" % len(member[0]))
print(member[0][0], member[0][1], member[0][2], member[0][3])
print(member[1][0], member[1][1], member[1][2], member[1][3])
print(member[2][0], member[2][1], member[2][2], member[2][3])

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\break01.py

# pid串列存放產品編號
pid = ["A01", "A02", "A03"]
# name串列存放產品名稱
name = ["PS4 特價包", "Switch", "Xbox One"]
# price串列存放產品單價
price = [9980, 12999, 11000]

inputId = input("請輸入欲查詢的產品編號：")

index = -1  # index串列索引為-1表示找不到
count = len(pid)  # len()函式取得name串列個數並指定給count
# count等於3，因此range(count)會產生[0, 1, 2]串列
# for迴圈中的i會逐一被指定為0, 1, 2
for i in range(count):
    if inputId == pid[i]:
        index = i  # 若有找到資料將i指定給index
        break  # 離開迴圈
# 若index等於-1表示找不到資料
if index == -1:
    print("找不到資料")
else:
    print("編號\t品名\t單價")
    print("%s\t%s\t%d" % (pid[index], name[index], price[index]))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\continue01.py

i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print("%d不是3的倍數" % (i))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\createProduct.py

product = []
count = int(input("請輸入產品建檔數量："))

i = 0
while i < count:
    print("第 %d 項產品資訊" % (i + 1))
    temp = []
    temp.append((input("編號：")))
    temp.append((input("品名：")))
    temp.append((input("單價：")))
    product.append(temp)
    i += 1

print("\n產品資訊如下：")
for row in product:  # 印出每列
    for col in row:  # 印出每欄
        print(col, end="\t")
    print()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\for01.py

for i in range(1, 6):
    print(i, end=",")
print()

for i in range(5, 0, -1):
    print(i, end=",")
print()

sum = 0
for i in range(1, 100, 2):
    sum += i
print("1+3+5+...<100=%d" % sum)

program = ["Python", "Java", "C#", "C++"]
for s in program:
    print(s, end=",")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\for02.py

name = [
    "PS4 Slim主機 CUH-2117",
    "任天堂 Nintendo Switch",
    "Xbox One S 500G同捆組",
]  # name串列存放產品名稱
price = [9980, 12999, 11000]  # price串列存放產品單價
# len()函式取得name串列個數並指定給count
count = len(name)
# count等於3，因此range(count)會產生[0, 1, 2]串列
# for迴圈中的i會逐一被指定為0, 1, 2
for i in range(count):
    print("%s \t" % name[i], end="")  # 印出產品
    print("單價%d元" % price[i])  # 印出單價


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\for03.py

listScore = []  # 建立listScore為空串列
count = int(input("請輸入學生數："))  # 指定學生數
# 輸入學生成績並逐一放入listScore串列，append()方法可將資料附加到串列中
for i in range(count):
    print("第 %d 位學生：" % (i + 1), end="")
    listScore.append(int(input("")))

print("成績列表：", listScore)  # 顯示listScore所有元素
listScore.sort()  # 呼叫sort()方法將listScore中的元素進行由小到大非序
print("遞增排序：", listScore)  # 印出listScore由小到大排序的結果
listScore.reverse()  # 呼叫reverse()方法將listScore中的元素進行反轉
print("遞減排序：", listScore)  # 印出listScore由大到小排序的結果


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\forelse01.py

# 執行三次
for i in range(3):
    print("第 %d 次帳密驗證：" % (i + 1), end="")
    uid = input(" 帳號：")  # 將帳號指定給uid
    pw = input(" 密碼：")  # 將密碼指定給pw
    if uid == "dtc" and pw == "168":
        print("帳密正確，歡迎進入系統")
        break
else:
    print()
    print("3 次帳密錯誤，無法使用系統")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\nestLoop01.py

for i in range(1, 10):
    for j in range(1, 10):
        print("%d*%d=%2d" % (i, j, (i * j)), end=";  ")
    print()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\nestLoop02.py

name = ["小明", "小華", "小莉", "小呆"]  # 姓名
score = [[77, 66, 88], [83, 92, 56], [90, 98, 79], [89, 81, 70]]  # 成績
print("姓名   國文   英文   數學   總分")
print("================================")
for i in range(len(name)):
    print("%s" % name[i], end="   ")
    sum = 0
    for j in range(len(score[i])):
        print("%3d" % score[i][j], end="    ")
        sum += score[i][j]
    print("%3d" % sum)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\while01.py

# name串列存放產品名稱
name = ["PS4 Slim主機 CUH-2117", "任天堂 Nintendo Switch", "Xbox One S 500G同捆組"]
# price串列存放產品單價
price = [9980, 12999, 11000]
# len()函式取得name串列個數並指定給count
count = len(name)
# count等於3，range(count)會產生0, 1, 2串列，for迴圈中的i會逐一被指定為0, 1, 2
i = 0  # i起始為0
while i < count:
    print("%s \t" % name[i], end="")  # 印出產品
    print("單價%d元" % price[i])  # 印出單價
    i += 1

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\while02.py

listScore = []  # 建立listScore為空串列
count = int(input("請輸入學生數："))  # 指定學生數
# 輸入學生成績並逐一放入listScore串列，append()方法可將資料附加到串列中
i = 0
while i < count:
    print("第 %d 位學生：" % (i + 1), end="")
    listScore.append(int(input("")))
    i += 1

print("成績列表：", listScore)  # 顯示listScore所有元素
listScore.sort()  # 呼叫sort()方法將listScore中的元素進行由小到大非序
print("遞增排序：", listScore)  # 印出listScore由小到大排序的結果
listScore.reverse()  # 呼叫reverse()方法將listScore中的元素進行反轉
print("遞減排序：", listScore)  # 印出listScore由大到小排序的結果


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch06\whileelse01.py

i = 1  # i起始值為1
# 執行三次
while i <= 3:
    print("第 %d 次帳密驗證：" % i, end="")
    uid = input(" 帳號：")  # 將帳號指定給uid
    pw = input(" 密碼：")  # 將密碼指定給pw
    if uid == "dtc" and pw == "168":
        print("帳密正確，歡迎進入系統")
        break
    i += 1
else:
    print()
    print("3 次帳密錯誤，無法使用系統")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\callReference.py


def CallReference(x):
    for i in range(len(x)):
        x[i] += 10
    print("函式呼叫中：x位址={}, x={}".format(id(x), x))


a = [1, 2, 3, 4]
print("函式呼叫前：a位址={}, a={}".format(id(a), a))
CallReference(a)
print("函式呼叫後：a位址={}, a={}".format(id(a), a))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\callValue.py


def CallValue(x):
    x += 10
    print("函式呼叫中：x位址=%d, x=%d" % (id(x), x))


a = 6
print("函式呼叫前：a位址=%d, a=%d" % (id(a), a))
CallValue(a)
print("函式呼叫後：a位址=%d, a=%d" % (id(a), a))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func01.py


# 定義Hello()函式
def Hello():
    print("Hello!大家好")


Hello()  # 呼叫Hello()函式，結果顯示 “Hello!大家好”


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func02.py


# 定義HelloByName()函式，可接收name參數
def HelloByName(name):
    print("Hello!大家好, 我是", name)


HelloByName("王小明")  # 呼叫Hello()函式並傳入 "王小明" 參數
HelloByName("李小華")  # 呼叫Hello()函式並傳入 "李小華" 參數


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func03.py


# 定義HelloByName()函式，可接收name和gender參數
def HelloByName(name, gender):
    if gender:
        str = "先生"
    else:
        str = "小姐"
    print("Hello!大家好, 我是", name, str)


HelloByName("王小明", True)  # 呼叫Hello()函式並傳入 "王小明" 和 True 參數
HelloByName("李小華", False)  # 呼叫Hello()函式並傳入 "李小華" 和 False 參數


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func04.py


# 定義GetRoundArea函式，可傳入radius半徑，並傳回圓面積
def GetRoundArea(radius):
    # 傳回圓面積，圓面積公式為 半徑 *  半徑 * 3.14
    return radius * radius * 3.14


r = int(input("請輸入半徑："))
RoundArea = GetRoundArea(r)
print("圓形半徑 %d，面積為 %d" % (r, RoundArea))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func05.py


# 定義GetMax()函式，可傳回n1和n2兩數的最大數
def GetMax(n1, n2):
    if n1 > n2:
        vMax = n1
    else:
        vMax = n2
    return vMax


Max = GetMax(70, 9)
print("70和 9最大值為", Max)
print("17和30最大值為", GetMax(17, 30))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\func06.py


# 定義Sort()函式，此函式可將傳入的三個數值進行由小到大排序， 並將排序後的結果傳回
def Sort(x, y, z):
    # 判斷三個數的大小，並做調整
    if x > y:
        t = x
        x = y
        y = t
    if y > z:
        t = y
        y = z
        z = t
    if x > z:
        t = x
        x = z
        z = t
    return x, y, z


# 將輸入的數值1~數值3依序放到a, b, c三個變數
a = int(input("數值1："))
b = int(input("數值2："))
c = int(input("數值3："))
# 呼叫Sort()函式傳入a, b, c三個數，最後將由小到大排序的結果依序指定給a, b, c
a, b, c = Sort(a, b, c)
print("\n由小到大排序：%d %d %d" % (a, b, c))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\funcAry01.py


def GetMax(ary):
    maxNum = ary[0]
    index = 0
    for i in range(len(ary)):
        if maxNum < ary[i]:
            index = i
            maxNum = ary[index]
    return index


listName = ["阿才肉乾", "恐龍餅乾", "快樂汽水", "天天豆干"]
listPrice = [70, 230, 400, 240]

for i in range(len(listName)):
    print("%s %d" % (listName[i], listPrice[i]))
print()
n = GetMax(listPrice)
print("最貴產品：%s, 單價：%d" % (listName[n], listPrice[n]))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\random01.py

import random

for i in range(5):
    print("第 %d 個亂數：%d" % (i + 1, random.randint(1, 10)))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\random02.py

import random  # 引用random亂數套件

#  將 1~49 的整數放入num串列中
num = []
for i in range(49):
    num.append(i + 1)
# 使用 random套件的sample函式由num中隨機取得不重複的7個元素
lot = random.sample(num, 7)

print("大樂透  號碼：", end="")
# 印出 lot[0]~lot[5]
for i in range(6):
    print(lot[i], end=", ")

print()
print("大樂透特別號：%2d" % (lot[6]))  # 印出 lot[6]


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\var01.py


def func():
    n = 10
    print("區域變數n 位址=%d, 值=%d" % (id(n), n))


n = 100
func()
print("全域變數n 位址=%d, 值=%d" % (id(n), n))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch07\var02.py


def func():
    global n
    n = 10
    print("函式內 全域變數n 位址=%d, 值=%d" % (id(n), n))


n = 100
print("函式外 全域變數n 位址=%d, 值=%d" % (id(n), n))
func()
print("函式外 全域變數n 位址=%d, 值=%d" % (id(n), n))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch08\dict01.py

dictBook = {"A001": ["木偶奇遇記", 199], "A002": ["三隻小豬", 120], "A003": ["白雪公主", 99]}
print(dictBook)
# 印出 dictBook所有元素
print("書號A001：", dictBook["A001"])  # 印出dictBook字典鍵A001的值 ['木偶奇遇記', 199]
print("書號A002：", dictBook["A002"])  # 印出dictBook字典鍵A002的值 ['三隻小豬', 120]
print("書號A003：", dictBook["A003"])  # 印出dictBook字典鍵A003的值 ['白雪公主', 99]


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch08\dict02.py

tupleBookId = ("A001", "A002", "A003")
dictBook = {"A001": ["木偶奇遇記", 199], "A002": ["三隻小豬", 120], "A003": ["白雪公主", 99]}
print("書號\t書名\t單價")
print("========================")

for key in list(tupleBookId):
    print(key, end="\t")
    for col in dictBook[key]:
        print(col, end="\t")
    print()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch08\dict03.py

dictBook = {"A001": ["木偶奇遇記", 199]}
print("編輯前字典內容：", dictBook)

dictBook["A002"] = ["三隻小豬", 120]
print("新增後字典內容：", dictBook)

dictBook["A002"] = ["白雪公主", 120]
print("修改後字典內容：", dictBook)

print("是否有書號A001的書籍：", "A001" in dictBook)

del dictBook["A001"]
print("刪除後字典內容：", dictBook)

print("是否有書號A001的書籍：", "A001" in dictBook)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch08\dictGame.py

import random

bossHp = 100
listPcCard = [["青眼白龍", 20], ["紅髮女妖", 11], ["白骷髏王", 9], ["碧眼狐怪", 12]]
random.shuffle(listPcCard)
dictMyCard = dict(listPcCard)

while True:
    n = int(input("功能選項：1.抽卡攻擊 2.補齊卡牌 3.目前卡牌 4.離開遊戲："))
    if n == 1:
        if not dictMyCard:
            print("目前沒有卡牌，請補卡牌")
            continue
        card = dictMyCard.popitem()
        listCard = list(card)
        cardName = listCard[0]
        cardAttack = listCard[1]
        bossHp -= cardAttack
        if bossHp <= 0:
            bossHp = 0
            print("%s最後一擊 %d 點\t魔王血量歸 %d，成功過關" % (cardName, cardAttack, bossHp))
            break
        print("使用%s攻擊 %d 點\t魔王目前血量：%d" % (cardName, cardAttack, bossHp))
    elif n == 2:
        random.shuffle(listPcCard)
        dictMyCard = dict(listPcCard)
        print("完成補齊卡牌!")
    elif n == 3:
        print("目前卡牌：", dictMyCard)
    elif n == 4:
        break
    else:
        print("無此選項功能!")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch08\ProductSys.py


# 新增
def fnCreate():
    uid = input("編號：")
    if uid in dictProduct:
        print("編號重複，無法新增產品記錄")
        return
    name = input("品名：")
    price = int(input("單價："))
    newProduct = {uid: [name, price]}
    dictProduct.update(newProduct)
    print("產品新增成功!")


# 修改
def fnUpdate():
    uid = input("編號：")
    if uid not in dictProduct:
        print("無此編號，無法修改產品記錄")
        return
    name = input("品名：")
    price = int(input("單價："))
    dictProduct[uid] = [name, price]
    print(dictProduct)
    print("產品修改成功!")


# 刪除
def fnDelete():
    uid = input("編號：")
    if uid not in dictProduct:
        print("無此編號，無法刪除產品記錄")
        return
    dictProduct.pop(uid)
    print("產品刪除成功!")


# 依編號查詢產品
def fnGetProductById():
    uid = input("編號：")
    if uid not in dictProduct:
        print("查無此編號")
        return
    print("編號\t品名\t單價")
    print("%s\t%s\t%d" % (uid, dictProduct[uid][0], dictProduct[uid][1]))


# 將所有產品列出
def fnGetProductList():
    print("編號\t品名\t單價")
    listKey = dictProduct.keys()
    for uid in listKey:
        print("%s\t%s\t%d" % (uid, dictProduct[uid][0], dictProduct[uid][1]))


# 主程式
dictProduct = {}
print("======= DTC產品管理系統 =======")
while True:
    option = int(input("系統功能->1.新增 2.修改 3.刪除 4.查詢 5.產品列表 其他.離開："))
    if option == 1:
        fnCreate()
    elif option == 2:
        fnUpdate()
    elif option == 3:
        fnDelete()
    elif option == 4:
        fnGetProductById()
    elif option == 5:
        fnGetProductList()
    else:
        print("離開系統")
        break

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch08\tuple01.py

tupleFruit = ("apple", "banana", "cherry")  # 建立tupleFruit元組用來存放水果英文名稱
tupleNum = (1, 2, 3, 4, 5)  # 建立tupleNum元組用來存放1~5整數
tupleBool = (True, False)  # 建立tupleBool元組用來存放布林值True|False
tupleProduct = ("P01", "五香豆干", 45)  # 建立tupleProduct元組用來存放產品資訊
print(tupleFruit)  # 顯示 ('apple', 'banana', 'cherry')
print(tupleNum)  # 顯示 (1, 2, 3, 4, 5)
print(tupleBool)  # 顯示 (True, False)
print(tupleProduct)  # 顯示 ('P01', '五香豆干', 45)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\跟著阿才學Python從基礎到網路爬蟲應用\ch08\tuple02.py

tupleScore = (89, 87, 36, 55, 94)
tupleName = ("小明", "小華", "小強", "小保", "小呆")
print("****DTC大學-學生績表****")
print("姓名\t分數")
print("=======================")
for i in range(len(tupleScore)):
    print("%s\t%d" % (tupleName[i], tupleScore[i]))
print("=======================")
print("  最高分：%d" % max(tupleScore))
print("  最低分：%d" % min(tupleScore))
print("平均分數：%.2f" % (sum(tupleScore) / len(tupleScore)))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
