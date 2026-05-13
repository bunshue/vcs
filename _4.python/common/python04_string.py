import sys

"""
各種 python 字串 專用的語法

各種格式化列印

"""
'''
print("------------------------------------------------------------")  # 60個

"""
字串的函數
just center replace find
"""

str1 = "dog"
print(str1.ljust(7))
print(str1.ljust(7, "#"))

print("------------------------------------------------------------")  # 60個

str1 = "dog"
print(str1.rjust(7, "#"))

print("------------------------------------------------------------")  # 60個

str1 = "dog"
print(str1.center(7, "#"))

print("------------------------------------------------------------")  # 60個

str1 = "  This is a dog.  "
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())

print("------------------------------------------------------------")  # 60個

print("測試find")

str1 = "I like Python."
print(str1.find("like"))
print(str1.find("Pascal"))
print("------------------------------------------------------------")  # 60個

str1 = "I like Python."
print(str1.replace("Python", "Pascal"))

print("------------------------------------------------------------")  # 60個

str1 = "dog"
print(str1.ljust(7))
print(str1.ljust(7, "#"))

print("------------------------------------------------------------")  # 60個

str1 = "dog"
print(str1.rjust(7, "#"))

print("------------------------------------------------------------")  # 60個

str1 = "dog"
print(str1.center(7, "#"))

print("------------------------------------------------------------")  # 60個

str1 = "  This is a dog.  "
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())

print("------------------------------------------------------------")  # 60個

# join() 連接字串

animals = ["鼠", "牛", "虎", "兔"]

print("---".join(animals))

# split() 分割字串
animals = "米老鼠 班尼牛 跳跳虎 彼得兔 逗逗龍"
cc = animals.split()
print(cc)

# 字串排版

# ljust rjust
text = "米老鼠"
print("|" + text + "|")
print("|" + text.ljust(10) + "|")
print("|" + text.ljust(10, "#") + "|")
print("|" + text.rjust(10) + "|")
print("|" + text.rjust(10, "#") + "|")
# center(n) : 將字串擴充n個字元並置中
print("|" + text.center(10) + "|")

print("------------------------------------------------------------")  # 60個

title = "Ming-Chi Institute of Technology"
print(f"/{title.center(50)}/")
dt = "Department of ME"
print(f"/{dt.ljust(50)}/")
site = "JK Hung"
print(f"/{site.rjust(50)}/")
print(f"/{title.zfill(50)}/")

print("------------------------------------------------------------")  # 60個

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4))
print("x= ", str(x2).rjust(4))
print("x= ", str(x3).rjust(4))
print("x= ", str(x4).rjust(4))

print("------------------------------------------------------------")  # 60個

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4), end="\r", flush=True)
print("x= ", str(x2).rjust(4), end="\r", flush=True)
print("x= ", str(x3).rjust(4), end="\r", flush=True)
print("x= ", str(x4).rjust(4), end="\r", flush=True)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

str1 = "Python is funny and powerful"
print("原字串", str1)
print("欄寬40，字串置中", str1.center(40))
print("字串置中，* 填補", str1.center(40, "*"))
print("欄寬10，字串靠左", str1.ljust(40, "="))
print("欄寬40，字串靠右", str1.rjust(40, "#"))

mobilephone = "931666888"
print("字串左側補0:", mobilephone.zfill(10))

str2 = "Mayor,President"
print("以逗點分割字元", str2.partition(","))

str3 = "禮\n義\n廉\n恥"
print("依\\n分割字串", str3.splitlines(False))

print("------------------------------------------------------------")  # 60個

str1 = "Happy birthday to my best friend."
s1 = str1.count("to", 0)  # 從str1字串索引0的位置開始搜尋
s2 = str1.count("e", 0, 34)  # 搜尋str1從索引值0到索引值34-1的位置
print("{}\n「to」出現{}次,「e」出現{}次".format(str1, s1, s2))

print("------------------------------------------------------------")  # 60個


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

str1 = "Python is funny and powerful"
print("原字串", str1)
print("欄寬40，字串置中", str1.center(40))
print("字串置中，* 填補", str1.center(40, "*"))
print("欄寬10，字串靠左", str1.ljust(40, "="))
print("欄寬40，字串靠右", str1.rjust(40, "#"))

mobilephone = "931666888"
print("字串左側補0:", mobilephone.zfill(10))

str2 = "Mayor,President"
print("以逗點分割字元", str2.partition(","))

str3 = "禮\n義\n廉\n恥"
print("依\\n分割字串", str3.splitlines(False))

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

animals = "welcome to python"
print("animals = ", animals)
b = animals.endswith("thon")
print("animals.endswith('thon') = ", b)
b = animals.startswith("hello")
print("animals.startswith('hello') = ", b)
b = animals.count("o")
print("animals.count('o') = ", b)
b = animals.find("come")
print("animals.find('come') = ", b)
b = animals.find("become")
print("animals.find('become') = ", b)
b = animals.find("o")
print("animals.find('o') = ", b)
b = animals.find("e")
print("animals.find('e') = ", b)
b = animals.rfind("o")
print("animals.rfind('o') = ", b)
b = animals.rfind("e")
print("animals.rfind('e') = ", b)

print("------------------------------------------------------------")  # 60個

animals = "welcome to python"
print("animals = ", animals)
animals = "Welcome to Python"
print("animals = ", animals)
str3 = "This is a test."
print("str3 = ", str3)
s = animals.capitalize()
print("animals.capitalize() = ", s)
s = animals.lower()
print("animals.lower() = ", s)
s = animals.upper()
print("animals.upper() = ", s)
s = animals.title()
print("animals.title() = ", s)
s = animals.swapcase()
print("animals.swapcase() = ", s)
s = str3.replace("is", "was")
print("str3.replace('is', 'was') = ", s)

print("------------------------------------------------------------")  # 60個

title = "9 * 9 Multiplication Table"
print("%s" % title.center(40))
for i in range(1, 10):
    print(f"{i:4d}", end="")
print()  # 跳列輸出
for i in range(40):
    print("=", end="")  # 列印分隔符號
print()  # 跳列輸出
for i in range(1, 10):
    print(i, "|", end="")
    for j in range(1, 10):
        print(f"{i*j:4d}", end="")  # 列印乘法值
    print()  # 跳列輸出
'''
print("------------------------------------------------------------")  # 60個

