# Homework 2-8
class property():
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
    def getName(self):
        return self.__name
    def getValue(self):
        return self.__value
class house(property):
    def __init__(self, name, value, ownerName, address):
        super().__init__(name, value)
        self.ownerName = ownerName
        self.address = address
class deposit(property):
    def __init__(self, name, value, account):
        super().__init__(name, value)
        self.account = account
class stock(property):
    def __init__(self, name, amount, price):
        value = amount*price
        super().__init__(name, value)
        self.amount = amount
tc = house('apartment', 5600000, 'tclin','taichung')
money = deposit('money', 100000, 'taiwanBank')
stock = stock('tpowerStock', 5, 20000)
total = [tc, money, stock]
for i in total:
    print("Property name:{0}, value:{1}".format(i.getName(), i.getValue()))
