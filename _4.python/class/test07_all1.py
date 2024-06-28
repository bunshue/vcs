import sys

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


# 產生物件
car1 = Motor()  # 物件1
car1.showMessage()  # 呼叫方法
car1.setupCar("Vios", "極光藍")
car1.showMessage()  # 呼叫方法

car2 = Motor()  # 物件2
car2.showMessage()
car2.setupCar("Altiss", "炫魅紅")
car2.showMessage()

print("打印物件訊息, 使用__repr__")
print(car1)
print(car2)

print("------------------------------------------------------------")  # 60個


# 建立類別，產生物件能以不同再別做存取
class Student:
    def message(self, name):  # 方法一
        self.data = name

    def showMessage(self):  # 方法二
        print(self.data)


s1 = Student()  # 第一個物件
s1.message("James McAvoy")  # 呼叫方法時傳入字串
s1.showMessage()
s2 = Student()  # 第二個物件
s2.message(78.566)  # 呼叫方法時傳入浮點數值
s2.showMessage()

print("------------------------------------------------------------")  # 60個


# 宣告類別
class student:
    def score(self, s1, s2, s3):
        return (s1 + s2 + s3) / 3


# 產生物件
vicky = student()
# 呼叫score()方法並傳入引數
average = vicky.score(98, 65, 81)
print(f"Vicky 平均分數：{average:.3f}")


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


# 產生物件
x = newClass("")
print()
y = newClass("Second")


print("------------------------------------------------------------")  # 60個


# 產生父類別 或稱 基礎類別
class Father:
    def walking(self):
        print("父類別之函數 AAAAA")


# 產生子類別 或稱 衍生類別
class Son(Father):
    pass
    """同名的函數，若有，則使用子類別之函數
    def walking(self):
        print("子類別之函數 BBBBB")
    """

print('產生子類別實體 - 即物件')
Joe = Son()

print('呼叫函數，繼承自父類別的函數')
Joe.walking()


print("------------------------------------------------------------")  # 60個


# 類和繼承
class Plant():
    def __init__(self, name):
        self.name = name
    def show(self):
        print("plant", self.name)

p = Plant('banana')
p.show()

#plant banana

class Fruit(Plant):
    def show(self):
        print("fruit", self.name)
f = Fruit('banana')
f.show()

#fruit banana


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

class Person:
    def __init__(self, name, birthyear):
        self._name = name
        self._birthyear = birthyear

    def get_birthyear(self):
        return self._birthyear     # 讀取資料成員

    def set_birthyear(self, v):
        self._birthyear = v        # 寫入資料成員

    def del_birthyear(self):
        del self._birthyear        # 刪除資料成員

    birthyear = property(get_birthyear, set_birthyear, del_birthyear)
    # 設定為屬性存取方法

p1 = Person('約翰', 1985)
print(p1.birthyear)
p1.birthyear = 1988
print(p1.birthyear)
del p1.birthyear
#print(p1.birthyear)        # AttributeError    已刪除, 不可用

print("------------------------------------------------------------")  # 60個

class Student:
    name = 'unknown' # class attribute
    def __init__(self):
        self.age = 20  # instance attribute

    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=', cls.name)

    @classmethod
    def tostring2(cls):
        print('Student Class Attributes: name=', cls.name, ', age=', cls.age)

Student.tostring()           # 輸出"Student Class Attributes: name= unknown"
stu1 = Student()
stu1.tostring()              # 相同輸出，物件也可以呼叫類別方法

print("------------------------------------------------------------")  # 60個

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):    # 讓加法運算子"+"動得起來
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1+p2)        # (3, 5)

print("------------------------------------------------------------")  # 60個


# 定義DOG類別
class DOG:    
    # 建構式！
    def __init__(self, breed, size, age, color):
        self.Breed = breed
        self.Size = size
        self.Age = age
        self.Color = color

    # Eat方法
    def Eat(self):
        print("I am a "+self.Breed+", now I'm eating.")
        
    # Sleep方法
    def Sleep(self):
        print("I am a "+self.Breed+", now I'm sleeping.")
        
    # Sit方法
    def Sit(self):
        print("I am a "+self.Breed+", now I'm sitting.")
    
    # Run方法
    def Run(self):
        print("I am a "+self.Breed+", now I'm running.")
        
    # __str__方法，將物件用字串表達
    def __str__(self):
        return "I am a "+self.Breed+", I'm "+str(self.Age)+ \
                " years old, my body size is "+self.Size+ \
                " and my color is "+self.Color+"."
        

# 實體化第一隻狗
dog1 = DOG("Neapolitan Mastiff", "Large", 5, "Black")
print(dog1)
dog1.Eat()     # 吃
dog1.Sleep()   # 睡

# 實體化第二隻狗
dog2 = DOG("Maltese", "Small", 2, "White")
print(dog2)
dog2.Sleep()   # 睡
dog2.Sit()     # 坐

# 實體化第三隻狗
dog3 = DOG("Chow Chow", "Medium", 3, "Brown")
print(dog3)
dog3.Sit()     # 坐
dog3.Run()     # 跑

print("------------------------------------------------------------")  # 60個


