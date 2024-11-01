import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


class Myclass:
    # 文件字串實例, Myclass類別的應用

    def __init__(self, x):
        self.x = x

    def printMe(self):
        # 文字檔字串實例, Myclass類別內printMe方法的應用
        print("Hi", self.x)


data = Myclass(100)
data.printMe()
print(data.__doc__)  # 列印Myclass文件字串docstring
print(data.printMe.__doc__)  # 列印printMe文件字串docstring

print("------------------------------------------------------------")  # 60個


class Geometric:
    def __init__(self):
        self.color = "Green"


class Circle(Geometric):
    def __init__(self, radius):
        super().__init__()
        self.PI = 3.14159
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def getDiameter(self):
        return self.radius * 2

    def getPerimeter(self):
        return self.radius * 2 * self.PI

    def getArea(self):
        return self.PI * (self.radius**2)

    def getColor(self):
        return color


A = Circle(5)
print("圓形的顏色 : ", A.color)
print("圓形的半徑 : ", A.getRadius())
print("圓形的直徑 : ", A.getDiameter())
print("圓形的圓周 : ", A.getPerimeter())
print("圓形的面積 : ", A.getArea())
A.setRadius(10)
print("圓形的直徑 : ", A.getDiameter())

print("------------------------------------------------------------")  # 60個


class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        return (self.x, self.y)


a = shape(100, 200)
b = shape(200, 300)
print(a.info())
print(b.info())

print("------------------------------------------------------------")  # 60個


class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class circle(shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def info(self):
        return ("圓形", self.x, self.y, self.r)


class rectangle(shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def info(self):
        return ("矩形", self.x, self.y, self.w, self.h)


a = shape(100, 200)
b = shape(200, 300)
c = circle(100, 200, 50)
d = rectangle(100, 200, 50, 50)
shapes = [a, b, c, d]
for s in shapes:
    print("info :", s.info())

print("D info :", d.info())
print("D 往x前進50點，y後退20點")
d.move(50, -20)
print("D info :", d.info())

print("------------------------------------------------------------")  # 60個


# 狗類基底類別
class DOG:
    # 建構式！
    def __init__(self, breed, size, age, color):
        self.Breed = breed
        self.Size = size
        self.Age = age
        self.Color = color

    # Eat方法
    def Eat(self):
        print("I am a " + self.Breed + ", now I'm eating.")

    # Sleep方法
    def Sleep(self):
        print("I am a " + self.Breed + ", now I'm sleeping.")

    # Sit方法
    def Sit(self):
        print("I am a " + self.Breed + ", now I'm sitting.")

    # Run方法
    def Run(self):
        print("I am a " + self.Breed + ", now I'm running.")

    # __str__方法，將物件用字串表達
    def __str__(self):
        return (
            "I am a "
            + self.Breed
            + ", I'm "
            + str(self.Age)
            + " years old, my body size is "
            + self.Size
            + " and my color is "
            + self.Color
            + "."
        )


# 實體化第一隻狗
dog1 = DOG("Neapolitan Mastiff", "Large", 5, "Black")
print(dog1)
dog1.Eat()  # 吃
dog1.Sleep()  # 睡

# 實體化第二隻狗
dog2 = DOG("Maltese", "Small", 2, "White")
print(dog2)
dog2.Sleep()  # 睡
dog2.Sit()  # 坐

# 實體化第三隻狗
dog3 = DOG("Chow Chow", "Medium", 3, "Brown")
print(dog3)
dog3.Sit()  # 坐
dog3.Run()  # 跑

print("------------------------------------------------------------")  # 60個


# 手機類基底類別
class MobilePhone:
    def touch(self):
        print("我能提供螢幕觸控操作的功能")


# HTC類衍生類別(繼承 手機類基底類別)
class HTC(MobilePhone):
    def touch(self):
        MobilePhone.touch(self)
        print("我也能提供多點觸控的操作方式")


print("建立物件 helen")
helen = HTC()
helen.touch()

print("------------------------------------------------------------")  # 60個


class CoffeeMaker:
    def __init__(self):
        self.power = False  # 初始化咖啡機電源：關
        self.waterTemp = 20  # 室溫水的溫度，攝氏20度

    def switchPower(self):
        self.power = ~self.power  # 切換開關就是這樣做的！

    def getWaterTemp(self):
        return self.waterTemp  # 回傳咖啡機水溫

    def heatWater(self):
        # 將水加熱到可沖咖啡的溫度：攝氏90度
        print("正在加熱水溫")
        self.waterTemp = 90
        print("完成！")

    def brewCoffee(self):
        if self.power:  # 一切要咖啡機開了才可以！
            print("開始沖泡咖啡...")
            if self.waterTemp < 90:
                print("水溫不足")
                self.heatWater()  # 呼叫物件方法，加熱水溫
            print("沖泡咖啡...")
            print("完成！")
        else:
            print("未開機")


cm1 = CoffeeMaker()  # 咖啡機一號出現了！
cm1.brewCoffee()  # 直接沖咖啡？能沖才有鬼
cm1.switchPower()  # 先開電源，正解
cm1.brewCoffee()  # 順利沖咖啡了！

print("------------------------------------------------------------")  # 60個


class Book:
    # 定義方法一：取得書籍名稱和價格
    def setInfo(self, title, price):
        self.title = title
        self.price = price

    # 定義方法二：輸出書籍名稱和價格
    def showInfo(self):
        print("書籍名稱:{0:6s}, 價格:{1:4s}元".format(self.title, self.price))


print("建立物件 book1")
book1 = Book()
book1.setInfo("Python一週速成", "360")
book1.showInfo()  # 呼叫方法

print("建立物件 book2")
book2 = Book()
book2.setInfo("網路行銷與社群行銷", "520")
book2.showInfo()

print("------------------------------------------------------------")  # 60個


# 宣告類別
class student:
    def score(self, s1, s2, s3):
        return (s1 + s2 + s3) / 3


print("建立物件 vicky")
vicky = student()
# 呼叫score()方法並傳入引數
average = vicky.score(98, 65, 81)
print(f"Vicky 平均分數：{average:.3f}")

print("------------------------------------------------------------")  # 60個


class Score:
    def __init__(self, score):
        self.__score = score

    def getscore(self):
        return self.__score

    def setscore(self, score):
        self.__score = score

    sc = property(getscore, setscore)  # Python 風格


stu = Score(50)
print(stu.getscore())
stu.score = 100  # 無效
print(stu.getscore())

stu = Score(0)
print(stu.getscore())
stu.setscore(80)
print(stu.getscore())

stu = Score(0)
print(stu.sc)
stu.sc = 80
print(stu.sc)

print("------------------------------------------------------------")  # 60個


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


def adapt_point(point):
    return "%f;%f" % (point.x, point.y)


p1 = Point(4.0, -3.2)
p2 = Point(8.0, 1.2)

print(adapt_point(p1))
print(adapt_point(p2))

print("------------------------------------------------------------")  # 60個


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):  # 讓加法運算子"+"動得起來
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 + p2)  # (3, 5)

print("------------------------------------------------------------")  # 60個


class NannyNag(Exception):
    def __init__(self, lineno, msg, line):
        self.lineno, self.msg, self.line = lineno, msg, line

    def get_lineno(self):
        return self.lineno

    def get_msg(self):
        return self.msg

    def get_line(self):
        return self.line


nag = NannyNag(123, "kkk", 456)
badline = nag.get_lineno()
line = nag.get_line()

print("%r: *** Line %d: trouble in tab city! ***" % ("dddd", badline))
print("offending line: %r" % (line,))

print(nag.get_msg())
print("dddd", badline, repr(line))


print("------------------------------------------------------------")  # 60個


class Tom:  # 父類別
    def __init__(self):
        self.height1 = 178


class Andy(Tom):  # 父類別是Tom
    def __init__(self):
        self.height2 = 180
        super().__init__()


class Michael(Tom):  # 父類別是Tom
    def __init__(self):
        self.height3 = 185
        super().__init__()

    def display(self):
        print("父親Tom的身高:", self.height1, "公分")
        print("兄弟Andy的身高:", Andy().height2, "公分")
        print("自己Michael的身高:", m1.height3, "公分")


m1 = Michael()
m1.display()

print("------------------------------------------------------------")  # 60個


# 父類別
class Rectangle:
    def __init__(self, width, height):
        self.width = width  # 定義共用屬性
        self.height = height  # 定義共用屬性

    def area(self):  # 定義共用方法
        return self.width * self.height


# 子類別 Triangle, 繼承 Rectangle
# 三角形 繼承 矩形, 可用area(), 新增area2()
class Triangle(Rectangle):
    def area2(self):  # 定義子類別的共用方法
        return (self.width * self.height) / 2


print("父類別 Rectangle")
rectangle = Rectangle(5, 6)  # 建立物件 rectangle
print("rectangle 矩形面積 :", rectangle.area())  # 30

print("子類別 Triangle, 繼承 Rectangle")
triangle = Triangle(5, 6)  # 建立物件 triangle
print("triangle 矩形面積 :", triangle.area())  # 30
print("triangle 三角形面積 :", triangle.area2())  # 15

print("------------------------------------------------------------")  # 60個


class City:
    def __init__(self, name):
        self.name = name

    def equals(self, city2):
        return self.name.upper() == city2.name.upper()

    def __eq__(self, city2):
        return self.name.upper() == city2.name.upper()


city1 = City("Taipei")
city2 = City("taipei")
city3 = City("myhome")
print(city1.equals(city2))
print(city1.equals(city3))
print(city1 == city2)
print(city1 == city3)

print("------------------------------------------------------------")  # 60個

print("測試hasattr功能")
print("內建函數 (function) hasattr() ，判斷參數 (parameter) name 是否為 object 的屬性名稱")


class Demo:
    def __init__(self, i):
        self.i = i
        self.x = "xxx"
        self.y = "yyy"
        self.z = "zzz"

    def __str__(self):
        return str(self.i)

    def hello(self):
        print("hello " + self.__str__())


d = Demo(22)

print(hasattr(d, "t"))  # 不是
print(hasattr(d, "u"))  # 不是
print(hasattr(d, "v"))  # 不是
print(hasattr(d, "w"))  # 不是
print(hasattr(d, "x"))  # 是
print(hasattr(d, "y"))  # 是
print(hasattr(d, "z"))  # 是

print("------------------------------------------------------------")  # 60個


class poker:
    def __init__(self):
        self.deck = [i for i in range(52)]
        random.shuffle(self.deck)
        self.card_type = ["黑桃", "紅心", "梅花", "方塊"]
        self.index = 0

    def decode(self, card):
        suit = self.card_type[card // 13]
        no = card % 13 + 1
        if no == 1:
            no = "A"
        elif no > 10:
            no = chr((no - 11) + ord("J"))
        return (suit, str(no))

    def showAll(self):
        for card in self.deck:
            print(self.decode(card), end="")
        print()

    def dealFive(self):
        for i in range(5):
            print(self.decode(self.deck[self.index]), end="")
            self.index += 1
        print()

    def oneMore(self):
        print(self.decode(self.deck[self.index]), end="")
        self.index += 1
        print()

    def shuffle(self):
        random.shuffle(self.deck)
        self.index = 0


"""
p = poker()
p.showAll()
print("------")
p.dealFive()
for i in range(3):
    p.oneMore()
print("------")
p.shuffle()
p.showAll()
print("------")
p.dealFive()
"""

print("------------------------------------------------------------")  # 60個


# 宣告類別
class Motor:
    def __init__(self):
        # 屬性
        self.name = "CCCCCC"
        self.color = "XXXXXX"

    # 打印物件訊息
    def __repr__(self):
        return f"Motor({self.name, self.color})"

    # 定義方法一：取得名稱和顏色
    def setupCar(self, name, color):
        self.name = name
        self.color = color

    # 定義方法二：輸出名稱和顏色
    def showMessage(self):
        print(f"款式:{self.name:6s},", f"顏色:{self.color:4s}")


print("建立物件 car1")
car1 = Motor()
car1.showMessage()  # 呼叫方法
car1.setupCar("Vios", "極光藍")
car1.showMessage()  # 呼叫方法

print("建立物件 car2")
car2 = Motor()
car2.showMessage()
car2.setupCar("Altiss", "炫魅紅")
car2.showMessage()

print("打印物件訊息, 使用__repr__")
print(car1)
print(car2)

print("------------------------------------------------------------")  # 60個


# 宣告類別
class newClass:
    # __new__()建構物件
    def __new__(Kind, name):
        if name != "":
            print("物件已建構")
            return object.__new__(Kind)
        else:
            print("物件未建構")
            return None

    # __init__()初始化物件
    def __init__(self, name):
        print("物件初始化...")
        print(name)


print("建立物件 x")
x = newClass("")

print("建立物件 y")
y = newClass("Second")

print("------------------------------------------------------------")  # 60個


# 父類別 Plant
class Plant:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("plant", self.name)


# 子類別 Fruit, 繼承 Plant
class Fruit(Plant):
    def show(self):
        print("fruit", self.name)


print("父類別 Plant")
p = Plant("banana")
p.show()

print("子類別 Fruit, 繼承 Plant")
f = Fruit("banana")
f.show()

print("------------------------------------------------------------")  # 60個


class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


for i in Fib(100):
    print(i)

print("------------------------------------------------------------")  # 60個


class newFruit:
    color = "red"

    def taste(self):
        return "delicious"


apple = newFruit()
cc = apple.color
print(cc)

cc = apple.taste()
print(cc)

print("------------------------------------------------------------")  # 60個


class Date:
    def setDate(self, birthday):  # 第一種方法
        self.birthday = birthday

    def showDate(self):  # 第二種方法
        print("出生年月日:", self.birthday)


d1 = Date()  # 第一個物件
d1.setDate("民國67年7月3日")  # 呼叫方法時傳入字串
d1.showDate()
d2 = Date()  # 第二個物件
d2.setDate([67, 7, 3])  # 呼叫方法時傳入串列

print("------------------------------------------------------------")  # 60個


def bar(self, name):
    self._name = name


def foo(self, course_name):
    print("%s正在學習%s." % (self._name, course_name))


Student = type("Student", (object,), dict(__init__=bar, study=foo))
stu1 = Student("駱昊")
stu1.study("Python程序設計")

print("------------------------------------------------------------")  # 60個


def _foo():
    print("test")


class Student(object):
    # __init__是一個特殊方法用于在創建對象時進行初始化操作
    # 通過這個方法我們可以為學生對象綁定name和age兩個屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在學習%s." % (self.name, course_name))

    # PEP 8要求標識符的名字用全小寫多個單詞用下劃線連接
    # 但是很多程序員和公司更傾向于使用駝峰命名法(駝峰標識)
    def watch_av(self):
        if self.age < 18:
            print("%s只能觀看《熊出沒》." % self.name)
        else:
            print("%s正在觀看島國大電影." % self.name)


stu1 = Student("駱昊", 38)
stu1.study("Python程序設計")
stu1.watch_av()
stu2 = Student("王大錘", 15)
stu2.study("思想品德")
stu2.watch_av()

print("------------------------------------------------------------")  # 60個


class Rect(object):
    # 矩形類

    def __init__(self, width=0, height=0):
        # 初始化方法
        self.__width = width
        self.__height = height

    def perimeter(self):
        # 計算周長
        return (self.__width + self.__height) * 2

    def area(self):
        # 計算面積
        return self.__width * self.__height

    def __str__(self):
        # 矩形對象的字符串表達式
        return "矩形[%f,%f]" % (self.__width, self.__height)

    def __del__(self):
        # 析構器
        print("銷毀矩形對象")


rect1 = Rect()
print(rect1)
print(rect1.perimeter())
print(rect1.area())

rect2 = Rect(3.5, 4.5)
print(rect2)
print(rect2.perimeter())
print(rect2.area())

print("------------------------------------------------------------")  # 60個


class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")


test = Test("hello")
test._Test__bar()
print(test._Test__foo)

print("------------------------------------------------------------")  # 60個

# 父類基底類別
class Father:
    def __init__(self):
        self.__address = "台北市羅斯福路"

    def getaddr(self):
        return self.__address

    def walking(self):
        print("父類別之函數 AAAAA")

# 子類衍生類別(繼承 父類基底類別)
class Son(Father):
    # 同名的函數，若有，則使用子類別之函數
    def walking(self):
        print("子類別之函數 BBBBB")

print("建立物件 frank")
frank = Father()
print("建立物件 steve")
steve = Son()

print("使用父類別函數 :", frank.getaddr())
print("使用子類別函數 :", steve.getaddr())

print("呼叫函數，父類別的函數")
frank.walking()

print("呼叫函數，繼承自父類別的函數")
steve.walking()

print("------------------------------------------------------------")  # 60個


# 祖父類基底類別
class Grandfather:
    pass


# 父親類衍生類別(繼承 祖父類基底類別)
class Father(Grandfather):
    pass


# 伊凡類衍生類別(繼承 父親類基底類別)
class Ivan(Father):
    def fn(self):
        pass


grandfather = Grandfather()
father = Father()
ivan = Ivan()
print("grandfather物件類型: ", type(grandfather))
print("father物件類型     : ", type(father))
print("ivan物件類型       : ", type(ivan))
print("ivan物件fn方法類型 : ", type(ivan.fn))

print("------------------------------------------------------------")  # 60個


# 祖父類基底類別
class Grandfather:
    pass


# 父親類衍生類別(繼承 祖父類基底類別)
class Father(Grandfather):
    pass


# 伊凡類衍生類別(繼承 父親類基底類別)
class Ivan(Father):
    def fn(self):
        pass


grandfa = Grandfather()
father = Father()
ivan = Ivan()
print("ivan屬於Ivan類別: ", isinstance(ivan, Ivan))
print("ivan屬於Father類別: ", isinstance(ivan, Father))
print("ivan屬於GrandFather類別: ", isinstance(ivan, Grandfather))
print("father屬於Ivan類別: ", isinstance(father, Ivan))
print("father屬於Father類別: ", isinstance(father, Father))
print("father屬於Grandfather類別: ", isinstance(father, Grandfather))
print("grandfa屬於Ivan類別: ", isinstance(grandfa, Ivan))
print("grandfa屬於Father類別: ", isinstance(grandfa, Father))
print("grandfa屬於Grandfather類別: ", isinstance(grandfa, Grandfather))

print("------------------------------------------------------------")  # 60個

# 祖父類基底類別
class Grandfather:
    def __init__(self):
        self.grandfathermoney = 10000

    def get_info1(self):
        print("Grandfather's information")


# 父親類衍生類別(繼承 祖父類基底類別)
class Father(Grandfather):
    def __init__(self):
        self.fathermoney = 8000
        super().__init__()

    def get_info2(self):
        print("Father's information")


# 伊凡類衍生類別(繼承 父親類基底類別)
class Ivan(Father):
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()

    def get_info3(self):
        print("Ivan's information")

    def get_money(self):  # 取得資產明細
        print(
            "\nIvan資產: ",
            self.ivanmoney,
            "\n父親資產: ",
            self.fathermoney,
            "\n祖父資產: ",
            self.grandfathermoney,
        )


ivan = Ivan()
ivan.get_info3()  # 從Ivan中獲得
ivan.get_info2()  # 流程 Ivan -> Father
ivan.get_info1()  # 流程 Ivan -> Father -> Grandtather
ivan.get_money()  # 取得資產明細

print("------------------------------------------------------------")  # 60個


# 父親類基底類別
class Father:
    def __init__(self):
        self.fathermoney = 10000


# 伊拉類衍生類別(繼承 父親類基底類別)
class Ira(Father):
    def __init__(self):
        self.iramoney = 8000
        super().__init__()


# 伊凡類衍生類別(繼承 父親類基底類別)
class Ivan(Father):
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()

    def get_money(self):  # 取得資產明細
        print(
            "Ivan資產: ",
            self.ivanmoney,
            "\n父親資產: ",
            self.fathermoney,
            "\nIra資產 : ",
            Ira().iramoney,
        )  # 注意寫法


ivan = Ivan()
ivan.get_money()  # 取得資產明細

print("------------------------------------------------------------")  # 60個


# 祖父類基底類別
class Grandfather:
    def action1(self):
        print("Grandfather")


# 父親類衍生類別(繼承 祖父類基底類別)
class Father(Grandfather):
    def action2(self):  # 定義action2()
        print("Father")


# 叔叔類衍生類別(繼承 祖父類基底類別)
class Uncle(Grandfather):
    def action2(self):  # 定義action2()
        print("Uncle")


# 伊凡類衍生類別(繼承 父親類基底類別 和 叔叔類基底類別)
class Ivan(Father, Uncle):
    def action3(self):
        print("Ivan")


ivan = Ivan()
ivan.action3()  # 順序 Ivan
ivan.action2()  # 順序 Ivan -> Father
ivan.action1()  # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個


# 祖父類基底類別
class Grandfather:
    def action1(self):
        print("Grandfather")


# 父親類衍生類別(繼承 祖父類基底類別)
class Father(Grandfather):
    def action3(self):  # 定義action3()
        print("Father")


# 叔叔類衍生類別(繼承 祖父類基底類別)
class Uncle(Grandfather):
    def action2(self):  # 定義action2()
        print("Uncle")


# 伊凡類衍生類別(繼承 父親類基底類別 和 叔叔類基底類別)
class Ivan(Father, Uncle):
    def action4(self):
        print("Ivan")


ivan = Ivan()
ivan.action4()  # 順序 Ivan
ivan.action3()  # 順序 Ivan -> Father
ivan.action2()  # 順序 Ivan -> Father -> Uncle
ivan.action1()  # 順序 Ivan -> Father -> Uncle -> Grandfather

print("------------------------------------------------------------")  # 60個

print("繼承, 子類別方法 覆寫 父類別方法")


# 鳥類基底類別
class Bird:  # 父類別
    def fly(self):
        print("大多數鳥能飛翔")

    def swim(self):
        print("少部份鳥能游水")

    def display(self):
        print("我是鳥類")


# 鸚鵡類衍生類別(繼承 鳥類基底類別)
class Parrot(Bird):  # 繼承Bird
    def fly(self):  # 覆寫方法
        print("鸚鵡能飛翔")

    def swim(self):  # 覆寫方法
        print("鸚鵡不能游水")


# 企鵝類衍生類別(繼承 鳥類基底類別)
class Penguin(Bird):  # 繼承Bird
    def fly(self):  # 覆寫方法
        print("企鵝不能飛翔")

    def swim(self):  # 覆寫方法
        print("企鵝能游水")


# 共同介面
def flying_test(bird):
    bird.fly()


def display_test(bird):
    bird.display()


print("建立物件 p1")
p1 = Parrot()
print("建立物件 p2")
p2 = Penguin()

# 傳入物件測試
flying_test(p1)
flying_test(p2)

# 傳入物件測試
display_test(p1)
display_test(p2)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("檢查至此")
print("------------------------------------------------------------")  # 60個

print("繼承")


# 動物類基底類別
class animalBaseClass:
    animallegs = 4

    def walk(self):
        print("走動")

    def cry(self):
        print("吼叫")

    def getLegsNum(self):
        print(self.animallegs)


# 狗類衍生類別(繼承 動物類基底類別)
class dogClass(animalBaseClass):
    def __init__(self):
        print("我是小狗")


david = dogClass()
david.walk()
david.cry()
david.getLegsNum()

print("------------------------------------------------------------")  # 60個


# 動物類基底類別
class animalBaseClass:
    animallegs = 2

    def walk(self):
        print("走動")

    def cry(self):
        print("吼叫")


# 鳥類衍生類別(繼承 動物類基底類別)
class birdClass(animalBaseClass):
    def __init__(self):
        print("我是小鳥")

    def cry(self):
        print("啾啾")


bryan = birdClass()
bryan.walk()
bryan.cry()

print("------------------------------------------------------------")  # 60個


# 動物類基底類別
class animalBaseClass:
    def __init__(self, num):
        self.animallegs = num

    def walk(self):
        print("走動")

    def cry(self):
        print("吼叫")

    def getLegsNum(self):
        print(self.animallegs)


# 蛇類衍生類別(繼承 動物類基底類別)
class snakeClass(animalBaseClass):
    def __init__(self, num):
        parent_class = super(snakeClass, self)
        parent_class.__init__(num)
        print("我是蛇")


steve = snakeClass(0)
steve.getLegsNum()

print("------------------------------------------------------------")  # 60個


# 蛇類衍生類別(繼承 動物類基底類別)
class snakeClass(animalBaseClass):
    def __init__(self):
        snake_leg = 0
        parent_class = super(snakeClass, self)
        parent_class.__init__(snake_leg)
        print("我是蛇")


steve = snakeClass()
steve.getLegsNum()

print("------------------------------------------------------------")  # 60個


# 動物類基底類別
class animalBaseClass:
    def __init__(self, num):
        self.animallegs = num

    def walk(self):
        print("走動")

    def cry(self):
        print("吼叫")

    def getLegsNum(self):
        print(self.animallegs)


# 狗類衍生類別(繼承 動物類基底類別)
class dogClass(animalBaseClass):
    def __init__(self, num):
        parent_class = super(dogClass, self)
        parent_class.__init__(num)
        print("我是小狗")


# 鳥類衍生類別(繼承 動物類基底類別)
class birdClass(animalBaseClass):
    def __init__(self, num):
        parent_class = super(birdClass, self)
        parent_class.__init__(num)
        print("我是小鳥")

    def cry(self):
        print("啾啾")


# 蛇類衍生類別(繼承 動物類基底類別)
class snakeClass(animalBaseClass):
    def __init__(self, num):
        parent_class = super(snakeClass, self)
        parent_class.__init__(num)
        print("我是蛇")


david = dogClass(4)
david.walk()
david.cry()
david.getLegsNum()

bryan = birdClass(2)
bryan.walk()
bryan.cry()
bryan.getLegsNum()

steve = snakeClass(0)
steve.walk()
steve.cry()
steve.getLegsNum()

print("------------------------------------------------------------")  # 60個


# 定義Student類別
class Student:
    # 建構子
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # 方法
    def displayStudent(self):
        print("姓名: ", self.name)
        print("成績: ", self.grade)

    def whoami(self):
        return self.name


print("建立物件 s1")
s1 = Student("陳會安", 90)
s1.displayStudent()  # 呼叫方法

print("s1.whoami(): ", s1.whoami())
# 存取資料欄位
print("s1.name: ", s1.name)
print("s1.grade: ", s1.grade)

print("------------------------------------------------------------")  # 60個


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


print("建立物件 s1")
s1 = Student("陳會安", 85)
s1.displayStudent()  # 呼叫方法

print("s1.whoami() = " + s1.whoami())
# 存取資料欄位
print("s1.name = " + s1.name)
print("s1.grade = " + str(s1.grade))

print("------------------------------------------------------------")  # 60個


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


print("建立物件 s1")
s1 = Student("陳會安", 85)
s1.displayStudent()  # 呼叫方法

# print("s1.__getGrade() = " + str(s1.__getGrade()))
# 存取資料欄位
print("s1.name = " + s1.name)
# print(s1.__grade)

print("------------------------------------------------------------")  # 60個


# 定義Student類別
class Student:
    count = 0

    # 建構子
    def __init__(self, name):
        self.name = name
        Student.count += 1

    # 方法
    def getCount(self):
        return Student.count

    def getName(self):
        return self.name


print("建立物件 s1")
s1 = Student("陳會安")
print(s1.getCount(), s1.getName())

print("建立物件 s2")
s2 = Student("陳允傑")
print(s2.getCount(), s2.getName())

print("建立物件 s3")
s3 = Student("江小魚")
print(s3.getCount(), s3.getName())

print("學生數: ", Student.count)

print("------------------------------------------------------------")  # 60個


# 定義Vehicle父類別
class Vehicle:
    # 建構子
    def __init__(self, name):
        self.name = name

    # 方法
    def getName(self):
        return self.name

    # 方法
    def displayVehicle(self):
        print("廠牌: ", self.name)


# 定義Car子類別
class Car(Vehicle):
    # 建構子
    def __init__(self, name, model):
        # 呼叫父類別的建構子
        super().__init__(name)
        self.model = model

    # 方法
    def displayVehicle(self):
        print("名稱: ", self.getName())
        print("車型: ", self.model)


print("建立物件 v1")
v1 = Vehicle("BMW")
v1.displayVehicle()  # 呼叫方法

print("建立物件 c1")
c1 = Car("Ford", "GT350")
c1.displayVehicle()  # 呼叫方法

print("------------------------------------------------------------")  # 60個

print("兩棲動物")


class Vehicle:
    def __init__(self):
        print("Vehicle-start")
        print("Vehicle-done")


class WheeledVehicle(Vehicle):
    def __init__(self):
        print("WheeledVehicle-start")
        super().__init__()
        print("WheeledVehicle-done")


class WaterVehicle(Vehicle):
    def __init__(self):
        print("WaterVehicle-start")
        super().__init__()
        print("WaterVehicle-done")


class Amphibian(WheeledVehicle, WaterVehicle):
    def __init__(self):
        print("Amphibian-start")
        super().__init__()
        print("Amphibian-done")


amphibian = Amphibian()

Amphibian.mro()

print("------------------------------------------------------------")  # 60個


# 定義 Vehicle 類別來表示車輛
class Vehicle:
    # 初始化方法，設置車輛的製造商、型號和生產年份
    def __init__(self, make, model, year):
        self.make = make  # 車輛的製造商
        self.model = model  # 車輛的型號
        self.year = year  # 車輛的生產年份

    # 方法回傳車輛的基本資料
    def get_info(self):
        # 回傳格式化的車輛資料字串
        return f"{self.year} {self.make} {self.model}"


# 使用 Vehicle 類別來建立車輛物件並獲取車輛資料
print("建立物件 car")
car = Vehicle("Lexus", "ES 300h", 2025)  # 建立一個 Vehicle 對象
info = car.get_info()  # get_info方法獲取車輛資料
print(info)  # 輸出：'2025 ES 300h'

print("------------------------------------------------------------")  # 60個


class staff:
    def salary(self):
        return "10000元"


yamamoto = staff()
yamamoto.salary()

print("------------------------------------------------------------")  # 60個


class staff:
    def __init__(self, bonus):
        self.bonus = bonus

    def salary(self):
        salary = 10000 + self.bonus
        return salary


yamamoto = staff(50000)
money = yamamoto.salary()
print(money)

print("------------------------------------------------------------")  # 60個


class staff:
    bonus = 30000

    def salary(self):
        salary = 10000 + self.bonus
        return salary


yamamoto = staff()
yamamoto.salary()

print("------------------------------------------------------------")  # 60個


class staff:
    def __init__(self, bonus):
        self.bonus = bonus

    def salary(self):
        salary = 10000 + self.bonus
        return salary


yamamoto = staff(50000)
yamamoto.salary()

print("------------------------------------------------------------")  # 60個


# 動物類基底類別
class Animals:
    def __init__(self, animal_name, animal_age):
        self.name = animal_name  # 紀錄動物名稱
        self.age = animal_age  # 紀錄動物年齡

    def run(self):  # 輸出動物 is running
        print(self.name.title(), " is running")


# 狗類衍生類別(繼承 動物類基底類別)
class Dogs(Animals):
    def __init__(self, dog_name, dog_age):
        super().__init__("My pet " + dog_name.title(), dog_age)

    def sleeping(self):
        print("My pet", "is sleeping")


print("建立物件 mycat")
mycat = Animals("lucy", 5)  # 建立Animals物件以及測試
print(mycat.name.title(), " is ", mycat.age, " years old.")
mycat.run()

print("建立物件 mydog")
mydog = Dogs("lily", 6)  # 建立Dogs物件以及測試
print(mydog.name.title(), " is ", mydog.age, " years old.")
mydog.run()
mydog.sleeping()

print("------------------------------------------------------------")  # 60個


# 動物類基底類別
class Animals:
    def __init__(self, animal_name):
        self.name = animal_name  # 紀錄動物名稱

    def which(self):  # 回傳動物名稱
        return "My pet " + self.name.title()

    def action(self):  # 動物的行為
        return " sleeping"


# 狗類衍生類別(繼承 動物類基底類別)
class Dogs(Animals):
    def __init__(self, dog_name):  # 紀錄動物名稱
        super().__init__(dog_name.title())

    def action(self):  # 動物的行為
        return " running in the street"


class Monkeys:
    # 猴子類別, 這是其他類別

    def __init__(self, monkey_name):  # 紀錄動物名稱
        self.name = "My monkey " + monkey_name.title()

    def which(self):  # 回傳動物名稱
        return self.name

    def action(self):  # 動物的行為
        return " running in the forest"


def doing(obj):  # 列出動物的行為
    print(obj.which(), "is", obj.action())


my_cat = Animals("lucy")  # Animals物件
doing(my_cat)
my_dog = Dogs("gimi")  # Dogs物件
doing(my_dog)
my_monkey = Monkeys("taylor")  # Monkeys物件
doing(my_monkey)

print("------------------------------------------------------------")  # 60個


# 此程式單純類別定義,沒有任何輸出到螢幕的執行結果
class Company:  # 定義公司類別
    name = "賺大錢有限公司"

    def slogan(self):
        print("優良品質 創新研發 強力行銷")


print("------------------------------------------------------------")  # 60個


class Wage:
    def __init__(self, fee=200, hour=80):
        self.fee = fee
        self.hour = hour

    def getArea(self):
        return self.fee * self.hour


tom = Wage()
print("透過init()方法預設值的總薪資: ", tom.getArea(), "元")

jane = Wage(250, 100)
print("透過init()方法傳入參數的總薪資: ", jane.getArea(), "元")

print("------------------------------------------------------------")  # 60個


class Animal:  # 祖父類別
    def feature1(self):
        print("大多數動物能自發且獨立地移動")


class Human(Animal):  # 父類別一
    def feature2(self):
        print("人類是一種有思考能力與情感的高級動物")


class Fish(Animal):  # 父類別二
    def feature3(self):
        print("水生脊椎動物的總稱")


class Mermaid(Human, Fish):  # 子類別同時繼承兩種類別
    def feature4(self):
        print("又稱人魚,傳說中的生物同時具備人及魚的部份特性")


print("建立物件 tiger")
tiger = Animal()

print("建立物件 daniel")
daniel = Human()

print("建立物件 goldfish")
goldfish = Fish()

print("建立物件 alice")
alice = Mermaid()

print("tiger是屬於Animal類別:", isinstance(tiger, Animal))
print("daniel是屬於Animal類別:", isinstance(daniel, Animal))
print("goldfish是屬於Animal類別:", isinstance(goldfish, Animal))
print("alice是屬於Animal類別:", isinstance(alice, Animal))
print("===============================================")
print("tiger是屬於Human類別:", isinstance(tiger, Human))
print("daniel是屬於Human類別:", isinstance(daniel, Human))
print("goldfish是屬於Human類別:", isinstance(goldfish, Human))
print("alice是屬於Human類別:", isinstance(alice, Human))
print("===============================================")
print("tiger是屬於Fish類別:", isinstance(tiger, Fish))
print("daniel是屬於Fish類別:", isinstance(daniel, Fish))
print("goldfish是屬於Fish類別:", isinstance(goldfish, Fish))
print("alice是屬於Fish類別:", isinstance(alice, Fish))
print("===============================================")
print("tiger是屬於Mermaid類別:", isinstance(tiger, Mermaid))
print("daniel是屬於Mermaid類別:", isinstance(daniel, Mermaid))
print("goldfish是屬於Mermaid類別:", isinstance(goldfish, Mermaid))
print("alice是屬於Mermaid類別:", isinstance(alice, Mermaid))

print("------------------------------------------------------------")  # 60個


class Animal:  # 祖父類別
    def feature1(self):
        print("大多數動物能自發且獨立地移動")


class Human(Animal):  # 父類別一
    def feature2(self):
        print("人類是一種有思考能力與情感的高級動物")


class Fish(Animal):  # 父類別二
    def feature3(self):
        print("水生脊椎動物的總稱")


class Mermaid(Human, Fish):  # 子類別同時繼承兩種類別
    def feature4(self):
        print("又稱人魚,傳說中的生物同時具備人及魚的部份特性")


print("Mermaid是屬於Fish子類別:", issubclass(Mermaid, Fish))
print("Mermaid是屬於Human子類別:", issubclass(Mermaid, Human))
print("Mermaid是屬於Animal子類別:", issubclass(Mermaid, Animal))

print("------------------------------------------------------------")  # 60個

# 多重繼承範例1


class Animal:  # 祖父類別
    def feature1(self):
        print("大多數動物能自發且獨立地移動")


class Human(Animal):  # 父類別一
    def feature2(self):
        print("人類是一種有思考能力與情感的高級動物")


class Fish(Animal):  # 父類別二
    def feature2(self):
        print("水生脊椎動物的總稱")


class Mermaid(Human, Fish):  # 子類別同時繼承兩種類別
    def feature3(self):
        print("又稱人魚,傳說中的生物同時具備人及魚的部份特性")


print("建立物件 alice")
alice = Mermaid()
alice.feature1()
alice.feature2()
alice.feature3()

print("------------------------------------------------------------")  # 60個

# 多重繼承範例2


class Animal:  # 祖父類別
    def feature1(self):
        print("大多數動物能自發且獨立地移動")


class Human(Animal):  # 父類別一
    def feature2(self):
        print("人類是一種有思考能力與情感的高級動物")


class Fish(Animal):  # 父類別二
    def feature3(self):
        print("水生脊椎動物的總稱")


class Mermaid(Human, Fish):  # 子類別同時繼承兩種類別
    def feature4(self):
        print("又稱人魚,傳說中的生物同時具備人及魚的部份特性")


print("建立物件 alice")
alice = Mermaid()
alice.feature1()
alice.feature2()
alice.feature3()
alice.feature4()

print("------------------------------------------------------------")  # 60個

print("繼承, 子類別方法 覆寫 父類別方法")


class Normal:  # 父類別
    def subsidy(self, income):
        self.money = income
        if self.money >= 500000:
            print("小康家庭補助金額：", end=" ")
            return 5000


class Poor(Normal):  # 子類別
    def subsidy(self, income):  # 覆寫subsidy方法
        self.money = income
        if self.money < 300000:
            print("中低收入家庭補助金額：", end=" ")
            return 10000


print("建立物件 student1")
student1 = Normal()  # 建立父類別物件
print(student1.subsidy(780000), "元")

print("建立物件 student2")
student2 = Poor()  # 建立子類別物件
print(student2.subsidy(250000), "元")

print("------------------------------------------------------------")  # 60個


# 多型實作
class Colleague:  # 父類別
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def bonus(self):
        return self.income

    def title(self):
        return self.name


class Manager(Colleague):  # 子類別
    def bonus(self):
        return self.income * 1.5


class Director(Colleague):  # 子類別
    def bonus(self):
        return self.income * 1.2


print("===============================")
obj1 = Colleague("一般性員工", 50000)  # 父類別物件
print("{:8s} 紅利 {:,}".format(obj1.title(), obj1.bonus()))

print("===============================")
obj2 = Manager("經理級年終", 80000)  # 子類別物件
print("{:8s} 紅利 {:,}".format(obj2.title(), obj2.bonus()))

print("===============================")
obj3 = Director("芏任級年終", 65000)  # 子類別物件
print("{:8s} 紅利 {:,}".format(obj3.title(), obj3.bonus()))
print("===============================")

print("------------------------------------------------------------")  # 60個


class Wage:
    def __init__(self, h=80):
        self.__hour = h

    def getHour(self):
        return self.__hour

    def pay(self):
        return hour_fee * self.__hour


hour_fee = 200
obj1 = Wage(100)
print("每小時基本工資為:", hour_fee, "元")
print("總共工作的小時數:", obj1.getHour())
print("要付給這位工讀生的薪水總額:", obj1.pay(), "元")

print("------------------------------------------------------------")  # 60個

print("繼承, 子類別方法 覆寫 父類別方法")
# 在子類別呼叫父類別方法—使用super()函式


class Weekday:  # 父類別
    def display(self, pay):
        self.price = pay
        print("歡迎來購物")
        print("購買總金額{:,}".format(self.price))


class Holiday(Weekday):  # 子類別
    def display(self, pay):  # 覆寫display方法
        super().display(pay)
        if self.price >= 15000:
            self.price *= 0.8
        else:
            self.price
        print("8折 {:,}".format(self.price))


monday = Weekday()  # 父類別物件
monday.display(25000)

Christmas = Holiday()  # 子類別物件
Christmas.display(18000)

print("------------------------------------------------------------")  # 60個

# __init__()方法呼叫super()


class Animal:  # 父類別
    def __init__(self):
        print("我屬於動物類別")


class Human(Animal):  # 子類別
    def __init__(self, name):
        super().__init__()
        print("我也屬於人類類別")


man = Human("黃種人")  # 子類別實體

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別
    title = "Taipei Bank"  # 定義屬性

    def motto(self):  # 定義方法
        return "以客為尊"


userbank = Banks()  # 定義物件userbank
print("目前服務銀行是 ", userbank.title)
print("銀行服務理念是 ", userbank.motto())

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別
    title = "Taipei Bank"  # 定義屬性

    def __init__(self, uname, money):  # 初始化方法
        self.name = uname  # 設定存款者名字
        self.balance = money  # 設定所存的錢

    def save_money(self, money):  # 設計存款方法
        self.balance += money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.balance -= money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)


