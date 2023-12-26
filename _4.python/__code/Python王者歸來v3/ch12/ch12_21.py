# ch12_21.py
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

grandfa = Grandfather()
father = Father()
ivan = Ivan()
print("ivan屬於Ivan類別: ", isinstance(ivan, Ivan))
print("ivan屬於Father類別: ", isinstance(ivan, Father))
print("ivan屬於GrandFather類別: ", isinstance(ivan, Grandfather))
print("father屬於Ivan類別: ", isinstance(father, Ivan))
print("father屬於Father類別: ", isinstance(father, Father))
print("father屬於Grandfather類別: ", isinstance(father, Grandfather))
print("grandfa屬於Ivan類別: ", isinstance(grandfa, Ivan))
print("grandfa屬於Father類別: ", isinstance(grandfa, Father))
print("grandfa屬於Grandfather類別: ", isinstance(grandfa, Grandfather))


