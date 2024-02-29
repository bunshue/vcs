import os
import sys
import time
import random

import bext

print("------------------------------------------------------------")  # 60個

        
print("------------------------------------------------------------")  # 60個

"""
def wait_for_user_interrupt():
    while True:
        time.sleep(1)
        print('無限迴圈, 按 Ctrl + C 離開')

try:
    wait_for_user_interrupt()
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.

print("------------------------------------------------------------")  # 60個

bext.fg('yellow')
bext.clear()

# Draw the quit message:
bext.goto(0, 0)
print('Ctrl-C to quit.', end='')

print("------------------------------------------------------------")  # 60個


import sys
import time

SAND = chr(9617)
WALL = chr(9608)

print(WALL, end='')
print(' ', end='')  # Clear the old position.
print(SAND, end='')
print(' ', end='')  # Clear the old position.

print(WALL, end='')
print(' ', end='')  # Clear the old position.
print(SAND, end='')
print(' ', end='')  # Clear the old position.

print(WALL, end='')
print(' ', end='')  # Clear the old position.
print(SAND, end='')
print(' ', end='')  # Clear the old position.

print(WALL, end='')
print(' ', end='')  # Clear the old position.
print(SAND, end='')
print(' ', end='')  # Clear the old position.


print('enumerate的用法')
allSand = list('ABCD')

for i, sand in enumerate(allSand):
    print(i, sand)

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

import threading

def run():
    print('啟動了！')
    for i in range(100):
        print(i, end = " ")
    print('完成了！')

thr1 = threading.Thread(target=run)
thr2 = threading.Thread(target=run)
thr1.start()
thr2.start()

print("------------------------------------------------------------")  # 60個


import threading

def run(which):
    print(which, '啟動了！')
    for i in range(100):
        print(which, i)
    print(which, '完成了！')

thr1 = threading.Thread(target=run, args=('1'))
thr2 = threading.Thread(target=run, args=('2'))
thr1.start()
thr2.start()

print("------------------------------------------------------------")  # 60個

import threading
import time

def childThread(name):
    for i in range(7):
        print(name, i)
        time.sleep(1)

thr1 = threading.Thread(target=childThread, args=('1'))
thr1.start()

for i in range(3):
    print('main', i)
    time.sleep(1)
    
print('Wait for child thread...')
thr1.join()
print('Child thread stopped')

print("------------------------------------------------------------")  # 60個

import threading
import time

class MyThread(threading.Thread):
    
    def __init__(self, idnum):
        # 必須先初始化Thread!
        threading.Thread.__init__(self)
        self.idnum = idnum
        
    def run(self):
        for i in range(7):
            print('Thread', self.idnum, i)
            time.sleep(1)
            
thr1 = MyThread(1)
thr2 = MyThread(2)
thr1.start()
thr2.start()

print("------------------------------------------------------------")  # 60個


import threading
import time

def thread1(lock):
    global commonResource
    lock.acquire()
    for i in range(3):
        commonResource += 1
        print(i, 'this is the thread1, resource value:', commonResource)
        time.sleep(1)
    lock.release()
        
def thread2(lock):
    global commonResource
    lock.acquire()
    for i in range(3):
        commonResource -= 1
        print(i, 'this is the thread2, resource value:', commonResource)
        time.sleep(1)
    lock.release()
        
commonResource = 0
lock = threading.Lock()

thr1 = threading.Thread(target=thread1, args=(lock,))
thr2 = threading.Thread(target=thread2, args=(lock,))

print('Thread1 start')
thr1.start()
print('Thread2 start')
thr2.start()

thr1.join()
thr2.join()

print('All threads stop')


print("------------------------------------------------------------")  # 60個

import random
import time

class BankAccount:
    
    def __init__(self, deposit):
        self.balance = deposit
        
    def deposit(self, d):
        self.balance += d
        
    def getBalance(self):
        return self.balance
    
    def withdraw(self, d):
        # delay on bank electronic operation
        self.delay()
        if self.balance>=d:
            # delay on bank electronic operation
            self.delay()
            self.balance -= d
            # delay on bank electronic operation
            self.delay()
            return True
        # delay on bank electronic operation
        self.delay()
        return False    # unsuccessful withdrawal
    
    def delay(self):
        rnd = random.randint(1, 2)
        time.sleep(rnd)



from threading import Thread

class Withdrawer(Thread):
    
    def __init__(self, bankAccount, name):
        Thread.__init__(self)
        self.bankAccount = bankAccount
        self.moneyGot = 0
        self.name = name
        
    def run(self):
        while self.bankAccount.getBalance()>=10:
            if self.bankAccount.withdraw(10):
                self.moneyGot += 10
            else:
                break
            print('This is', self.name, ', I got', self.moneyGot, 'now')
            # delay on withdrawer operation
            self.delay()
        print('This is', self.name, ', I got', self.moneyGot, 'totally')
        
    def delay(self):
        rnd = random.randint(1, 2)
        time.sleep(rnd)


acc = BankAccount(500.0)
print('Current bank balance:', acc.getBalance())
p1, p2, p3 = Withdrawer(acc, 'John'), Withdrawer(acc, 'Mary'), Withdrawer(acc, 'Tom')

p1.start()
p2.start()
p3.start()


print("------------------------------------------------------------")  # 60個

import threading
import random
import time

class SafeBankAccount:
    
    def __init__(self, deposit, lock):
        self.balance = deposit
        self.lock = lock
        
    def deposit(self, d):
        self.balance += d
        
    def getBalance(self):
        return self.balance
    
    def withdraw(self, d):
        # lock on
        lock.acquire()     #!!!!!!!!!!!!!!!!!!
        # delay on bank electronic operation
        self.delay()
        if self.balance>=d:
            # delay on bank electronic operation
            self.delay()
            self.balance -= d
            # delay on bank electronic operation
            self.delay()
            # lock off
            lock.release()     #!!!!!!!!!!!!!!!!!!
            return True
        # delay on bank electronic operation
        self.delay()
        # lock off
        lock.release()     #!!!!!!!!!!!!!!!!!!
        return False    # unsuccessful withdrawal
    
    def delay(self):
        rnd = random.randint(1, 2)
        time.sleep(rnd)

# prepare lock
lock = threading.Lock()

acc = SafeBankAccount(500.0, lock)
print('Current bank balance:', acc.getBalance())
p1, p2, p3 = Withdrawer(acc, 'John'), Withdrawer(acc, 'Mary'), Withdrawer(acc, 'Tom')

p1.start()
p2.start()
p3.start()



print("------------------------------------------------------------")  # 60個

import threading
from threading import Thread
import random
import time

# 消費者thread
def threadConsumer(cond):
    global commonResource
 
 
    for i in range(30):
        # 取得 lock
        cond.acquire()
        print("Acquire the condition lock")    # 執行緒進入等待狀況 
        if commonResource==0:
            print("wait")
            cond.wait()    # 喚醒執行緒 
        print("notify to wake up")
        cond.notify()

        commonResource -= 1
        print("This is the consumer thread ", commonResource)
 
        # 釋放 lock
        cond.release()
        delay()
    
# 生產者thread
def threadProducer(cond):
    global commonResource

    for i in range(30):
        # 取得 lock
        cond.acquire()
 
        # 喚醒執行緒
        commonResource += 1
        print("This is the producer thread ", commonResource)
        cond.notify()
 
        # 釋放 lock
        cond.release()
        delay()
        
def delay():
    time.sleep(random.randint(0, 2))
    
commonResource = 0
condition = threading.Condition()

thr1 = Thread(target=threadConsumer, args=(condition,))
thr2 = Thread(target=threadProducer, args=(condition,))

print('Thread1 consumer start')
thr1.start()
print('Thread2 producer start')
thr2.start()

thr1.join()
thr2.join()

print('All threads stop')



print("------------------------------------------------------------")  # 60個

from threading import Thread
import time

class Rabbit(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
  
    def run(self):
        for i in range(10):
            print(self.name, 'run', i)
            time.sleep(1)
            
class Turtle(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
  
    def run(self):
        for i in range(10):
            print(self.name, 'run', i)
            time.sleep(2)

rabbit1 = Rabbit('Bunny')
turtle1 = Turtle('Ted')
rabbit1.start()
turtle1.start()
"""

