class Book:
    #定義方法一：取得書籍名稱和價格
    def setData(self, title, price):
        self.title = title
        self.price = price
    #定義方法二：輸出書籍名稱和價格
    def showData(self):
        print('書籍名稱:{0:6s}, 價格:{1:4s}'.format(
            self.title, self.price))
