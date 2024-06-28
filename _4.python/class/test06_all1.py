import os
import sys
import time
import random

import sys
print("Class測試")

class animalBaseClass:
        def __init__(self, num):
                self.animallegs = num
        def walk(self):
                print('走動')
        def cry(self):
                print('吼叫')
        def getLegsNum(self):
                print(self.animallegs)

class dogClass(animalBaseClass):
        def __init__(self, num):
                parent_class = super(dogClass, self)
                parent_class.__init__(num)
                print('我是小狗')

class birdClass(animalBaseClass):
        def __init__(self, num):
                parent_class = super(birdClass, self)
                parent_class.__init__(num)
                print('我是小鳥')
        def cry(self):
                print('啾啾')

class snakeClass(animalBaseClass):
        def __init__(self, num):
                parent_class = super(snakeClass, self)
                parent_class.__init__(num)
                print('我是蛇')

wanko = dogClass(4)
wanko.walk()
wanko.cry()
wanko.getLegsNum()

piyo_suke = birdClass(2)
piyo_suke.walk()
piyo_suke.cry()
piyo_suke.getLegsNum()

nyoro = snakeClass(0)
nyoro.walk()
nyoro.cry()
nyoro.getLegsNum()



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

# Python 新進測試 13

print("求面積")

class Rectangle():       #定義父類別  
    def __init__(self, width,height):
        self.width = width    #定義共用屬性   
        self.height = height  #定義共用屬性
    def area(self):           #定義共用方法 
        return self.width * self.height
        
class Triangle(Rectangle): #定義子類別  
    def area2(self):       #定義子類別的共用方法 
        return (self.width * self.height)/2
     
triangle = Triangle(5,6) #建立 triangle 物件
print("矩形面積=",triangle.area())    #30
print("三角形面積=",triangle.area2()) #15


print("------------------------------------------------------------")  # 60個

print("Class測試")

class fruit:
	color = 'red'
	def taste(self):
		return 'delicious'
apple = fruit()
cc = apple.color
print(cc)

cc = apple.taste() 
print(cc)

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

import sys

print('------------------------------------------------------------')	#60個


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

# 使用類別建立物件
s1 = Student("陳會安", 90)
s1.displayStudent()  # 呼叫方法
print("s1.whoami(): ", s1.whoami())
# 存取資料欄位
print("s1.name: ", s1.name)
print("s1.grade: ", s1.grade)

print('------------------------------------------------------------')	#60個


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

# 使用類別建立物件
s1 = Student("陳會安")
print(s1.getCount(), s1.getName())
s2 = Student("陳允傑")
print(s2.getCount(), s2.getName())
s3 = Student("江小魚")
print(s3.getCount(), s3.getName())
print("學生數: ", Student.count)



print('------------------------------------------------------------')	#60個

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
        
# 使用類別建立物件
v1 = Vehicle("BMW")
v1.displayVehicle()  # 呼叫方法
c1 = Car("Ford", "GT350")
c1.displayVehicle()  # 呼叫方法


print('------------------------------------------------------------')	#60個


class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'       # 定義屬性
    def motto(self):            # 定義方法
        return "以客為尊"

userbank = Banks()              # 定義物件userbank
print("目前服務銀行是 ", userbank.title)
print("銀行服務理念是 ", userbank.motto())





print('------------------------------------------------------------')	#60個



class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

def adapt_point(point):
    return "%f;%f" % (point.x, point.y)


p1 = Point(4.0, -3.2)

p2 = Point(8.0, 1.2)

print(adapt_point(p1))
print(adapt_point(p2))


print('------------------------------------------------------------')	#60個


class NannyNag(Exception):
    def __init__(self, lineno, msg, line):
        self.lineno, self.msg, self.line = lineno, msg, line
    def get_lineno(self):
        return self.lineno
    def get_msg(self):
        return self.msg
    def get_line(self):
        return self.line

nag = NannyNag(123, 'kkk', 456)
badline = nag.get_lineno()
line = nag.get_line()

