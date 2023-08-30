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




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