str = "{1} * {0} = {2}"
a = 3
b = "5"
print(str.format(a, b, a * int(b)))

print("------------------------------------------------------------")  # 60個

year = 2024
month = 1
day = 20
print("日期：%s-%s-%s" % (year, month, day))

print("------------------------------------------------------------")  # 60個

print("{0:10}收入：{1:_^12}".format("Axel", 52000))
print("{0:10}收入：{1:>12}".format("Michael", 87000))
print("{0:10}收入：{1:*<12}".format("May", 36000))

print("------------------------------------------------------------")  # 60個

num = 168
print("數字 %s 的浮點數：%5.1f" % (num, num))

print("------------------------------------------------------------")  # 60個

print("編號 姓名    底薪  業務獎金 加給補貼")
print("%3d %3s %6d %6d %6d" % (801, "朱正富", 32000, 10000, 5000))
print("%3d %3s %6d %6d %6d" % (805, "曾自強", 35000, 8000, 7000))
print("%3d %3s %6d %6d %6d" % (811, "陳威動", 43000, 15000, 6000))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%06.2f\n" % (1.2345))
print("不足數位預設空格：%6.2f\n" % (1.2345))
print("小數點保留2位：%.2f\n" % (1.2345))
print("不足數位補0(以*替代)：%0*.2f\n" % (6, 1.2345))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%05d\n" % (66))
print("不足數位預設空格：%5d\n" % (66))
print("小於位數則輸出全部：%2d\n" % (666))
print("不足數位補0(以*替代)：%0*d\n" % (5, 66))

print("------------------------------------------------------------")  # 60個

str1 = "Hello!\nPython"
print("不含r字元的輸出")
print(str1)
str2 = r"Hello!\nPython"
print("含r字元的輸出 忠實保留雙引號內的資料內容")
print(str2)

print("------------------------------------------------------------")  # 60個

x = 47.5
print("以下輸出round(x)函數的應用")
print("x = ", x)  # 輸出x變數
print("round(47.5) = ", round(x))  # 輸出round(x)

x = 48.5
print("x = ", x)  # 輸出x變數
print("round(48.5) = ", round(x))  # 輸出round(x)

x = 49.5
print("x = ", x)  # 輸出x變數
print("round(49.5) = ", round(x))  # 輸出round(x)
print("以下輸出round(x,n)函數的應用")

x = 2.15
print("x = ", x)  # 輸出x變數
print("round(2.15,1) = ", round(x, 1))  # 輸出round(x,1)

x = 2.25
print("x = ", x)  # 輸出x變數
print("round(2.25,1) = ", round(x, 1))  # 輸出round(x,1)

x = 2.151
print("x = ", x)  # 輸出x變數
print("round(2.151,1) = ", round(x, 1))  # 輸出round(x,1)

x = 2.251
print("x = ", x)  # 輸出x變數
print("round(2.251,1) = ", round(x, 1))  # 輸出round(x,1)

print("------------------------------------------------------------")  # 60個

x = 12345678
print("/%10.1e/" % x)
print("/%10.2E/" % x)
print("/%-10.2E/" % x)
print("/%+10.2E/" % x)
print("=" * 60)
string = "abcdefg"
print("/%10.3s/" % string)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x = 100
print("x=/%6d/" % x)
y = 10.5
print("y=/%6.2f/" % y)
s = "Deep"
print("s=/%6s/" % s)
print("以下是保留格數空間不足的實例")
print("x=/%2d/" % x)
print("y=/%3.2f/" % y)
print("s=/%2s/" % s)


print("------------------------------------------------------------")  # 60個

x = 100
print("x=/%-8d/" % x)
y = 10.5
print("y=/%-8.2f/" % y)
s = "Deep"
print("s=/%-8s/" % s)

print("------------------------------------------------------------")  # 60個

x = 10
print("x=/%+8d/" % x)
y = 10.5
print("y=/%+8.2f/" % y)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
