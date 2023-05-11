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