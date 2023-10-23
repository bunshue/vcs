#__init__()方法呼叫super()

class Animal():#父類別
    def __init__(self):
        print('我屬於動物類別')
        
class Human(Animal): #子類別
    def __init__(self, name):
        super().__init__()
        print('我也屬於人類類別')

man = Human('黃種人')#子類別實體
