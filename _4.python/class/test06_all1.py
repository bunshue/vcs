import os
import sys
import time
import random

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



