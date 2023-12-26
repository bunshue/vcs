# ch12_11_1.py
class Person():
    def __init__(self,name):
        self.name = name
class LawerPerson(Person):
    def __init__(self,name):
        self.name = name + "律師"

hung = Person("洪錦魁")
lawer = LawerPerson("洪錦魁")
print(hung.name)
print(lawer.name)
















