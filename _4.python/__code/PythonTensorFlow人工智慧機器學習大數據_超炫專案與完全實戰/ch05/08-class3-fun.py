class MyClass(object):
     def __init__(self,name):
           print("hello "+str(name))
     def fun1(self):
           print("fun1")
     def fun3(self,num1=0, num2=0):
         return (num1 * 2) + num2

g=MyClass("Powen")
g.fun1()
print(g.fun3(1,2))
print(g.fun3(num2=1, num1=2))
