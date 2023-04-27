class Animal():          #定義父類別         
    def fly(self):       #定義共用方法 
        print("時速 20公里!")
        
class Bird(Animal):      #定義子類別  
    def fly(self,speed): #定義共用方法         
        print("時速 " + str(speed) + "公里!")
        
class Plane():           #定義類別  
    def fly(self):       #定義共用方法         
        print("時速 1000公里!")
        
def fly(speed):          #定義函式         
    print("時速 " + str(speed) + "英哩!")    
        
animal = Animal() #以 Animal 類別建立 animal 物件
animal.fly()  #時速 20公里!
      
bird = Bird() #以 Bird 類別建立 bird 物件
bird.fly(60)  #時速 60公里!

plane=Plane() #以 Plane 類別建立 plane 物件
plane.fly()   #時速 1000公里!

fly(5)        #時速 5英哩!