import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個


c = 1 + 3j
print("c的資料型態：", type(c))
print("c是否為複數？", isinstance(1 + 3j, complex))


print("------------------------------------------------------------")  # 60個


sigma = 0
k = int(input("請輸入k值："))  # 輸入k值
for n in range(0, k, 1):
    if n & 1:  # 如果n是奇數
        sigma += float(-1 / (2 * n + 1))
    else:  # 如果n是偶數
        sigma += float(1 / (2 * n + 1))
print("PI = %f" % (sigma * 4))

print("------------------------------------------------------------")  # 60個

# 九九乘法表的雙重迴圈
for i in range(1, 10):
    for j in range(1, 10):
        print("{0}*{1}={2:2d}  ".format(i, j, i * j), sep="\t", end="")
        if j >= 7:
            break  # 設定跳出的條件
    print("\n-------------------------------------------------------\n")


print("------------------------------------------------------------")  # 60個
info = [
    ["C程式設計", "朱大峰", "480"],
    ["Python程式設計", "吳志明", "500"],
    ["Java程式設計", "許伯如", "540"],
]

for book, author, price in info:
    print("%10s %3s" % (book, author), " 書籍訂價:", price)


print("------------------------------------------------------------")  # 60個

word = [
    "holiday",
    "happy",
    "birth",
    "yesterday",
    "holiday",
    "car",
    "yellow",
    "happy",
    "mobile",
    "cup",
    "happy",
    "holiday",
    "holiday",
    "desk",
    "birth",
]
print("holiday 出現的次數", word.count("holiday"))


print("------------------------------------------------------------")  # 60個

str1 = "do your best what you can do"
s1 = str1.count("do", 0)
s2 = str1.count("o", 0, 20)
print("{}\n「do」出現{}次,「o」出現{}次".format(str1, s1, s2))


print("------------------------------------------------------------")  # 60個

str1 = "設定中文字型及負號正確顯示"
print("原字串內容: ", str1)
print("轉換成串列: ", list(str1))
print("轉換成值組: ", tuple(str1))
print("字串長度: ", len(str1))

list1 = list(str1)
print("原串列內容: ", list1)
print("串列中最大值: ", max(list1))
print("串列中最小值: ", min(list1))

relist = reversed(list1)  # 反轉串列
for i in relist:  # 將反轉後的串列內容依序印出
    print(i, end=" ")
print()  # 換行
print("串列元素由小到大排序: ", sorted(list1))


print("------------------------------------------------------------")  # 60個


result = lambda x: 3 * x - 1  # lambda()函數
print(result(3))  # 輸出數值8

print("------------------------------------------------------------")  # 60個


def formula(x, y):  # 自訂函數
    return 3 * x + 2 * y


formula = lambda x, y: 3 * x + 2 * y  # 表示lambda有二個參數
print(formula(5, 10))  ##傳入兩個數值讓lambda()函數做運算，輸出數值35


print("------------------------------------------------------------")  # 60個

str1 = "淡泊以明志，寧靜以致遠"
print("原字串", str1)
print("欄寬20，字串置中", str1.center(20))
print("字串置中，# 填補", str1.center(20, "#"))
print("欄寬20，字串靠左", str1.ljust(20, "@"))
print("欄寬20，字串靠右", str1.rjust(20, "!"))

mobilephone = "931828736"
print("字串左側補0:", mobilephone.zfill(10))

str2 = "Time create hero.,I love my family."
print("以逗點分割字元", str2.partition(","))

str3 = "忠孝\n仁愛\n信義\n和平"
print("依\\n分割字串", str3.splitlines(False))


print("------------------------------------------------------------")  # 60個
math.sqrt(sum(pow(x - (sum(data) / len(data)), 2) for x in data) / len(data))

mean = sum(data) / len(data)
variance = sum(pow(x - mean, 2) for x in data) / len(data)
std = math.sqrt(variance)


print("------------------------------------------------------------")  # 60個

print("a", "b", "c", sep="|")

print("a", "b", "c", end="\n\n")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
