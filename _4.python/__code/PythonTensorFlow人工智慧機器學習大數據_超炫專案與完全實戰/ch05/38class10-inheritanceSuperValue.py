#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"
class MyClass(object):
    value2 = 2
    value3 = 3
    def fun1(self):
        print("MyClass->fun1")

    def fun2(self):
        print("MyClass->fun2")
        self.value1=1



class MyClassChild(MyClass):
    value3=13
    def __init__(self, name):
        print("MyClassChild " + str(name))

    def fun2(self):
        try:
          super().fun2()                     # 3.x
        except:
          super(MyClassChild, self).fun2()   # 2.7
        print("MyClassChild->fun3")
        print(self.value1)
        print(self.value2)
        print(self.value3)
        print(super(MyClassChild, self).value3)



g=MyClassChild("Powen Ko")
g.fun1()
g.fun2()