print("%r: *** Line %d: trouble in tab city! ***" % ('dddd', badline))
print("offending line: %r" % (line,))

print(nag.get_msg())
print('dddd', badline, repr(line))


print('------------------------------------------------------------')	#60個



print('建一個測試list')

class User:
    user_id: int
    first_name: str
    last_name: str

USERS = [(i, f"first_name_{i}", f"last_name_{i}") for i in range(2_0)]

print(type(USERS))
print(USERS)


def show_price(price: float) -> str:
    return "$ {0:,.2f}".format(price)


print(show_price(1000))
#    '$ 1,000.00'

print(show_price(1_250.75))
#    '$ 1,250.75'



print('------------------------------------------------------------')	#60個



print('測試hasattr功能')
print('內建函數 (function) hasattr() ，判斷參數 (parameter) name 是否為 object 的屬性名稱')

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

print(hasattr(d, "t"))  #不是
print(hasattr(d, "u"))  #不是
print(hasattr(d, "v"))  #不是
print(hasattr(d, "w"))  #不是
print(hasattr(d, "x"))  #是
print(hasattr(d, "y"))  #是
print(hasattr(d, "z"))  #是


print('------------------------------------------------------------')	#60個


import sys

print('------------------------------------------------------------')	#60個

class fruit:
	color = 'red'
	def taste(self):
		return 'delicious'

apple = fruit()
apple.color 
apple.taste() 

print('------------------------------------------------------------')	#60個

'''
class staff:
	def salary():
		return "10000元"

yamamoto = staff()
yamamoto.salary()
'''

print('------------------------------------------------------------')	#60個

class staff:
	def salary(self):
		return "10000元"

yamamoto = staff()
yamamoto.salary()

print('------------------------------------------------------------')	#60個

'''
class staff:
	bonus = 30000
	def salary(self):
		salary = 10000 + bonus
		return salary

yamamoto = staff()
yamamoto.salary()
'''

print('------------------------------------------------------------')	#60個

class staff:
	bonus = 30000
	def salary(self):
		salary = 10000 + self.bonus
		return salary

yamamoto = staff()
yamamoto.salary()

print('------------------------------------------------------------')	#60個

class staff:
	def __init__(self, bonus):
		self.bonus = bonus
	def salary(self):
		salary = 10000 + self.bonus
		return salary

yamamoto = staff(50000)
yamamoto.salary()

print('------------------------------------------------------------')	#60個

class animalBaseClass:
	animallegs = 4
	def walk(self):
		print('走動')
	def cry(self):
		print('吼叫')
	def getLegsNum(self):
		print(self.animallegs)

class dogClass(animalBaseClass):
	def __init__(self):
		print('我是小狗')

wanko = dogClass()
wanko.walk()
wanko.cry()
wanko.getLegsNum()

print('------------------------------------------------------------')	#60個

class animalBaseClass:
	animallegs = 2
	def walk(self):
		print('走動')
	def cry(self):
		print('吼叫')

class birdClass(animalBaseClass):
	def __init__(self):
		print('我是小鳥')
	def cry(self):
		print('啾啾')

piyo_suke = birdClass()
piyo_suke.walk()
piyo_suke.cry()

print('------------------------------------------------------------')	#60個

class animalBaseClass:
	def __init__(self, num):
		self.animallegs = num
	def walk(self):
		print('走動')
	def cry(self):
		print('吼叫')
	def getLegsNum(self):
		print(self.animallegs)

class snakeClass(animalBaseClass):
	def __init__(self, num):
		parent_class = super(snakeClass, self)
		parent_class.__init__(num)
		print('我是蛇')

nyoro = snakeClass(0)
nyoro.getLegsNum()

print('------------------------------------------------------------')	#60個

class snakeClass(animalBaseClass):
	def __init__(self):
		snake_leg = 0 
		parent_class = super(snakeClass, self)
		parent_class.__init__( snake_leg)
		print('我是蛇')

nyoro = snakeClass()
nyoro.getLegsNum()




