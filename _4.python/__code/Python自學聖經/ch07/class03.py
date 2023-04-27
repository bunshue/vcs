class Animal():      #定義類別  
    def __init__(self, name,age):
        self.name = name  #定義屬性 
        self.age = age
    def sing(self):       #定義方法        
        print(self.name + str(self.age) + "歲，很會唱歌!")  
    def grow(self,year):  #定義方法        
        self.age += year     
        
bird = Animal("鸚鵡",1) #以 Animal 類別，建立一個名叫鸚鵡、1歲大的 bird物件
bird.grow(1)     #長大1歲
bird.sing()      #鸚鵡2歲，很會唱歌!