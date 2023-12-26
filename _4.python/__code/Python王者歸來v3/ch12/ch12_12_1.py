# ch12_12_1.py
class Person():
    def job(self):
        print("我是老師")
    
class LawerPerson(Person):
    def job(self):
        print("我是律師")

hung = Person()
ivan = LawerPerson()
hung.job()
ivan.job()


















