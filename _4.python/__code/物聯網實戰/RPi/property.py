class Property():
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
    def getName(self):
        return self.__name
    def getValue(self):
        return self.__value
class House(Property):
    def __init__(self, name, value, ownerName, address):
        super().__init__(name, value)
        self.ownerName = ownerName
        self.address = address
class Deposit(Property):
    def __init__(self, name, value, account):
        super().__init__(name, value)
        self.account = account
class Stock(Property):
    def __init__(self, name, amount, price):
        value = amount*price
        super().__init__(name, value)
        self.amount = amount