print("------------------------------------------------------------")  # 60個

#可以拿來作統計常態分佈用

scores = [90, 59, 78, 71, 39, 0, 19, 85, 77, 84, 91, 98, 38, 66, 65, 88, 63, 85, 18, 0]
freq = [0]*5
for score in scores:
    if score<20:
        freq[0] += 1
    elif score<40:
        freq[1] += 1
    elif score<60:
        freq[2] += 1
    elif score<80:
        freq[3] += 1
    else:
        freq[4] += 1
print('人數分佈頻率:', freq)



print("------------------------------------------------------------")  # 60個

import collections

list1 = [10, 30, 10, 50, 40, 20, 30, 20, 40, 20, 10, 50, 10]
freqDict = collections.Counter(list1)
print(freqDict)

print("------------------------------------------------------------")  # 60個

import string

# 北美獨立宣言
str1 = 'Resolved: That these United Colonies are, and of right ought to be, '+ \
        'free and independent States, that they are absolved from all allegiance '+ \
        'to the British Crown, and that all political connection between them and '+ \
        'the State of Great Britain is, and ought to be, totally dissolved.'
# 先一律轉小寫
str2 = str1.lower()

charSet = set(string.ascii_lowercase)
freqDict = {}
for ch in str2:
    # 判斷如果不在ASCII小寫字母集，則略過
    if not ch in charSet:
        continue
    freqDict[ch] = freqDict.get(ch, 0)+1

print(freqDict)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
