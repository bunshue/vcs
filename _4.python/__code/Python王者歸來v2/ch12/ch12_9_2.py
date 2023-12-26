# ch12_9_2.py
class Score():
    def __init__(self, score):
        self.__score = score
    def getscore(self):
        print("inside the getscore")
        return self.__score
    def setscore(self, score):
        print("inside the setscore")
        self.__score = score

stu = Score(0)
print(stu.getscore())
stu.setscore(80)            
print(stu.getscore())





        
        