hungbank = Banks("hung", 100)  # 定義物件hungbank
hungbank.get_balance()  # 獲得存款餘額
hungbank.save_money(300)  # 存款300元
hungbank.get_balance()  # 獲得存款餘額
hungbank.withdraw_money(200)  # 提款200元
hungbank.get_balance()  # 獲得存款餘額

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別
    title = "Taipei Bank"  # 定義屬性

    def __init__(self, uname, money):  # 初始化方法
        self.name = uname  # 設定存款者名字
        self.balance = money  # 設定所存的錢

    def save_money(self, money):  # 設計存款方法
        self.balance += money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.balance -= money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)


hungbank = Banks("hung", 100)  # 定義物件hungbank
johnbank = Banks("john", 300)  # 定義物件johnbank
hungbank.get_balance()  # 獲得hung存款餘額
johnbank.get_balance()  # 獲得john存款餘額
hungbank.save_money(100)  # hung存款100
johnbank.withdraw_money(150)  # john提款150
hungbank.get_balance()  # 獲得hung存款餘額
johnbank.get_balance()  # 獲得john存款餘額

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別

    def __init__(self, uname):  # 初始化方法
        self.name = uname  # 設定存款者名字
        self.balance = 0  # 設定開戶金額是0
        self.title = "Taipei Bank"  # 設定銀行名稱

    def save_money(self, money):  # 設計存款方法
        self.balance += money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.balance -= money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)


