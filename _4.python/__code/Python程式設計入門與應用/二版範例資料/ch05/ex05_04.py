# Filename: ex05_04.py
def scope():
    var1 = 1
    print(var1, var2)
var1 = 3
var2 = 4
print(var1, var2)
scope()
print(var1, var2) 