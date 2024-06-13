import os
import sys
import time
import random

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
        if self.power=='high':
            return 'Sports'
        # (2) 馬力等級不是高，如果車門數是4，則一定是轎車（Sedan）
        elif self.doors==4:
            return 'Sedan'
        # (3) 剩下的只有轎跑車（Coupe）的可能了！
        else:
            return 'Coupe'
    
car1 = Car(True, 4, 'low')
car2 = Car(False, 2, 'high')
car3 = Car(True, 2, 'median')
car4 = Car(False, 4, 'median')
print('Car1 type:', car1.carType())
print('Car2 type:', car2.carType())
print('Car3 type:', car3.carType())
print('Car4 type:', car4.carType())

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
        return 'Sedan' 
    
class Coupe(Car):
    # 建構式
    def __init__(self, driverSide, doors):
        # 直接設定部份屬性，建構父類別
        super().__init__(driverSide, doors, 'median')
    
    def carType(self):
        return 'Coupe' 

class Sports(Car):
    # 建構式
    def __init__(self, driverSide):
        # 直接設定部份屬性，建構父類別
        super().__init__(driverSide, 2, 'high')
    
    def carType(self):
        return 'Sports' 

# 直接建構各款汽車物件
car1 = Sedan(True, 'low')
car2 = Sports(False)
car3 = Coupe(True, 2)
car4 = Sedan(False, 'median')
print('Car1 type:', car1.carType())
print('Car2 type:', car2.carType())
print('Car3 type:', car3.carType())
print('Car4 type:', car4.carType())



print("------------------------------------------------------------")  # 60個



class Father:
    def __init__(self):
        self.__address = "台北市羅斯福路"

    def getaddr(self):
        return self.__address


class Son(Father):
    pass


hung = Father()
ivan = Son()
print("父類別 : ", hung.getaddr())
print("子類別 : ", ivan.getaddr())

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


class Animals:
    """Animals類別, 這是基底類別"""

    def __init__(self, animal_name, animal_age):
        self.name = animal_name  # 紀錄動物名稱
        self.age = animal_age  # 紀錄動物年齡

    def run(self):  # 輸出動物 is running
        print(self.name.title(), " is running")


class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別"""

    def __init__(self, dog_name, dog_age):
        super().__init__("My pet " + dog_name.title(), dog_age)


mycat = Animals("lucy", 5)  # 建立Animals物件以及測試
print(mycat.name.title(), " is ", mycat.age, " years old.")
mycat.run()

mydog = Dogs("lily", 6)  # 建立Dogs物件以及測試
print(mydog.name.title(), " is ", mydog.age, " years old.")
mydog.run()

print("------------------------------------------------------------")  # 60個


class Animals:
    """Animals類別, 這是基底類別"""

    def __init__(self, animal_name, animal_age):
        self.name = animal_name  # 紀錄動物名稱
        self.age = animal_age  # 紀錄動物年齡

    def run(self):  # 輸出動物 is running
        print(self.name.title(), " is running")


class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別"""

    def __init__(self, dog_name, dog_age):
        super().__init__("My pet " + dog_name.title(), dog_age)

    def sleeping(self):
        print("My pet", "is sleeping")


mycat = Animals("lucy", 5)  # 建立Animals物件以及測試
print(mycat.name.title(), " is ", mycat.age, " years old.")
mycat.run()

mydog = Dogs("lily", 6)  # 建立Dogs物件以及測試
print(mydog.name.title(), " is ", mydog.age, " years old.")
mydog.run()
mydog.sleeping()

print("------------------------------------------------------------")  # 60個


class Grandfather:
    """定義祖父的資產"""

    def __init__(self):
        self.grandfathermoney = 10000

    def get_info1(self):
        print("Grandfather's information")


class Father(Grandfather):  # 父類別是Grandfather
    """定義父親的資產"""

    def __init__(self):
        self.fathermoney = 8000
        super().__init__()

    def get_info2(self):
        print("Father's information")


class Ivan(Father):  # 父類別是Father
    """定義Ivan的資產"""

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


class Father:
    """定義父親的資產"""

    def __init__(self):
        self.fathermoney = 10000


class Ira(Father):  # 父類別是Father
    """定義Ira的資產"""

    def __init__(self):
        self.iramoney = 8000
        super().__init__()


class Ivan(Father):  # 父類別是Father
    """定義Ivan的資產"""

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


class Person:
    def interest(self):
        print("Smiling is my interest")


hung = Person()
hung.interest()

print("------------------------------------------------------------")  # 60個


class Animals:
    """Animals類別, 這是基底類別"""

    def __init__(self, animal_name):
        self.name = animal_name  # 紀錄動物名稱

    def which(self):  # 回傳動物名稱
        return "My pet " + self.name.title()

    def action(self):  # 動物的行為
        return " sleeping"


