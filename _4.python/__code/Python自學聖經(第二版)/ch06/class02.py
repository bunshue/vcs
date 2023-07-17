class Animal():      #定義類別  
    def __init__(self, name):
        self.name = name  #定義屬性   
    def sing(self):       #定義方法        
        print(self.name + "，很會唱歌!")     
        
bird = Animal("鸚鵡")  #以 Animal 類別，建立一個名叫鸚鵡的 bird物件
print(bird.name) #鸚鵡
bird.sing()      #鸚鵡，很會唱歌!