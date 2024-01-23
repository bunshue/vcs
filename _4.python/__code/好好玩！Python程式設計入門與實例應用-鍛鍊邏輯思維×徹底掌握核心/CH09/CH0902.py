# 建立類別，產生物件能以不同再別做存取
class Student:
    def message(self, name): #方法一
        self.data = name
    def showMessage(self): # 方法二
        print(self.data)

s1 = Student()#第一個物件
s1.message('James McAvoy')#呼叫方法時傳入字串
s1.showMessage()
s2 = Student()#第二個物件
s2.message(78.566)#呼叫方法時傳入浮點數值
s2.showMessage()
