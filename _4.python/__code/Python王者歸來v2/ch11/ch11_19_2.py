# ch11_19_2.py
def mydata(n):
    print(f"函  數 id(n) = :  {id(n)} \t {n}")
    n[0] = 5
    print(f"函  數 id(n) = :  {id(n)} \t {n}")

x = [1, 2]
print("主程式 id(x) = : ", id(x), "\t", x)
mydata(x)
print("主程式 id(x) = : ", id(x), "\t", x)