print('------------------------------------------------------------')	#60個


'''
# 其他

'''


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def info(self):
        return (self.x, self.y)
if __name__ == '__main__':    
    a = shape(100, 200)
    b = shape(200, 300)
    print(a.info())
    print(b.info())
    

print('------------------------------------------------------------')	#60個


class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def info(self):
        return (self.x, self.y)
    
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

if __name__ == '__main__':
    a = shape(100, 200)
    b = shape(200, 300)
    c = circle(100, 200, 50)
    d = rectangle(100, 200, 50, 50)
    shapes = [a, b, c, d]
    for s in shapes:
        print(s.info())
        
print('------------------------------------------------------------')	#60個

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

if __name__ == '__main__':
    d = rectangle(100, 200, 50, 50)
    print(d.info())
    print("往x前進50點，y後退20點")
    d.move(50, -20)
    print(d.info())
    


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


import random
class poker():
    def __init__(self):
        self.deck = [i for i in range(52)]
        random.shuffle(self.deck)
        self.card_type = ['黑桃', '紅心', '梅花', '方塊']
        self.index = 0
    
    def decode(self, card):
        suit = self.card_type[card // 13]
        no = card % 13 + 1
        if no == 1:
            no = 'A'
        elif no > 10:
            no = chr((no - 11) + ord('J'))
        return (suit, str(no))
        
    def showAll(self):
        for card in self.deck:
            print(self.decode(card), end='')
        print()
    
    def dealFive(self):
        for i in range(5):
            print(self.decode(self.deck[self.index]), end='')
            self.index += 1
        print()
    
    def oneMore(self):
        print(self.decode(self.deck[self.index]), end='')
        self.index += 1
        print()
    
    def shuffle(self):
        random.shuffle(self.deck)
        self.index = 0

if __name__ == '__main__':
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

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



'''


'''


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

class Animals1():
    """Animals1類別, 這是基底類別 """
    def __init__(self, animal_name, animal_age ):
        self.name = animal_name # 紀錄動物名稱
        self.age = animal_age   # 紀錄動物年齡

    def run(self):              # 輸出動物 is running
        print(self.name.title(), " is running")

class Dogs(Animals1):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet ' + dog_name.title(), dog_age)
    def sleeping(self):
        print("My pet", "is sleeping")

mycat = Animals1('lucy', 5)      # 建立Animals1物件以及測試
print(mycat.name.title(), ' is ', mycat.age, " years old.")
mycat.run()

mydog = Dogs('lily', 6)         # 建立Dogs物件以及測試
print(mydog.name.title(), ' is ', mydog.age, " years old.")
mydog.run()
mydog.sleeping()

print('------------------------------------------------------------')	#60個


class Animals2():
    """Animals2類別, 這是基底類別 """
    def __init__(self, animal_name):
        self.name = animal_name         # 紀錄動物名稱
    def which(self):                    # 回傳動物名稱
        return 'My pet ' + self.name.title()
    def action(self):                   # 動物的行為
        return ' sleeping'

class Dogs(Animals2):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name):       # 紀錄動物名稱
        super().__init__(dog_name.title())
    def action(self):                   # 動物的行為
        return ' running in the street'

class Monkeys():
    """猴子類別, 這是其他類別 """
    def __init__(self, monkey_name):    # 紀錄動物名稱
        self.name = 'My monkey ' + monkey_name.title()
    def which(self):                    # 回傳動物名稱
        return self.name
    def action(self):                   # 動物的行為
        return ' running in the forest'
    
def doing(obj):                         # 列出動物的行為
    print(obj.which(), "is", obj.action())
    
my_cat = Animals2('lucy')                # Animals2物件
doing(my_cat)
my_dog = Dogs('gimi')                   # Dogs物件
doing(my_dog)
my_monkey = Monkeys('taylor')           # Monkeys物件
doing(my_monkey)

print("------------------------------------------------------------")  # 60個

