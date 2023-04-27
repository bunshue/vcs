class Animal():      #定義類別
    name = "小鳥"    #定義屬性
    def sing(self):  #定義方法
        print("很會唱歌!")     
        
bird = Animal()  #以 Animal 類別，建立一個名叫小鳥的 bird物件
print(bird.name) #小鳥
bird.sing()      #很會唱歌!