class MyClass(object):
    mX=1
    mY=1
    def __init__(self,x,y):
        self.mX=x
        self.mY=y

    def fun1(self):
        s = ""
        for x in range(self.mX,10,1):
            for y in range(self.mY,10,1):
                self.fun2(x,y)

    def fun2(self,x,y):
        s = str(x) + "*" + str(y) + "=" + str(x * y)
        print(s)



g=MyClass(8,8)
g.fun1()