class Book:
    #定義方法一：取得書籍名稱和價格
    def setInfo(self, title, price):
        self.title = title
        self.price = price
    #定義方法二：輸出書籍名稱和價格
    def showInfo(self):
        print('書籍名稱:{0:6s}, 價格:{1:4s}元'.format(
            self.title, self.price))
# 產生物件
book1=Book()#物件1
book1.setInfo('Python一週速成', '360')
book1.showInfo() #呼叫方法
book2=Book()#物件2
book2.setInfo('網路行銷與社群行銷', '520')
book2.showInfo()

print("------------------------------------------------------------")  # 60個

class Tom():#父類別
    def __init__(self):
        self.height1=178

class Andy(Tom):#父類別是Tom
    def __init__(self):
        self.height2=180
        super().__init__()

class Michael(Tom):#父類別是Tom
    def __init__(self):
        self.height3=185
        super().__init__()
    def display(self):
        print('父親Tom的身高:', self.height1,'公分')
        print('兄弟Andy的身高:', Andy().height2,'公分')
        print('自己Michael的身高:', m1.height3,'公分')

m1=Michael()
m1.display()

print("------------------------------------------------------------")  # 60個

class Book:
    #定義方法一：取得書籍名稱和價格
    def setData(self, title, price):
        self.title = title
        self.price = price
    #定義方法二：輸出書籍名稱和價格
    def showData(self):
        print('書籍名稱:{0:6s}, 價格:{1:4s}'.format(
            self.title, self.price))

print("------------------------------------------------------------")  # 60個

#此程式單純類別定義,沒有任何輸出到螢幕的執行結果
class Company: #定義公司類別
    name='賺大錢有限公司'
    def slogan(self):
        print('優良品質 創新研發 強力行銷')

print("------------------------------------------------------------")  # 60個

class Date:
    def setDate(self,birthday): #第一種方法
        self.birthday =birthday
    def showDate(self): #第二種方法
        print("出生年月日:",self.birthday)
d1 = Date()#第一個物件
d1.setDate("民國67年7月3日")#呼叫方法時傳入字串
d1.showDate()
d2 = Date()#第二個物件
d2.setDate([67,7,3])#呼叫方法時傳入串列

print("------------------------------------------------------------")  # 60個

class Wage:
	def __init__(self, fee=200, hour=80):
		self.fee=fee
		self.hour=hour

	def getArea(self):
		return self.fee* self.hour

tom=Wage()
print("透過init()方法預設值的總薪資: ",tom.getArea(),"元")

jane= Wage(250,100)
print("透過init()方法傳入參數的總薪資: ",jane.getArea(),"元")

