
print("------------------------------------------------------------")  # 60個

a = True
b = False
print(type(a)) # 顯示 "<class 'bool'>"
print(a and b) # 邏輯AND: 顯示 "False"
print(a or b)  # 邏輯OR: 顯示"True"
print(not a)   # 邏輯NOT: 顯示 "False"

print("------------------------------------------------------------")  # 60個

s = "hello"
print(s.capitalize())  # 第1個字元大寫: 顯示 "Hello"
print(s.upper())       # 轉成大寫: 顯示 "HELLO"
print(s.rjust(7))      # 右邊填空白字元: 顯示 "  hello"
print(s.center(7))     # 置中顯示: 顯示 " hello "
print(s.replace('l', 'L'))  # 取代字串: 顯示 "heLLo"
print('  python '.strip())  # 刪除空白字元: 顯示 "python"

print("------------------------------------------------------------")  # 60個

# 擁有1個參數的range()函數
for i in range(5):
    print("range(5)的值 = " + str(i))
for i in range(10):
    print("range(10)的值 = " + str(i))
for i in range(11):
    print("range(11)的值 = " + str(i))
# 擁有2個參數的range()函數
for i in range(1, 5):
    print("range(1,5)的值 = " + str(i))
for i in range(1, 10):
    print("range(1,10)的值 = " + str(i))
for i in range(1, 11):
    print("range(1,11)的值 = " + str(i))
# 擁有3個參數的range()函數
for i in range(1, 11, 2):
    print("range(1,11,2)的值 = " + str(i))
for i in range(1, 11, 3):
    print("range(1,11,3)的值 = " + str(i))
for i in range(1, 11, 4):
    print("range(1,11,4)的值 = " + str(i))
for i in range(0, -10, -1):
    print("range(0,-10,-1)的值 = " + str(i))
for i in range(0, -10, -2):
    print("range(0,-10,-2)的值 = " + str(i))
    
print("------------------------------------------------------------")  # 60個

# 定義函數
def print_msg():
    print("歡迎學習Python程式設計!")

def is_valid_num(no):
    if no >= 0 and no <= 200.0:
        return True
    else:
        return False

def convert_to_f(c):
    f = (9.0 * c) / 5.0 + 32.0
    return f
# 函數呼叫
print_msg()
c = 100
f = convert_to_f(c)
print("華氏: " + str(f))
if is_valid_num(c):
    print("合法!")
else:
    print("不合法")

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)

print("------------------------------------------------------------")  # 60個

