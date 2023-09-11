import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

print(f"全域變數 : {globals()}")


print('------------------------------------------------------------')	#60個

# 定義lambda函數
square = lambda x: x ** 2

# 輸出平方值
print(square(10))

print('------------------------------------------------------------')	#60個

sc = [['John', 80],['Tom', 90], ['Kevin', 77]]
sc.sort(key = lambda x:x[1])
print(sc)

sc = [['John', 80],['Tom', 90], ['Kevin', 77]]
newsc = sorted(sc, key = lambda x:x[1])
print(newsc)


sc = {'John':80, 'Tom':90, 'Kevin':77}
newsc1 = sorted(sc.items(), key = lambda x:x[0])  # 依照key排序
print("依照人名排序")
print(newsc1)

newsc2 = sorted(sc.items(), key = lambda x:x[1])  # 依照value排序
print("依照分數排序")
print(newsc2)



things = {'iWatch手錶':(15000, 0.1),    # 定義商品
          'Asus  筆電':(35000, 0.7),
          'iPhone手機':(38000, 0.3),
          'Acer  筆電':(40000, 0.8),          
          'Go Pro攝影':(12000, 0.1),
         }

# 商品依價值排序
th = sorted(things.items(), key=lambda item:item[1][1])   
print('所有商品依價值排序如下')
print('商品', '        商品價格 ',  ' 商品重量')
for i in range(len(th)):
    print(f"{th[i][0]:8s}{th[i][1][0]:10d}{th[i][1][1]:10.2f}")


    



print('------------------------------------------------------------')	#60個

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

a, b = 24, 36
print("最大公約數是 : ", gcd(a, b))

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

class Banks():
    ''' 定義銀行類別 '''

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__bankname = "Taipei Bank"     # 設定私有銀行名稱

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
hungbank.__balance = 10000                  # 類別外直接竄改存款餘額
hungbank.get_balance()


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

# ch12_13.ipynb
class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        #self.__bankname = "Taipei Bank"     # 設定私有銀行名稱
        self.bankname = "Taipei Bank"       # 設定公有銀行名稱
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
        #return self.__bankname
        return self.bankname

class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.bankname = "Taipei Bank - Shilin Branch"  # 定義分行名稱

hungbank = Shilin_Banks('hung')             # 定義物件hungbank
print("我的存款銀行是: ", hungbank.bank_title())

'''
hungbank.save_money(500)
hungbank.get_balance()
'''

jamesbank = Banks('James')                      # 定義Banks類別物件
print("James's banks = ", jamesbank.bankname)   # 列印銀行名稱
hungbank = Shilin_Banks('Hung')                 # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.bankname)    # 列印銀行名稱

jamesbank = Banks('James')                  # 定義Banks類別物件
print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
hungbank = Shilin_Banks('Hung')             # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.bank_title())   # 列印銀行名稱


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



# ch12_29.ipynb
class Geometric():
    def __init__(self):
        self.color = "Green"
class Circle(Geometric):
    def __init__(self,radius):
        super().__init__()
        self.PI = 3.14159
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self,radius):
        self.radius = radius
    def getDiameter(self):
        return self.radius * 2
    def getPerimeter(self):
        return self.radius * 2 * self.PI
    def getArea(self):
        return self.PI * (self.radius ** 2)
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


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

