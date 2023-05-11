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