try: 
    fp = open("myfile.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("錯誤: myfile.txt檔案不存在!")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-1.py

ls = [6, 4, 5]    # 建立清單
print(ls, ls[2])  # 顯示 "[6, 4, 5] 5"
print(ls[-1])     # 負索引從最後開始: 顯示 "5"
ls[2] = "py"      # 指定字串型態的項目
print(ls)         # 顯示 "[6, 4, 'py']"
ls.append("bar")  # 新增項目
print(ls)         # 顯示 "[6, 4, 'py', 'bar']"
ele = ls.pop()    # 取出最後項目
print(ele, ls)    # 顯示 "bar [6, 4, 'py']"



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-1a.py

nums = list(range(5))  # 建立一序列的整數清單
print(nums)            # 顯示 "[0, 1, 2, 3, 4]"
print(nums[2:4])       # 切割索引2~4(不含4): 顯示 "[2, 3]"
print(nums[2:])        # 切割索引從2至最後: 顯示 "[2, 3, 4]"
print(nums[:2])        # 切割從開始至索引2(不含2): 顯示 "[0, 1]"
print(nums[:])         # 切割整個清單: 顯示 "[0, 1, 2, 3, 4]"
print(nums[:-1])       # 使用負索引切割: 顯示 "[0, 1, 2, 3]"
nums[2:4] = [7, 8]     # 使用切割來指定子清單
print(nums)            # 顯示 "[0, 1, 8, 9, 4]"



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-1b.py

print("走訪顯示串列的每一個項目...")
animals = ['cat', 'dog', 'bat']
for animal in animals:
    print(animal)

print("走訪顯示串列的每一個項目和索引值...")
animals = ['cat', 'dog', 'bat']
for index, animal in enumerate(animals):
    print(index, animal)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-1c.py

list1 = [x for x in range(10)]
print("[x for x in range(10)]")
print(str(list1))
list2 = [x+1 for x in range(10)]
print("[x+1 for x in range(10)]")
print(str(list2))
list3 = [x for x in range(10) if x % 2 == 0]
print("[x for x in range(10) if x%2==0]")
print(str(list3))
list4 = [x*2 for x in range(10) if x % 2 == 0]
print("[x*2 for x in range(10) if x%2==0]")
print(str(list4))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-2.py

d = {"cat": "white", "dog": "black"}  # 建立字典
print(d["cat"])       # 使用Key取得項目: 顯示 "white"
print("cat" in d)     # 是否有Key: 顯示 "True"
d["pig"] = "pink"     # 新增項目
print(d["pig"])       # 顯示 "pink"
print(d.get("monkey", "N/A"))  # 取出項目+預設值: 顯示 "N/A"
print(d.get("pig", "N/A"))     # 取出項目+預設值: 顯示 "pink"
del d["pig"]          # 使用Key刪除項目
print(d.get("pig", "N/A"))     # "pig"不存在: 顯示 "N/A"


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-2a.py

print("以鍵來走訪字典...")
d = {"chicken": 2, "dog": 4, "cat": 4, "spider": 8}
for animal in d:
    legs = d[animal]
    print(animal, legs)
print("走訪字典的鍵和值...")
d = {"chicken": 2, "dog": 4, "cat": 4, "spider": 8}
for animal, legs in d.items():
    print("動物: %s 有 %d 隻腳" % (animal, legs))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-2b.py

d1 = {x:x*x for x in range(10)}
print("{x:x*x for x in range(10)}")
print(str(d1))
d2 = {x:x*x for x in range(10) if x % 2 == 1}
print("{x:x*x for x in range(11) if x%2==1}")
print(str(d2))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-3.py

animals = {"cat", "dog", "pig"} # 建立集合
print("cat" in animals)   # 檢查是否有此元素: 顯示 "True"
print("fish" in animals)  # 顯示 "False"
animals.add("fish")       # 新增集合元素
print("fish" in animals)  # 顯示 "True"
print(len(animals))       # 元素數: 顯示 "4"
animals.add("cat")        # 新增存在的元素
print(len(animals))       # 顯示 "4"
animals.remove('cat')     # 刪除集合元素
print(len(animals))       # 顯示 "3"



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-3a.py

animals = {"cat", "dog", "pig", "fish"} # 建立集合
for index, animal in enumerate(animals):
    print('#%d: %s' % (index + 1, animal))




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-3b.py

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("A = " + str(A))
print("B = " + str(B))
# 交集
C = A & B
print("A & B = " + str(C))
C = A.intersection(B)
print("A.intersection(B) = " + str(C))
# 聯集
C = A | B
print("A | B = " + str(C))
C = A.union(B)
print("A.union(B) = " + str(C))
# 差集
C = A - B
print("A - B = " + str(C))
C = A.difference(B)
print("A.difference(B) = " + str(C))
# 對稱差集
C = A ^ B
print("A ^ B = " + str(C))
C = A.symmetric_difference(B)
print("A.symmetric_difference(B) = " + str(C))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-4.py

t = (5, 6, 7, 8)  # 建立元組
print(type(t))    # 顯示 "<class 'tuple'>"
print(t)          # 顯示 "(5, 6, 7, 8)"
print(t[0])       # 顯示 "5"
print(t[1])       # 顯示 "6"
print(t[-1])      # 顯示 "8"
print(t[-2])      # 顯示 "7"
for ele in t:     # 走訪項目
    print(ele, end=" ")  # 顯示 "5, 6, 7, 8"



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-6-1.py

# 定義Student類別
class Student:
    # 建構子
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    # 方法
    def displayStudent(self):
        print("姓名 = " + self.name)
        print("成績 = " + str(self.grade))
        
    def whoami(self):
        return self.name

# 使用類別建立物件
s1 = Student("陳會安", 85)
s1.displayStudent()  # 呼叫方法
print("s1.whoami() = " + s1.whoami())
# 存取資料欄位
print("s1.name = " + s1.name)
print("s1.grade = " + str(s1.grade))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-6-2.py

# 定義Student類別
class Student:
    # 建構子
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade
    # 方法
    def displayStudent(self):
        print("姓名 = " + self.name)
        print("成績 = " + str(self.__getGrade()))
        
    def __getGrade(self):
        return self.__grade

# 使用類別建立物件
s1 = Student("陳會安", 85)
s1.displayStudent()  # 呼叫方法
# print("s1.__getGrade() = " + str(s1.__getGrade()))
# 存取資料欄位
print("s1.name = " + s1.name)
# print(s1.__grade)

print("------------------------------------------------------------")  # 60個


