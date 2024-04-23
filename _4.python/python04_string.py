import sys

"""
各種 python 字串 專用的語法


"""

print("------------------------------------------------------------")  # 60個


"""
字串的函數
just center replace find
"""

str1 = "dog"
print(str1.ljust(7))
print(str1.ljust(7,"#"))

print("------------------------------------------------------------")  # 60個

str1 = "dog"
print(str1.rjust(7,"#"))

print("------------------------------------------------------------")  # 60個

str1 = "dog"
print(str1.center(7,"#"))

print("------------------------------------------------------------")  # 60個

str1 = "  This is a dog.  "
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())

print("------------------------------------------------------------")  # 60個

print('測試find')

str1 = "I like Python."
print(str1.find("like"))
print(str1.find("Pascal"))
print("------------------------------------------------------------")  # 60個

str1 = "I like Python."
print(str1.replace("Python","Pascal"))

print("------------------------------------------------------------")  # 60個

str1 = "dog"
print(str1.ljust(7))
print(str1.ljust(7,"#"))

print("------------------------------------------------------------")  # 60個

str1 = "dog"
print(str1.rjust(7,"#"))

print("------------------------------------------------------------")  # 60個

str1 = "dog"
print(str1.center(7,"#"))

print("------------------------------------------------------------")  # 60個

str1 = "  This is a dog.  "
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())

print("------------------------------------------------------------")  # 60個


#join() 連接字串

animals = ["鼠", "牛", "虎", "兔"]

print("---".join(animals))

#split() 分割字串
animals = "米老鼠 班尼牛 跳跳虎 彼得兔 逗逗龍"
cc = animals.split()
print(cc)

#字串排版

#ljust rjust
text = "米老鼠"
print("|"+text+"|")
print("|"+text.ljust(10)+"|")
print("|"+text.ljust(10, '#')+"|")
print("|"+text.rjust(10)+"|")
print("|"+text.rjust(10, '#')+"|")
#center(n) : 將字串擴充n個字元並置中
print("|"+text.center(10)+"|")

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



