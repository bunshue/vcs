class Book:
    #定義方法一：取得書籍名稱和價格
    def setInfo(self, title, price):
        self.title = title
        self.price = price
    #定義方法二：輸出書籍名稱和價格
    def showInfo(self):
        print('書籍名稱:{0:6s}, 價格:{1:4s}元'.format(
            self.title, self.price))
# 產生物件
book1=Book()#物件1
book1.setInfo('Python一週速成', '360')
book1.showInfo() #呼叫方法
book2=Book()#物件2
book2.setInfo('網路行銷與社群行銷', '520')
book2.showInfo()

print('------------------------------------------------------------')	#60個

class Date:
    def setDate(self,birthday): #第一種方法
        self.birthday =birthday
    def showDate(self): #第二種方法
        print("出生年月日:",self.birthday)
d1 = Date()#第一個物件
d1.setDate("民國67年7月3日")#呼叫方法時傳入字串
d1.showDate()
d2 = Date()#第二個物件
d2.setDate([67,7,3])#呼叫方法時傳入串列

print('------------------------------------------------------------')	#60個

