#!/usr/bin/env
def fun3(n1,n2):
    print(str(n1)+"*"+str(n2)+"="+str(n1*n2))

x=0
while x<9:
    x=x+1
    y=1
    while y<10:
        fun3(x,y)
        y=y+1