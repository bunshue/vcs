class Animal():      #定義父類別  
    def __init__(self,name):
        self.name = name  #定義共用屬性         
    def fly(self):        #定義共用方法 
        print(self.name + "很會飛!")
        
class Bird(Animal):       #定義子類別  
    def __init__(self,name,age):
        super().__init__(name) #執行父類別的 __init__()方法
        self.age = age    #定義子類別共用屬性 
    def fly(self):        #定義子類別共用方法         
        print(str(self.age),end="歲") 
        super().fly()     #執行父類別的 fly方法

pigeon = Animal("小白鴿") #以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
pigeon.fly()  #小白鴿很會飛!
      
parrot = Bird("小鸚鵡",2) #以 Bird 類別，建立一個名叫小鸚鵡、2歲大的 parrot 物件
parrot.fly()             #2歲小鸚鵡很會飛!