# ex12_2.py
class Myschool():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def msg(self):
        print("Hi!" + self.name.title() + "你的成績是" + str(self.score) + "分")

A = Myschool("kevin",80)
A.msg()



