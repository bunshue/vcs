class MyClass(object):
    def __init__(self, name):
        print("MyClass " + str(name))

    def fun1(self):
        print("MyClass->fun1")


class MyClassChild(MyClass):
    def __init__(self, name):
        print("MyClassChild " + str(name))

    def fun2(self):
        print("MyClassChild->fun2")



g=MyClassChild("Powen Ko")
g.fun1()
g.fun2()





