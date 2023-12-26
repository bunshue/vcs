# ch12_9_3.py
class Score():
    def __init__(self, score):
        self.__score = score
    def getscore(self):
        print("inside the getscore")
        return self.__score
    def setscore(self, score):
        print("inside the setscore")
        self.__score = score
    sc = property(getscore, setscore)   # Python 風格     
    
stu = Score(0)
print(stu.sc)
stu.sc = 80
print(stu.sc)







        
        
