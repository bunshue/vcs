class MyClass(object):
    mX=1
    mY=1
    def __init__(self,x,y):
        self.mX=x
        self.mY=y
        self.x1=x

    def fun1(self):
        s = ""
        for x in range(self.mX,10,1):
            for y in range(self.mY,10,1):
                s = str(x) +"*"+ str(y)+"="+str(x*y)
                print(s)
        print(self.x1)


x=1
g=MyClass(8,8)
g.fun1()
print(g.mX)





