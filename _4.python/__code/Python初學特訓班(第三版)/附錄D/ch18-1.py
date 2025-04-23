
print("------------------------------------------------------------")  # 60個

# ch18-1.py
def add(n1,n2):
    return n1+n2
    
def sub(n1,n2):
    return n1-n2

print(add(5,2))  # 7
print(sub(5,2))  # 3


print("------------------------------------------------------------")  # 60個

# ch18-2.py
import calculate  # 匯入 calculate 模組

print(calculate.add(5,2))  # 7
print(calculate.sub(5,2))  # 3

print("------------------------------------------------------------")  # 60個

# ch18-3.py
from calculate import add,sub

print(add(5,2))  # 7
print(sub(5,2))  # 3

print("------------------------------------------------------------")  # 60個

# ch18-4.py
from calculate import add

print(add(5,2))  # 7
print(sub(5,2))  # NameError: name 'sub' is not defined

print("------------------------------------------------------------")  # 60個

# ch18-5.py

from calculate import *

print(add(5,2))  # 7
print(sub(5,2))  # 3

print("------------------------------------------------------------")  # 60個

# ch18-6.py

from calculate import add as a

print(a(5,2))  # 7

print("------------------------------------------------------------")  # 60個

# ch18-7.py

import calculate as cal # 匯入 calculate 模組，並取別名為 cal

print(cal.add(5,2))  # 7
print(cal.sub(5,2))  # 3

print("------------------------------------------------------------")  # 60個

# class01.py

class Animal():      #定義類別
    name = "小鳥"    #定義屬性
    def sing(self):  #定義方法
        print("很會唱歌!")     
        
bird = Animal()  #建立一個名叫 bird 的 Animal 物件
print(bird.name) #小鳥
bird.sing()      #很會唱歌!

print("------------------------------------------------------------")  # 60個

# class02.py

class Animal():      #定義類別  
    def __init__(self, name):
        self.name = name  #定義屬性   
    def sing(self):       #定義方法        
        print(self.name + "，很會唱歌!")     
        
bird = Animal("鸚鵡")  #建立一個名叫 bird 的 Animal 物件
print(bird.name) #鸚鵡
bird.sing()      #鸚鵡，很會唱歌!

print("------------------------------------------------------------")  # 60個

# class03.py

class Animal():      #定義類別  
    def __init__(self, name,age):
        self.name = name  #定義屬性 
        self.age = age
    def sing(self):       #定義方法        
        print(self.name + str(self.age) + "歲，很會唱歌!")  
    def grow(self,year):  #定義方法        
        self.age += year     
        
bird = Animal("鸚鵡",1)  #建立一個名叫 bird 的 Animal 物件
bird.grow(1)     #長大1歲
bird.sing()      #鸚鵡2歲，很會唱歌!

print("------------------------------------------------------------")  # 60個

# class04.py

class Animal():      #定義類別  
    def __init__(self, name,age):
        self.__name = name  #定義私用屬性 
        self.__age = age
    def __sing(self):       #定義私用方法        
        print(self.__name + str(self.__age),end= "歲，很會唱歌，")  
    def talk(self):        #定義共用方法 
        self.__sing()      #使用私用方法
        print("也會模仿人類說話!")
        
bird = Animal("灰鸚鵡",2)  #建立一個名叫 bird 的 Animal 物件
bird.talk()       #灰鸚鵡2歲，很會唱歌，也會模仿人類說話!

bird.__age = -1  #設定無效
bird.talk()      #灰鸚鵡2歲，很會唱歌，也會模仿人類說話!
#bird.__sing()   #執行出現錯誤

print("------------------------------------------------------------")  # 60個

# class05.py

class Animal():      #定義父類別  
    def __init__(self, name):
        self.name = name  #定義共用屬性         
    def fly(self):        #定義共用方法 
        print(self.name + "很會飛!")
        
class Bird(Animal):      #定義子類別  
    def __init__(self, name):
        self.name = name  #定義共用屬性         
    def sing(self):       #定義共用方法 
        print(self.name + "也愛唱歌!")        

pigeon = Animal("小白鴿") #建立一個名叫 pigeon 的 Animal 物件
pigeon.fly()  #小白鴿很會飛!
      
parrot = Bird("小鸚鵡")   #建立一個名叫 parrot 的 Bird 物件
parrot.fly()  #小鸚鵡很會飛!
parrot.sing() #小鸚鵡也愛唱歌!

print("------------------------------------------------------------")  # 60個

# class06.py

class Animal():      #定義父類別  
    def __init__(self,name):
        self.name = name  #定義共用屬性         
    def fly(self):        #定義共用方法 
        print(self.name + "很會飛!")
        
class Bird(Animal):      #定義子類別  
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age   #定義共用屬性 
    def fly(self):       #定義共用方法         
        print(str(self.age),end="歲") 
        super().fly()

pigeon = Animal("小白鴿") #建立一個名叫 pigeon 的 Animal 物件
pigeon.fly()  #小白鴿很會飛!
      
parrot = Bird("小鸚鵡",2) #建立一個名叫 parrot 的 Bird 物件
parrot.fly()  #2歲小鸚鵡很會飛!

print("------------------------------------------------------------")  # 60個

# class07.py

class Animal():          #定義父類別         
    def fly(self):       #定義共用方法 
        print("時速 20!")
        
class Bird(Animal):      #定義子類別  
    def fly(self,speed): #定義共用方法         
        print("時速 " + str(speed) + "!")
        
class Plane():           #定義類別  
    def fly(self):       #定義共用方法         
        print("時速 1000!")
        
def fly(speed):          #定義函式         
    print("時速 " + str(speed) + "!")    
        
animal = Animal() #建立一個名叫 animal 的 Animal 物件
animal.fly()  #時速 20!
      
bird = Bird() #建立一個名叫 bird 的 Bird 物件
bird.fly(60)  #時速 60!

plane=Plane() #建立一個名叫 plane 的 Plane 物件
plane.fly()   #時速 1000!

fly(5)        #時速 5!

print("------------------------------------------------------------")  # 60個

# class08.py

class Father():         #定義父類別         
    def say(self):      #定義共用方法 
        print("明天會更好!")
        
class Mother():         #定義父類別  
    def say(self):      #定義共用方法 
        print("包含、尊重!")
        
class Child(Father,Mother): #定義子類別  
    pass
        
child = Child() #建立 child 物件
child.say()     #明天會更好! 

print("------------------------------------------------------------")  # 60個

# getPrivateAttribut.py

class Father():      #定義父類別  
    def __init__(self,name):
        self.name = name  #定義私用屬性  
        self.__eye="黑色"
    def getEye(self):    #定義共用方法傳回私用屬性
        return self.__eye
        
class Child(Father):      #定義子類別  
    def __init__(self,name,skin):
        super().__init__(name)
        self.skin=skin
        self.fatherEye=super().getEye() #取得私用屬性
      
joe = Child("小華","棕色") #建立子類別物件 joe
print(joe.name+"眼睛是"+joe.skin+"，他的父親則是"+joe.fatherEye)
# 執行結果：小華眼睛是棕色，他的父親則是黑色      

print("------------------------------------------------------------")  # 60個

