class Father():      #定義父類別  
    def __init__(self,name):
        self.name = name    
        self.__eye = "黑色" #定義私用屬性
    def getEye(self):    #定義共用方法傳回私用屬性
        return self.__eye
        
class Child(Father):      #定義子類別  
    def __init__(self,name,eye):
        super().__init__(name)
        self.eye = eye
        self.fatherEye = super().getEye() #取得私用屬性
      
joe = Child("小華","棕色") #建立子類別物件 joe
print(joe.name + "眼睛是" + joe.eye + "，他的父親則是" + joe.fatherEye)
# 執行結果：小華眼睛是棕色，他的父親則是黑色

