#多型實作
class Colleague(): #父類別
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def bonus(self):
        return self.income
    
    def title(self):
        return self.name
    
class Manager(Colleague):#子類別
    def bonus(self):        
        return self.income * 1.5
    
class Director(Colleague): #子類別
    def bonus(self):
        return self.income * 1.2
print('===============================')
obj1 = Colleague('一般性員工', 50000) #父類別物件
print('{:8s} 紅利 {:,}'.format(obj1.title(), obj1.bonus()))

print('===============================')
obj2 = Manager('經理級年終', 80000) #子類別物件
print('{:8s} 紅利 {:,}'.format(obj2.title(), obj2.bonus()))

print('===============================')
obj3 = Director('芏任級年終', 65000) #子類別物件
print('{:8s} 紅利 {:,}'.format(obj3.title(), obj3.bonus()))
print('===============================')
