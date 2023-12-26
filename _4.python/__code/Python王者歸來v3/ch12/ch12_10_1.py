# ch12_10_1.py
class Father():
    def __init__(self):
        self.__address = '台北市羅斯福路'
    def getaddr(self):
        return self.__address

class Son(Father):
    pass

hung = Father()
ivan = Son()
print('父類別 : ',hung.getaddr())
print('子類別 : ',ivan.getaddr())







