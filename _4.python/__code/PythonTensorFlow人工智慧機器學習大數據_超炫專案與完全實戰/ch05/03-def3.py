#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"
def fun3(num1=0,num2=0):
    return (num1*2)+num2
print(fun3(1,2))
print(fun3(num2=1,num1=2))
print(fun3(num2=1))
a=fun3()
print(a)

def fun4():
    return 1,2

a,b=fun4()
print(a)
print(b)