class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別"""

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


class Grandfather:
    """定義祖父類別"""

    def action1(self):
        print("Grandfather")


class Father(Grandfather):
    """定義父親類別"""

    def action2(self):  # 定義action2()
        print("Father")


class Uncle(Grandfather):
    """定義叔父類別"""

    def action2(self):  # 定義action2()
        print("Uncle")


class Ivan(Father, Uncle):
    """定義Ivan類別"""

    def action3(self):
        print("Ivan")


ivan = Ivan()
ivan.action3()  # 順序 Ivan
ivan.action2()  # 順序 Ivan -> Father
ivan.action1()  # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個


class Grandfather:
    """定義祖父類別"""

    def action1(self):
        print("Grandfather")


class Father(Grandfather):
    """定義父親類別"""

    def action3(self):  # 定義action3()
        print("Father")


class Uncle(Grandfather):
    """定義叔父類別"""

    def action2(self):  # 定義action2()
        print("Uncle")


class Ivan(Father, Uncle):
    """定義Ivan類別"""

    def action4(self):
        print("Ivan")


ivan = Ivan()
ivan.action4()  # 順序 Ivan
ivan.action3()  # 順序 Ivan -> Father
ivan.action2()  # 順序 Ivan -> Father -> Uncle
ivan.action1()  # 順序 Ivan -> Father -> Uncle -> Grandfather

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


class Grandfather:
    """定義祖父類別"""

    pass


class Father(Grandfather):
    """定義父親類別"""

    pass


class Ivan(Father):
    """定義Ivan類別"""

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


class Grandfather:
    """定義祖父類別"""

    pass


class Father(Grandfather):
    """定義父親類別"""

    pass


class Ivan(Father):
    """定義Ivan類別"""

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


class Myclass:
    """文件字串實例
    Myclass類別的應用"""

    def __init__(self, x):
        self.x = x

    def printMe(self):
        """文字檔字串實例
        Myclass類別內printMe方法的應用"""
        print("Hi", self.x)


data = Myclass(100)
data.printMe()
print(data.__doc__)  # 列印Myclass文件字串docstring
print(data.printMe.__doc__)  # 列印printMe文件字串docstring

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


class City:
    def __init__(self, name):
        self.name = name

    def equals(self, city2):
        return self.name.upper() == city2.name.upper()


one = City("Taipei")
two = City("taipei")
three = City("myhome")
print(one.equals(two))
print(one.equals(three))

print("------------------------------------------------------------")  # 60個


class City:
    def __init__(self, name):
        self.name = name

    def __eq__(self, city2):
        return self.name.upper() == city2.name.upper()


one = City("Taipei")
two = City("taipei")
three = City("myhome")
print(one == two)
print(one == three)

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
inventory = Inventory()  # 建立 Inventory 物件
inventory.add_item("apple", 10)  # 向庫存中添加10個蘋果
inventory.remove_item("apple", 3)  # 從庫存中移除3個蘋果

# 查看庫存的目前狀態
print(inventory.items)  # 輸出：{'apple': 7}

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
car = Vehicle("Lexus", "ES 300h", 2025)  # 建立一個 Vehicle 對象
info = car.get_info()  # get_info方法獲取車輛資料
print(info)  # 輸出：'2025 ES 300h'

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
manager = StudentManager()  # 建立 StudentManager 物件
manager.add_student(1, "Hung")  # 添加學生 Hung
manager.remove_student(1)  # 移除學生ID為 1 的學生

# 用 print(manager.students) 來查看學生字典的當前狀態
print(manager.students)  # 輸出：{}

print("------------------------------------------------------------")  # 60個


class Score:
    def __init__(self, score):
        self.score = score


stu = Score(50)
print(stu.score)
stu.score = 100
print(stu.score)

print("------------------------------------------------------------")  # 60個


class Score:
    def __init__(self, score):
        self.__score = score

    def getscore(self):
        print("inside the getscore")
        return self.__score

    def setscore(self, score):
        print("inside the setscore")
        self.__score = score


stu = Score(0)
print(stu.getscore())
stu.setscore(80)
print(stu.getscore())

print("------------------------------------------------------------")  # 60個


class Score:
    def __init__(self, score):
        self.__score = score

    def getscore(self):
        print("inside the getscore")
        return self.__score

    def setscore(self, score):
        print("inside the setscore")
        self.__score = score

    sc = property(getscore, setscore)  # Python 風格


stu = Score(0)
print(stu.sc)
stu.sc = 80
print(stu.sc)

print("------------------------------------------------------------")  # 60個


class Score:
    def __init__(self, score):
        self.__score = score

    @property
    def sc(self):
        print("inside the getscore")
        return self.__score

    @sc.setter
    def sc(self, score):
        print("inside the setscore")
        self.__score = score


stu = Score(0)
print(stu.sc)
stu.sc = 80
print(stu.sc)

print("------------------------------------------------------------")  # 60個


class Square:
    def __init__(self, sideLen):
        self.__sideLen = sideLen

    @property
    def area(self):
        return self.__sideLen**2


obj = Square(10)
print(obj.area)

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


one = Counter()
two = Counter()
three = Counter()
Counter.show_counter()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