class CoffeeMaker:
    
    def __init__(self):
        self.power = False     # 初始化咖啡機電源：關
        self.waterTemp = 20    # 室溫水的溫度，攝氏20度
        
    def switchPower(self):
        self.power = ~self.power  # 切換開關就是這樣做的！
        
    def getWaterTemp(self):
        return self.waterTemp  # 回傳咖啡機水溫
    
    def heatWater(self):
        # 將水加熱到可沖咖啡的溫度：攝氏90度
        print('正在加熱水溫')
        self.waterTemp = 90
        print('完成！')
        
    def brewCoffee(self):
        if self.power:         # 一切要咖啡機開了才可以！
            print('開始沖泡咖啡...')
            if self.waterTemp<90:
                print('水溫不足')
                self.heatWater()  # 呼叫物件方法，加熱水溫
            print('沖泡咖啡...')
            print('完成！')
        else:
            print('未開機')
        
cm1 = CoffeeMaker()    # 咖啡機一號出現了！
cm1.brewCoffee()       # 直接沖咖啡？能沖才有鬼
cm1.switchPower()      # 先開電源，正解
cm1.brewCoffee()       # 順利沖咖啡了！

print("------------------------------------------------------------")  # 60個

print('繼承')

class A:       # 沒有標示繼承，預設繼承object
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('A init:', x, ',', y)
        
class B(A):    # B繼承A，A繼承object
    def __init__(self, x, y, z):
        # super()的意思是先執行好父類別的建構工作
        #super().__init__(x, y)
        super(B, self).__init__(x, y)
        self.z = z
        print('B init:', x, ',', y, ',', z)
        
b = B(1, 2, 3)
a = A(4, 5)


print("------------------------------------------------------------")  # 60個

print('繼承')
class Animal():
    def shout(self):
        print('動物吼')

class Dog(Animal):
    def shout(self):     # 覆寫Animal的shout
        print('汪！')

class Cat(Animal):
    def shout(self):     # 覆寫Animal的shout
        print('喵～')


dog1 = Dog()
cat1 = Cat()
dog1.shout()
cat1.shout()

print("------------------------------------------------------------")  # 60個

print('繼承')
class A:
    def __init__(self):
        self.x = 3
        self.__pi = 3.14

class B(A):
    def bar(self):
        # return self.__pi 這樣寫會錯！！
        return self._A__pi   # 會被改成_A__pi

b1 = B()

print(b1.bar())      # 3.14

print("------------------------------------------------------------")  # 60個

print('兩棲動物')

class Vehicle:
    def __init__(self):
        print('Vehicle-start')
        print('Vehicle-done')

class WheeledVehicle(Vehicle):
    def __init__(self):
        print('WheeledVehicle-start')
        super().__init__()
        print('WheeledVehicle-done')

class WaterVehicle(Vehicle):
    def __init__(self):
        print('WaterVehicle-start')
        super().__init__()
        print('WaterVehicle-done')

class Amphibian(WheeledVehicle, WaterVehicle):
    def __init__(self):
        print('Amphibian-start')
        super().__init__()
        print('Amphibian-done')

amphibian = Amphibian()

Amphibian.mro()

print("------------------------------------------------------------")  # 60個

class Bird:          # 父類別
    def fly(self):
        print("大多數鳥能飛翔")
    
    def swim(self):
        print("少部份鳥能游水")
    
    def display(self):
        print("我是鳥類")

class Parrot(Bird):  # 繼承Bird
    def fly(self):   # 覆寫方法
        print("鸚鵡能飛翔")
    
    def swim(self):  # 覆寫方法
        print("鸚鵡不能游水")

class Penguin(Bird): # 繼承Bird
    def fly(self):   # 覆寫方法
        print("企鵝不能飛翔")
    
    def swim(self):  # 覆寫方法
        print("企鵝能游水")

# 共同介面
def flying_test(bird):
    bird.fly()
    
def display_test(bird):
    bird.display()

# 建立物件實例
p1 = Parrot()
p2 = Penguin()

# 傳入物件測試
flying_test(p1)
flying_test(p2)

# 傳入物件測試
display_test(p1)
display_test(p2)

print("------------------------------------------------------------")  # 60個

# 定義ANIMAL類別
class ANIMAL:    
    # 建構式！
    def __init__(self, age, color):
        self.Age = age
        self.Color = color
        
    # __str__方法，將物件用字串表達
    def __str__(self):
        return "I'm "+str(self.Age)+" years old, my color is "+ \
                self.Color

# 定義DOG類別，繼承ANIMAL類別哦！
class DOG(ANIMAL):    
    # 建構式！
    def __init__(self, breed, size, age, color):
        super().__init__(age, color)
        self.Breed = breed
        self.Size = size

    # Eat方法
    def Eat(self):
        print("I am a "+self.Breed+", now I'm eating.")
        
    # Sleep方法
    def Sleep(self):
        print("I am a "+self.Breed+", now I'm sleeping.")
        
    # Sit方法
    def Sit(self):
        print("I am a "+self.Breed+", now I'm sitting.")
    
    # Run方法
    def Run(self):
        print("I am a "+self.Breed+", now I'm running.")
        
    # __str__方法，將物件用字串表達
    def __str__(self):
        return "I am a "+self.Breed+", my body size is "+self.Size+ \
                ", "+super().__str__()+"."
        

# 實體化第一隻狗
dog1 = DOG("Neapolitan Mastiff", "Large", 5, "Black")
print(dog1)
dog1.Eat()     # 吃
dog1.Sleep()   # 睡

# 實體化第二隻狗
dog2 = DOG("Maltese", "Small", 2, "White")
print(dog2)
dog2.Sleep()   # 睡
dog2.Sit()     # 坐

# 實體化第三隻狗
dog3 = DOG("Chow Chow", "Medium", 3, "Brown")
print(dog3)
dog3.Sit()     # 坐
dog3.Run()     # 跑
print("------------------------------------------------------------")  # 60個

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


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


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


