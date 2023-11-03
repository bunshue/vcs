# ch12_20.py
class Grandfather():
    """ 定義祖父類別 """
    pass
        
class Father(Grandfather):
    """ 定義父親類別 """
    pass

class Ivan(Father):
    """ 定義Ivan類別 """
    def fn(self):
        pass

grandfather = Grandfather()
father = Father()
ivan = Ivan()
print("grandfather物件類型: ", type(grandfather))
print("father物件類型     : ", type(father))
print("ivan物件類型       : ", type(ivan))
print("ivan物件fn方法類型 : ", type(ivan.fn))