hungbank = Banks("hung")  # 定義物件hungbank
print("目前開戶銀行 ", hungbank.title)  # 列出目前開戶銀行
hungbank.get_balance()  # 獲得hung存款餘額
hungbank.save_money(100)  # hung存款100
hungbank.get_balance()  # 獲得hung存款餘額

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別

    def __init__(self, uname):  # 初始化方法
        self.name = uname  # 設定存款者名字
        self.balance = 0  # 設定開戶金額是0
        self.title = "Taipei Bank"  # 設定銀行名稱

    def save_money(self, money):  # 設計存款方法
        self.balance += money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.balance -= money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)


hungbank = Banks("hung")  # 定義物件hungbank
hungbank.get_balance()
hungbank.balance = 10000  # 類別外直接竄改存款餘額
hungbank.get_balance()

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別

    def __init__(self, uname):  # 初始化方法
        self.__name = uname  # 設定私有存款者名字
        self.__balance = 0  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"  # 設定私有銀行名稱

    def save_money(self, money):  # 設計存款方法
        self.__balance += money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.__balance -= money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)


hungbank = Banks("hung")  # 定義物件hungbank
hungbank.get_balance()
hungbank.balance = 10000  # 類別外直接竄改存款餘額
hungbank.get_balance()

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別

    def __init__(self, uname):  # 初始化方法
        self.__name = uname  # 設定私有存款者名字
        self.__balance = 0  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"  # 設定私有銀行名稱
        self.__rate = 30  # 預設美金與台幣換匯比例
        self.__service_charge = 0.01  # 換匯的服務費

    def save_money(self, money):  # 設計存款方法
        self.__balance += money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.__balance -= money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):  # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self, usa_d):  # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))


