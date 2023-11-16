#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"
class MyClass(object):
    def fun1(self):
        print("MyClass->fun1")


class MyClass2(object):
    def fun2(self):
        print("MyClass2->fun2")



class MyClassChild(MyClass,MyClass2):
    def __init__(self, name):
        print("MyClassChild " + str(name))

    def fun3(self):
        print("MyClassChild->fun3")



g=MyClassChild("Powen Ko")
g.fun1()
g.fun2()
g.fun3()





