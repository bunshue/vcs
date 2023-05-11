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