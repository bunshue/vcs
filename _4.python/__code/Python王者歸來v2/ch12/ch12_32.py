# ch12_32.py
class City():
    def __init__(self, name):
        self.name = name
    def equals(self, city2):
        return self.name.upper() == city2.name.upper()

one = City("Taipei")
two = City("taipei")
three = City("myhome")
print(one.equals(two))
print(one.equals(three))




