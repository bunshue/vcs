# Python 新進測試 06

# 程式 6-1.py (Python 3.x version)
# _*_ coding: utf-8 _*_

def add2number(a, b):
    global d
    c = a + b
    d = a + b
    print("在函數中，(c={}, d={})".format(c,d))
    return c

c = 10
d = 99
print("呼叫函數前，(c={}, d={})".format(c,d))
print("{} + {} = {}".format(2, 2, add2number(2, 2)))
print("函數呼叫後，(c={}, d={})".format(c,d))

  


score = int(input("Please input your score:"))

if score >= 60:
    print("You pass the test, and your grade is", end="")
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 70:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("You fail the test!")


score = int(input("Please input your score:"))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("You fail the test!")





for i in range(2,9):
    if i != 2 and i != 6 : continue
    for j in range(1,10):
        for k in range(i,i+5):
            print("{}x{}={:>2}    ".format(k, j, k*j), end="")
        print()
    print()


for i in range(2,7,4):
    for j in range(1,10):
        for k in range(i,i+5):
            print("{}x{}={:>2}    ".format(k, j, k*j), end="")
        print()
    print()




for i in range(2,7,4):
    for j in range(1,10):
        print("{}x{}={:>2}    ".format(i, j, i*j), end="")
        print("{}x{}={:>2}    ".format(i+1, j, (i+1)*j), end="")
        print("{}x{}={:>2}    ".format(i+2, j, (i+2)*j), end="")
        print("{}x{}={:>2}    ".format(i+3, j, (i+3)*j))
    print()



adict = {'book':10, 'pen':3, 'earser':6, 'ruler':2}

for key, value in adict.items():
    if value < 5:
      print("({},{})".format(key, value))






import random
x = random.randint(1,6)
print(x)
while x != 6:
  x = random.randint(1,6)
  print(x)













