# 4-6-1 物件/類別/靜態 method

class MyClass:
    
    def objmethod(self):
        return ('呼叫了物件 method', self)
    
    @classmethod
    def clsmethod(cls):
        return ('呼叫了類別 method', cls)
    
    @staticmethod
    def stcmethod():
        return ('呼叫了靜態 method')


obj = MyClass()

print(obj.objmethod())

print(obj.clsmethod())

print(obj.stcmethod())

print(MyClass.clsmethod())

print(MyClass.stcmethod())