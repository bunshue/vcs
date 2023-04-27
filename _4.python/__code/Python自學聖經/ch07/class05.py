class Animal():      #定義父類別  
    def __init__(self, name):
        self.name = name  #定義共用屬性         
    def fly(self):        #定義共用方法 
        print(self.name + "很會飛!")
        
class Bird(Animal):      #定義子類別  
    def __init__(self, name):
        self.name = "粉紅色" + name  #覆寫父類別的建構式         
    def sing(self):       #定義子類別的方法 
        print(self.name + "也愛唱歌!")        

pigeon = Animal("小白鴿")#以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
pigeon.fly()  #小白鴿很會飛!
      
parrot = Bird("小鸚鵡")  #以 Bird 類別，建立一個名叫小鸚鵡的 parrot 物件
parrot.fly()  #粉紅色小鸚鵡很會飛!
parrot.sing() #粉紅色小鸚鵡也愛唱歌!