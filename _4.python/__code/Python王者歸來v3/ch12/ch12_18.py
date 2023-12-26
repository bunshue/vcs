# ch12_18.py
class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action2(self):      # 定義action2()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Ivan(Father, Uncle):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather



