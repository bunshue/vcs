# ch11_37_1.py
from functools import reduce
def strToInt(s):
    def func(x, y):
        return 10*x+y
    def charToNum(s):
        print("s = ", type(s), s)
        mydict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        n = mydict[s]
        print("n = ", type(n), n)
        return n
    return reduce(func,map(charToNum,s))

string = '5487'
x = strToInt(string) + 10
print("x = ", x)