hungbank = Banks("hung")  # 定義物件hungbank
usdallor = 50
print(usdallor, " 美金可以兌換 ", hungbank.usa_to_taiwan(usdallor), " 台幣")

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別

    def __init__(self, uname):  # 初始化方法
        self.__name = uname  # 設定私有存款者名字
        self.__balance = 0  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"  # 設定私有銀行名稱
        self.__rate = 30  # 預設美金與台幣換匯比例
        self.__service_charge = 0.01  # 換匯的服務費

    def save_money(self, money):  # 設計存款方法
        self.__balance += money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.__balance -= money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):  # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self, usa_d):  # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))


class Shilin_Banks(Banks):
    # 定義士林分行
    pass


hungbank = Shilin_Banks("hung")  # 定義物件hungbank
hungbank.save_money(500)
hungbank.get_balance()

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別

    def __init__(self, uname):  # 初始化方法
        self.__name = uname  # 設定私有存款者名字
        self.__balance = 0  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"  # 設定私有銀行名稱
        self.__rate = 30  # 預設美金與台幣換匯比例
        self.__service_charge = 0.01  # 換匯的服務費

    def save_money(self, money):  # 設計存款方法
        self.__balance += money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.__balance -= money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):  # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self, usa_d):  # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):  # 獲得銀行名稱
        return self.__title


