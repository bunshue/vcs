print("------------------------------------------------------------")  # 60個


# 函數: 計算2個參數和
def sum(a, b):
    return a + b


# 建立匿名函數
square = lambda x: x * x

# 將變數指定成函數
total = sum
r = square(10)  # 呼叫匿名函數
print("square(10) = ", r)

r = sum(10, 5)  # 呼叫函數
print("sum(10, 5) = ", r)

r = total(10, 5)  # 使用變數呼叫函數
print("total(10, 5) = ", r)

print("------------------------------------------------------------")  # 60個

# 定義lambda函數
square = lambda x: x**2

# 輸出平方值
print(square(10))

print("------------------------------------------------------------")  # 60個

# lambda : 只有單一運算式的匿名函式
add = lambda x, y: x + y  # 冒號前是參數, 冒號後是運算式
cc = add(3, 5)
print("使用 lambda 做加法:", cc)

print("------------------------------------------------------------")  # 60個

from functools import reduce


def strToInt(s):
    def charToNum(s):
        return {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }[s]

    return reduce(lambda x, y: 10 * x + y, map(charToNum, s))


string = "5487"
x = strToInt(string) + 10
print("x = ", x)

print("------------------------------------------------------------")  # 60個

str_len = lambda x: len(x)
strs = ["abc", "ab", "abcde"]
strs.sort(key=str_len)
print(strs)

print("------------------------------------------------------------")  # 60個

strs = ["abc", "ab", "abcde"]
strs.sort(key=lambda x: len(x))
print(strs)

print("------------------------------------------------------------")  # 60個

sc = [["John", 80], ["Tom", 90], ["Kevin", 77]]
sc.sort(key=lambda x: x[1])
print(sc)

print("------------------------------------------------------------")  # 60個

sc = [["John", 80], ["Tom", 90], ["Kevin", 77]]
newsc = sorted(sc, key=lambda x: x[1])
print(newsc)

print("------------------------------------------------------------")  # 60個

sc = {"John": 80, "Tom": 90, "Kevin": 77}
newsc1 = sorted(sc.items(), key=lambda x: x[0])  # 依照key排序
print("依照人名排序")
print(newsc1)

newsc2 = sorted(sc.items(), key=lambda x: x[1])  # 依照value排序
print("依照分數排序")
print(newsc2)

print("------------------------------------------------------------")  # 60個

mylist = [5, 10, 15, 20, 25, 30]

evenlist = list(filter(lambda x: (x % 2 == 0), mylist))

# 輸出偶數串列
print("偶數串列: ", evenlist)

print("------------------------------------------------------------")  # 60個

result = lambda x: 3 * x - 1  # lambda()函數
print(result(3))  # 輸出數值8

print("------------------------------------------------------------")  # 60個


def formula(x, y):  # 自訂函數
    return 3 * x + 2 * y


formula = lambda x, y: 3 * x + 2 * y  # 表示lambda有二個參數
print(formula(5, 10))  ##傳入兩個數值讓lambda()函數做運算，輸出數值35

print("------------------------------------------------------------")  # 60個

# lambda 函式簡介

power = lambda x: x**2
print(power(10))

add = lambda a, b: a + b
print(add(5, 3))

print("------------------------------------------------------------")  # 60個

# 定義lambda函數
square2 = lambda x: x**2

# 輸出平方值
print(square2(10))

print("------------------------------------------------------------")  # 60個

total = lambda a, b: a + b
num1 = 0
num2 = 0
num1 = 123
num2 = 456
print("數值 1+數值 2 =", total(num1, num2))

# 在 lambda 內使用一行 if 條件判斷式

absolute = lambda x: x if x >= 0 else -x

func = lambda x: (x**2 - 40 * x + 350) if 10 <= x < 30 else 50

# str.split()：分割字串為 list 元素

sentence = "This is a test sentence"

print(sentence.split(" "))

["This", "is", "a", "test", "sentence"]

print("------------------------------------------------------------")  # 60個

# 用 flter() 篩選容器元素

str_list = ["This", "is", "a", "test", "sentence"]

print(list(filter(lambda x: len(x) >= 3, str_list)))

["This", "test", "sentence"]

# 再探 sorted()：自訂目標容器的排序方式

str_list = ["This", "is", "a", "test", "sentence"]

print(sorted(str_list, key=len, reverse=True))

nest_list = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]

print(sorted(nest_list))

print(sorted(nest_list, key=lambda x: x[1]))

print(sorted(nest_list, key=lambda x: x[1], reverse=True))

print("------------------------------------------------------------")  # 60個

mylist = [5, 10, 15, 20, 25, 30]

oddlist = list(filter(lambda x: (x % 2 == 1), mylist))

# 輸出奇數串列
print("奇數串列: ", oddlist)

print("------------------------------------------------------------")  # 60個

mylist = [5, 10, 15, 20, 25, 30]

squarelist = list(map(lambda x: x**2, mylist))

# 輸出串列元素的平方值
print("串列的平方值: ", squarelist)

print("------------------------------------------------------------")  # 60個


cal_dict = {
    "加": lambda x, y: x + y,
    "減": lambda x, y: x - y,
    "乘": lambda x, y: x * y,
    "除": lambda x, y: x / y,
}


def calculator(x, operator, y):
    return cal_dict.get(operator, lambda: None)(x, y)


print(calculator(6, "乘", 7))

calculator = {
    "加": lambda x, y: x + y,
    "減": lambda x, y: x - y,
    "乘": lambda x, y: x * y,
    "除": lambda x, y: x / y,
}

default = lambda: None

print(calculator.get("加", default)(1, 2))
print(calculator.get("乘", default)(3, 5))


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
