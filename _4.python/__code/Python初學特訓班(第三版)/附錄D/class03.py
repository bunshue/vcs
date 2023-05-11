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