class Shilin_Banks(Banks):
    # 定義士林分行
    pass


hungbank = Shilin_Banks("hung")  # 定義物件hungbank
print("我的存款銀行是: ", hungbank.bank_title())

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別

    def __init__(self, uname):  # 初始化方法
        self.__name = uname  # 設定私有存款者名字
        self.__balance = 0  # 設定私有開戶金額是0
        self.title = "Taipei Bank"  # 設定公有銀行名稱
        self.__rate = 30  # 預設美金與台幣換匯比例
        self.__service_charge = 0.01  # 換匯的服務費

    def save_money(self, money):  # 設計存款方法
        self.__balance += money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.__balance -= money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):  # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self, usa_d):  # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):  # 獲得銀行名稱
        return self.title


class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.title = "Taipei Bank - Shilin Branch"  # 定義分行名稱


jamesbank = Banks("James")  # 定義Banks類別物件
print("James's banks = ", jamesbank.title)  # 列印銀行名稱
hungbank = Shilin_Banks("Hung")  # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.title)  # 列印銀行名稱

print("------------------------------------------------------------")  # 60個


class Banks:
    # 定義銀行類別

    def __init__(self, uname):  # 初始化方法
        self.__name = uname  # 設定私有存款者名字
        self.__balance = 0  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"  # 設定私有銀行名稱
        self.__rate = 30  # 預設美金與台幣換匯比例
        self.__service_charge = 0.01  # 換匯的服務費

    def save_money(self, money):  # 設計存款方法
        self.__balance += money  # 執行存款
        print("存款 ", money, " 完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.__balance -= money  # 執行提款
        print("提款 ", money, " 完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):  # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self, usa_d):  # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):  # 獲得銀行名稱
        return self.__title


class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.title = "Taipei Bank - Shilin Branch"  # 定義分行名稱

    def bank_title(self):  # 獲得銀行名稱
        return self.title


jamesbank = Banks("James")  # 定義Banks類別物件
print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
hungbank = Shilin_Banks("Hung")  # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.bank_title())  # 列印銀行名稱

print("------------------------------------------------------------")  # 60個


# 建立類別，產生物件能以不同再別做存取
class Student:
    def message(self, name):  # 方法一
        self.data = name

    def showMessage(self):  # 方法二
        print(self.data)


print("建立物件 s1")
s1 = Student()
s1.message("James McAvoy")  # 呼叫方法時傳入字串
s1.showMessage()

print("建立物件 s2")
s2 = Student()
s2.message(78.566)  # 呼叫方法時傳入浮點數值
s2.showMessage()

print("------------------------------------------------------------")  # 60個


class Person:
    def __init__(self, name, birthyear):
        self._name = name
        self._birthyear = birthyear

    def get_birthyear(self):
        return self._birthyear  # 讀取資料成員

    def set_birthyear(self, v):
        self._birthyear = v  # 寫入資料成員

    def del_birthyear(self):
        del self._birthyear  # 刪除資料成員

    birthyear = property(get_birthyear, set_birthyear, del_birthyear)
    # 設定為屬性存取方法


p1 = Person("約翰", 1985)
print(p1.birthyear)
p1.birthyear = 1988
print(p1.birthyear)
del p1.birthyear
# print(p1.birthyear)        # AttributeError    已刪除, 不可用

print("------------------------------------------------------------")  # 60個


class Student:
    name = "unknown"  # class attribute

    def __init__(self):
        self.age = 20  # instance attribute

    @classmethod
    def tostring(cls):
        print("Student Class Attributes: name=", cls.name)

    @classmethod
    def tostring2(cls):
        print("Student Class Attributes: name=", cls.name, ", age=", cls.age)


Student.tostring()  # 輸出"Student Class Attributes: name= unknown"
stu1 = Student()
stu1.tostring()  # 相同輸出，物件也可以呼叫類別方法

print("------------------------------------------------------------")  # 60個

print("繼承")


class A:  # 沒有標示繼承，預設繼承object
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("A init:", x, ",", y)


class B(A):  # B繼承A，A繼承object
    def __init__(self, x, y, z):
        # super()的意思是先執行好父類別的建構工作
        # super().__init__(x, y)
        super(B, self).__init__(x, y)
        self.z = z
        print("B init:", x, ",", y, ",", z)


b = B(1, 2, 3)
a = A(4, 5)


print("------------------------------------------------------------")  # 60個

print("繼承, 子類別方法 覆寫 父類別方法")


# 動物類基底類別
class Animal:
    def shout(self):
        print("動物吼")


# 狗類衍生類別(繼承 動物類基底類別)
class Dog(Animal):
    def shout(self):  # 覆寫Animal的shout
        print("汪！")


# 貓類衍生類別(繼承 動物類基底類別)
class Cat(Animal):
    def shout(self):  # 覆寫Animal的shout
        print("喵～")


dog1 = Dog()
cat1 = Cat()
dog1.shout()
cat1.shout()

print("------------------------------------------------------------")  # 60個

print("繼承")


# A類基底類別
class A:
    def __init__(self):
        self.x = 3
        self.__pi = 3.14


# B類衍生類別(繼承 A類基底類別)
class B(A):
    def bar(self):
        # return self.__pi 這樣寫會錯！！
        return self._A__pi  # 會被改成_A__pi


b1 = B()

print(b1.bar())  # 3.14

print("------------------------------------------------------------")  # 60個


# 動物類基底類別
class ANIMAL:
    # 建構式！
    def __init__(self, age, color):
        self.Age = age
        self.Color = color

    # __str__方法，將物件用字串表達
    def __str__(self):
        return "I'm " + str(self.Age) + " years old, my color is " + self.Color


# 狗類衍生類別(繼承 動物類基底類別)
class DOG(ANIMAL):
    # 建構式！
    def __init__(self, breed, size, age, color):
        super().__init__(age, color)
        self.Breed = breed
        self.Size = size

    # Eat方法
    def Eat(self):
        print("I am a " + self.Breed + ", now I'm eating.")

    # Sleep方法
    def Sleep(self):
        print("I am a " + self.Breed + ", now I'm sleeping.")

    # Sit方法
    def Sit(self):
        print("I am a " + self.Breed + ", now I'm sitting.")

    # Run方法
    def Run(self):
        print("I am a " + self.Breed + ", now I'm running.")

    # __str__方法，將物件用字串表達
    def __str__(self):
        return (
            "I am a "
            + self.Breed
            + ", my body size is "
            + self.Size
            + ", "
            + super().__str__()
            + "."
        )


# 實體化第一隻狗
dog1 = DOG("Neapolitan Mastiff", "Large", 5, "Black")
print(dog1)
dog1.Eat()  # 吃
dog1.Sleep()  # 睡

# 實體化第二隻狗
dog2 = DOG("Maltese", "Small", 2, "White")
print(dog2)
dog2.Sleep()  # 睡
dog2.Sit()  # 坐

# 實體化第三隻狗
dog3 = DOG("Chow Chow", "Medium", 3, "Brown")
print(dog3)
dog3.Sit()  # 坐
dog3.Run()  # 跑


print("------------------------------------------------------------")  # 60個

print("多重繼承")


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())

# 輸出
# [<class '__main__.M'>, <class '__main__.B'>,
#  <class '__main__.A'>, <class '__main__.X'>,
#  <class '__main__.Y'>, <class '__main__.Z'>,
#  <class 'object'>]

print("------------------------------------------------------------")  # 60個


class Car:
    # 建構式
    def __init__(self, driverSide, doors, power):
        # 布林值，True代表左駕
        self.driverSide = driverSide
        # 可能數值：2, 3, 4，暫不檢查
        self.doors = doors
        # 可能數值：'low', 'median', 'high'，暫不檢查
        self.power = power

    def carType(self):
        # (1) 如果馬力等級是高，則一定是跑車（Sports）
        if self.power == "high":
            return "Sports"
        # (2) 馬力等級不是高，如果車門數是4，則一定是轎車（Sedan）
        elif self.doors == 4:
            return "Sedan"
        # (3) 剩下的只有轎跑車（Coupe）的可能了！
        else:
            return "Coupe"


car1 = Car(True, 4, "low")
car2 = Car(False, 2, "high")
car3 = Car(True, 2, "median")
car4 = Car(False, 4, "median")
print("Car1 type:", car1.carType())
print("Car2 type:", car2.carType())
print("Car3 type:", car3.carType())
print("Car4 type:", car4.carType())

print("------------------------------------------------------------")  # 60個


# 與上一章的寫法類似
class Car:
    # 建構式
    def __init__(self, driverSide, doors, power):
        # 布林值，True代表左駕
        self.driverSide = driverSide
        # 可能數值：2, 3, 4，暫不檢查
        self.doors = doors
        # 可能數值：'low', 'median', 'high'，暫不檢查
        self.power = power


class Sedan(Car):
    # 建構式
    def __init__(self, driverSide, power):
        # 直接設定部份屬性，建構父類別
        super().__init__(driverSide, 4, power)

    def carType(self):
        return "Sedan"


class Coupe(Car):
    # 建構式
    def __init__(self, driverSide, doors):
        # 直接設定部份屬性，建構父類別
        super().__init__(driverSide, doors, "median")

    def carType(self):
        return "Coupe"


class Sports(Car):
    # 建構式
    def __init__(self, driverSide):
        # 直接設定部份屬性，建構父類別
        super().__init__(driverSide, 2, "high")

    def carType(self):
        return "Sports"


# 直接建構各款汽車物件
car1 = Sedan(True, "low")
car2 = Sports(False)
car3 = Coupe(True, 2)
car4 = Sedan(False, "median")
print("Car1 type:", car1.carType())
print("Car2 type:", car2.carType())
print("Car3 type:", car3.carType())
print("Car4 type:", car4.carType())


print("------------------------------------------------------------")  # 60個


class Person:
    def __init__(self, name):
        self.name = name


class LawerPerson(Person):
    def __init__(self, name):
        self.name = name + "律師"


hung = Person("洪錦魁")
lawer = LawerPerson("洪錦魁")
print(hung.name)
print(lawer.name)

print("------------------------------------------------------------")  # 60個


class Person:
    def job(self):
        print("我是老師")


class LawerPerson(Person):
    def job(self):
        print("我是律師")


hung = Person()
ivan = LawerPerson()
hung.job()
ivan.job()

print("------------------------------------------------------------")  # 60個


class Person:
    def interest(self):
        print("Smiling is my interest")


hung = Person()
hung.interest()

print("------------------------------------------------------------")  # 60個


# 動物類基底類別
class Animals:
    def __init__(self, animal_name):
        self.name = animal_name  # 紀錄動物名稱

    def which(self):  # 回傳動物名稱
        return "My pet " + self.name.title()

    def action(self):  # 動物的行為
        return " sleeping"


# 狗類衍生類別(繼承 動物類基底類別)
class Dogs(Animals):
    def __init__(self, dog_name):  # 紀錄動物名稱
        super().__init__(dog_name.title())

    def action(self):  # 動物的行為
        return " running in the street"


class Monkeys:
    """猴子類別, 這是其他類別"""

    def __init__(self, monkey_name):  # 紀錄動物名稱
        self.name = "My monkey " + monkey_name.title()

    def which(self):  # 回傳動物名稱
        return self.name

    def action(self):  # 動物的行為
        return " running in the forest"


def doing(obj):  # 列出動物的行為
    print(obj.which(), "is", obj.action())


my_cat = Animals("lucy")  # Animals物件
doing(my_cat)
my_dog = Dogs("gimi")  # Dogs物件
doing(my_dog)
my_monkey = Monkeys("taylor")  # Monkeys物件
doing(my_monkey)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


class A:
    def __init__(self):
        print("class A")


class B:
    def __init__(self):
        print("class B")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("class C")


x = C()

print("------------------------------------------------------------")  # 60個


class A:
    def __init__(self):
        super().__init__()
        print("class A")


class B:
    def __init__(self):
        super().__init__()
        print("class B")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("class C")


x = C()

print("------------------------------------------------------------")  # 60個

print("ch12_24.py module name = ", __name__)

print("------------------------------------------------------------")  # 60個


def myFun():
    print("__name__ == __main__")


myFun()

print("------------------------------------------------------------")  # 60個


class Name:
    def __init__(self, name):
        self.name = name


a = Name("Hung")
print(a)

print("------------------------------------------------------------")  # 60個


class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


a = Name("Hung")
print(a)

print("------------------------------------------------------------")  # 60個


class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    __repr__ = __str__


a = Name("Hung")
print(a)

print("------------------------------------------------------------")  # 60個


# 定義 Inventory 類別來管理商品庫存
class Inventory:
    # 初始化方法，建立一個空的商品字典
    def __init__(self):
        self.items = {}  # 商品字典，鍵是商品名，值是商品數量

    # 庫存中添加商品,如果商品存在則更新其數量；如果不存在則添加到字典中
    def add_item(self, item, quantity):
        self.items[item] = self.items.get(item, 0) + quantity

    # 庫存中移除商品
    def remove_item(self, item, quantity):
        # 檢查商品是否存在且數量充足，然後從庫存中移除指定數量的商品
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            # 如果商品數量為0，從字典中移除該商品
            if self.items[item] == 0:
                del self.items[item]


# 使用 Inventory 類別來管理庫存
print("建立物件 inventory")
inventory = Inventory()
inventory.add_item("apple", 10)  # 向庫存中添加10個蘋果
inventory.remove_item("apple", 3)  # 從庫存中移除3個蘋果

# 查看庫存的目前狀態
print(inventory.items)  # 輸出：{'apple': 7}

print("------------------------------------------------------------")  # 60個


# 定義 StudentManager 類別來管理學生資料
class StudentManager:
    # 初始化方法, 建立一個空的學生字典
    def __init__(self):
        self.students = {}  # 學生字典,鍵是學生ID,值是學生名字

    # 方法用於添加新學生到字典中
    def add_student(self, id, name):
        self.students[id] = name  # 添加學生

    # 移除指定ID的學生, 檢查學生ID是否存在，如果存在則移除
    def remove_student(self, id):
        if id in self.students:
            del self.students[id]


# 使用 StudentManager 類別來管理學生
print("建立物件 manager")
manager = StudentManager()  # 建立 StudentManager 物件
manager.add_student(1, "Hung")  # 添加學生 Hung
manager.remove_student(1)  # 移除學生ID為 1 的學生

# 用 print(manager.students) 來查看學生字典的當前狀態
print(manager.students)  # 輸出：{}

print("------------------------------------------------------------")  # 60個


class Counter:
    counter = 0  # 類別屬性,可由類別本身調用

    def __init__(self):
        Counter.counter += 1  # 更新指標

    @classmethod
    def show_counter(cls):  # 類別方法,可由類別本身調用
        print("class method")
        print("counter = ", cls.counter)  # 也可使用Counter.counter調用
        print("counter = ", Counter.counter)

print("建立物件 one")
one = Counter()

print("建立物件 two")
two = Counter()

print("建立物件 three")
three = Counter()

Counter.show_counter()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


