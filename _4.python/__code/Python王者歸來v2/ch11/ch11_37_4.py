# ch11_37_4.py
from functools import reduce
def strToInt(s):
    def charToNum(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(lambda x,y:10*x+y, map(charToNum,s))

string = '5487'
x = strToInt(string) + 10
print("x = ", x)


