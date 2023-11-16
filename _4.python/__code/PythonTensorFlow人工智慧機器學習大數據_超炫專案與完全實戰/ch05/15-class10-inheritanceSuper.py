#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"
class MyClass(object):
    def fun1(self):
        print("MyClass->fun1")

    def fun2(self):
        print("MyClass->fun2")



class MyClassChild(MyClass):
    def __init__(self, name):
        print("MyClassChild " + str(name))

    def fun2(self):
        try:
          super().fun2()                     # 3.x
        except:
          super(MyClassChild, self).fun2()   # 2.7
        print("MyClassChild->fun3")


g=MyClassChild("Powen Ko")
g.fun1()
g.fun2()










