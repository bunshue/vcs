# ch11_19_1.py
def mydata(n):
    print("副程式 id(n) = : ", id(n), "\t", n)
    n = 5
    print("副程式 id(n) = : ", id(n), "\t", n)

x = 1
print("主程式 id(x) = : ", id(x), "\t", x)
mydata(x)
print("主程式 id(x) = : ", id(x), "\t", x)