print("------------------------------------------------------------")  # 60個

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature3(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature4(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

#產生子類別實體
tiger = Animal()
daniel= Human()
goldfish=Fish()
alice = Mermaid()
print("tiger是屬於Animal類別:",isinstance(tiger,Animal))
print("daniel是屬於Animal類別:",isinstance(daniel,Animal))
print("goldfish是屬於Animal類別:",isinstance(goldfish,Animal))
print("alice是屬於Animal類別:",isinstance(alice,Animal))
print("===============================================")
print("tiger是屬於Human類別:",isinstance(tiger,Human))
print("daniel是屬於Human類別:",isinstance(daniel,Human))
print("goldfish是屬於Human類別:",isinstance(goldfish,Human))
print("alice是屬於Human類別:",isinstance(alice,Human))
print("===============================================")
print("tiger是屬於Fish類別:",isinstance(tiger,Fish))
print("daniel是屬於Fish類別:",isinstance(daniel,Fish))
print("goldfish是屬於Fish類別:",isinstance(goldfish,Fish))
print("alice是屬於Fish類別:",isinstance(alice,Fish))
print("===============================================")
print("tiger是屬於Mermaid類別:",isinstance(tiger,Mermaid))
print("daniel是屬於Mermaid類別:",isinstance(daniel,Mermaid))
print("goldfish是屬於Mermaid類別:",isinstance(goldfish,Mermaid))
print("alice是屬於Mermaid類別:",isinstance(alice,Mermaid))

print("------------------------------------------------------------")  # 60個

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature3(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature4(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

print("Mermaid是屬於Fish子類別:",issubclass(Mermaid,Fish))
print("Mermaid是屬於Human子類別:",issubclass(Mermaid,Human))
print("Mermaid是屬於Animal子類別:",issubclass(Mermaid,Animal))

print("------------------------------------------------------------")  # 60個

#多重繼承範例1

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature2(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature3(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

#產生子類別實體
alice = Mermaid()
alice.feature1()
alice.feature2()
alice.feature3()

print("------------------------------------------------------------")  # 60個

#多重繼承範例2

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature3(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature4(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

#產生子類別實體
alice = Mermaid()
alice.feature1()
alice.feature2()
alice.feature3()
alice.feature4()

print("------------------------------------------------------------")  # 60個

#子類別覆寫父類別的方法
class Normal(): #父類別
    def subsidy(self, income):
        self.money = income
        if self.money >= 500000:
            print('小康家庭補助金額：', end = ' ')
            return 5000
        
class Poor(Normal): #子類別
    def subsidy(self, income): #覆寫subsidy方法
        self.money = income
        if self.money < 300000:
            print('中低收入家庭補助金額：', end = ' ')
            return 10000

student1 = Normal()#建立父類別物件
print(student1.subsidy(780000),'元')

student2 = Poor()#建立子類別物件
print(student2.subsidy(250000),'元')

print("------------------------------------------------------------")  # 60個

#多型實作
class Colleague(): #父類別
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def bonus(self):
        return self.income
    
    def title(self):
        return self.name
    
class Manager(Colleague):#子類別
    def bonus(self):        
        return self.income * 1.5
    
class Director(Colleague): #子類別
    def bonus(self):
        return self.income * 1.2
print('===============================')
obj1 = Colleague('一般性員工', 50000) #父類別物件
print('{:8s} 紅利 {:,}'.format(obj1.title(), obj1.bonus()))

print('===============================')
obj2 = Manager('經理級年終', 80000) #子類別物件
print('{:8s} 紅利 {:,}'.format(obj2.title(), obj2.bonus()))

print('===============================')
obj3 = Director('芏任級年終', 65000) #子類別物件
print('{:8s} 紅利 {:,}'.format(obj3.title(), obj3.bonus()))
print('===============================')

print("------------------------------------------------------------")  # 60個

class Wage:
    def __init__(self, h=80):
        self.__hour=h
    def getHour(self):
        return self.__hour
    def pay(self):
        return hour_fee*self.__hour

hour_fee=200
obj1=Wage(100)
print("每小時基本工資為:",hour_fee,"元")
print("總共工作的小時數:", obj1.getHour())
print("要付給這位工讀生的薪水總額:", obj1.pay(),"元")

print("------------------------------------------------------------")  # 60個

class MobilePhone: #基礎類別
    def touch(self):
        print('我能提供螢幕觸控操作的功能')
        
class HTC(MobilePhone): #衍生類別
    pass

#產生子類別實體
u11 = HTC()
u11.touch()

print("------------------------------------------------------------")  # 60個

class MobilePhone: #基礎類別
    def touch(self):
        print('我能提供螢幕觸控操作的功能')
        
class HTC(MobilePhone): #衍生類別
    def touch(self):
        MobilePhone.touch(self)
        print('我也能提供多點觸控的操作方式')

#產生子類別實體
u11 = HTC()
u11.touch()

print("------------------------------------------------------------")  # 60個

#在子類別呼叫父類別方法—使用super()函式

class Weekday(): #父類別
    def display(self, pay):
        self.price=pay
        print('歡迎來購物')
        print('購買總金額{:,}'.format(self.price))
        
class Holiday(Weekday): #子類別
    def display(self, pay): #覆寫display方法        
        super().display(pay)
        if self.price >= 15000:            
            self.price *= 0.8
        else:
            self.price        
        print('8折 {:,}'.format(self.price))
        
monday = Weekday()#父類別物件
monday.display(25000)

Christmas = Holiday()#子類別物件
Christmas.display(18000)

print("------------------------------------------------------------")  # 60個

#__init__()方法呼叫super()

class Animal():#父類別
    def __init__(self):
        print('我屬於動物類別')
        
class Human(Animal): #子類別
    def __init__(self, name):
        super().__init__()
        print('我也屬於人類類別')

man = Human('黃種人')#子類別實體

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
hungbank.get_balance()                      # 獲得存款餘額                
hungbank.save_money(300)                    # 存款300元
hungbank.get_balance()                      # 獲得存款餘額
hungbank.withdraw_money(200)                # 提款200元
hungbank.get_balance()                      # 獲得存款餘額

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
johnbank = Banks('john', 300)               # 定義物件johnbank
hungbank.get_balance()                      # 獲得hung存款餘額                
johnbank.get_balance()                      # 獲得john存款餘額
hungbank.save_money(100)                    # hung存款100
johnbank.withdraw_money(150)                # john提款150
hungbank.get_balance()                      # 獲得hung存款餘額                
johnbank.get_balance()                      # 獲得john存款餘額

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = 0                    # 設定開戶金額是0
        self.title = "Taipei Bank"          # 設定銀行名稱

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung')                    # 定義物件hungbank
print("目前開戶銀行 ", hungbank.title)      # 列出目前開戶銀行
hungbank.get_balance()                      # 獲得hung存款餘額                
hungbank.save_money(100)                    # hung存款100
hungbank.get_balance()                      # 獲得hung存款餘額                

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = 0                    # 設定開戶金額是0
        self.title = "Taipei Bank"          # 設定銀行名稱

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung')                    # 定義物件hungbank
hungbank.get_balance()
hungbank.balance = 10000                    # 類別外直接竄改存款餘額
hungbank.get_balance()

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

hungbank = Banks('hung')                    # 定義物件hungbank
hungbank.get_balance()
hungbank.balance = 10000                    # 類別外直接竄改存款餘額
hungbank.get_balance()

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))
        
hungbank = Banks('hung')                    # 定義物件hungbank
usdallor = 50
print(usdallor, " 美金可以兌換 ", hungbank.usa_to_taiwan(usdallor), " 台幣") 

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

class Shilin_Banks(Banks):
    # 定義士林分行
    pass
       
hungbank = Shilin_Banks('hung')             # 定義物件hungbank
hungbank.save_money(500)
hungbank.get_balance()

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   # 獲得銀行名稱
        return self.__title

class Shilin_Banks(Banks):
    # 定義士林分行
    pass

hungbank = Shilin_Banks('hung')             # 定義物件hungbank
print("我的存款銀行是: ", hungbank.bank_title())

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.title = "Taipei Bank"          # 設定公有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   # 獲得銀行名稱
        return self.title

class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.title = "Taipei Bank - Shilin Branch"  # 定義分行名稱

jamesbank = Banks('James')                  # 定義Banks類別物件
print("James's banks = ", jamesbank.title)  # 列印銀行名稱
hungbank = Shilin_Banks('Hung')             # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.title)   # 列印銀行名稱

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__title = "Taipei Bank"        # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   # 獲得銀行名稱
        return self.__title

class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.title = "Taipei Bank - Shilin Branch"  # 定義分行名稱
    def bank_title(self):                   # 獲得銀行名稱
        return self.title

jamesbank = Banks('James')                  # 定義Banks類別物件
print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
hungbank = Shilin_Banks('Hung')             # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.bank_title())   # 列印銀行名稱

print("------------------------------------------------------------")  # 60個

class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name, animal_age ):
        self.name = animal_name # 紀錄動物名稱
        self.age = animal_age   # 紀錄動物年齡

    def run(self):              # 輸出動物 is running
        print(self.name.title(), " is running")

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet ' + dog_name.title(), dog_age)

mycat = Animals('lucy', 5)      # 建立Animals物件以及測試
print(mycat.name.title(), ' is ', mycat.age, " years old.")
mycat.run()

mydog = Dogs('lily', 6)         # 建立Dogs物件以及測試
print(mydog.name.title(), ' is ', mydog.age, " years old.")
mydog.run()

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父的資產 """
    def __init__(self):
        self.grandfathermoney = 10000
    def get_info1(self):
        print("Grandfather's information")

class Father(Grandfather):      # 父類別是Grandfather
    """ 定義父親的資產 """
    def __init__(self):
        self.fathermoney = 8000
        super().__init__()
    def get_info2(self):
        print("Father's information")

class Ivan(Father):             # 父類別是Father
    """ 定義Ivan的資產 """
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()
    def get_info3(self):
        print("Ivan's information")
    def get_money(self):        # 取得資產明細
        print("\nIvan資產: ", self.ivanmoney,
              "\n父親資產: ", self.fathermoney,
              "\n祖父資產: ", self.grandfathermoney)

ivan = Ivan()
ivan.get_info3()                # 從Ivan中獲得
ivan.get_info2()                # 流程 Ivan -> Father
ivan.get_info1()                # 流程 Ivan -> Father -> Grandtather
ivan.get_money()                # 取得資產明細

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch12\ch12_16.py

# ch12_16
class Father():
    """ 定義父親的資產 """
    def __init__(self):
        self.fathermoney = 10000
   
class Ira(Father):                                  # 父類別是Father
    """ 定義Ira的資產 """
    def __init__(self):
        self.iramoney = 8000
        super().__init__()
   
class Ivan(Father):                                 # 父類別是Father
    """ 定義Ivan的資產 """
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()   
    def get_money(self):                            # 取得資產明細
        print("Ivan資產: ", self.ivanmoney,
              "\n父親資產: ", self.fathermoney,
              "\nIra資產 : ", Ira().iramoney)        # 注意寫法

ivan = Ivan()
ivan.get_money()                                    # 取得資產明細

print("------------------------------------------------------------")  # 60個

class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name):
        self.name = animal_name         # 紀錄動物名稱
    def which(self):                    # 回傳動物名稱
        return 'My pet ' + self.name.title()
    def action(self):                   # 動物的行為
        return ' sleeping'

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name):       # 紀錄動物名稱
        super().__init__(dog_name.title())
    def action(self):                   # 動物的行為
        return ' running in the street'

class Monkeys():
    """猴子類別, 這是其他類別 """
    def __init__(self, monkey_name):    # 紀錄動物名稱
        self.name = 'My monkey ' + monkey_name.title()
    def which(self):                    # 回傳動物名稱
        return self.name
    def action(self):                   # 動物的行為
        return ' running in the forest'
    
def doing(obj):                         # 列出動物的行為
    print(obj.which(), "is", obj.action())
    
my_cat = Animals('lucy')                # Animals物件
doing(my_cat)
my_dog = Dogs('gimi')                   # Dogs物件
doing(my_dog)
my_monkey = Monkeys('taylor')           # Monkeys物件
doing(my_monkey)

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action2(self):      # 定義action2()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Ivan(Father, Uncle):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action3(self):      # 定義action3()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Ivan(Father, Uncle):
    """ 定義Ivan類別 """
    def action4(self):
        print("Ivan")

ivan = Ivan()
ivan.action4()              # 順序 Ivan
ivan.action3()              # 順序 Ivan -> Father
ivan.action2()              # 順序 Ivan -> Father -> Uncle
ivan.action1()              # 順序 Ivan -> Father -> Uncle -> Grandfather

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    pass
        
class Father(Grandfather):
    """ 定義父親類別 """
    pass

class Ivan(Father):
    """ 定義Ivan類別 """
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

class Grandfather():
    """ 定義祖父類別 """
    pass
        
class Father(Grandfather):
    """ 定義父親類別 """
    pass

class Ivan(Father):
    """ 定義Ivan類別 """
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



print("------------------------------------------------------------")  # 60個





