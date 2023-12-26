# ch12_9_4.py
class Score():
    def __init__(self, score):
        self.__score = score
    @property
    def sc(self):
        print("inside the getscore")
        return self.__score
    @sc.setter
    def sc(self, score):
        print("inside the setscore")
        self.__score = score    
    
stu = Score(0)
print(stu.sc)
stu.sc = 80
print(stu.sc)







        
        
