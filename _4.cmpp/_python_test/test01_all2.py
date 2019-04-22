x = 3              # an integer stored (in variable x)
f = 3.1415926      # a floating real point (in variable f)
name = "Python"    # a string
big = 358315791   # long, a very large number
z = complex(2,3)   # (2+3i)  a complex number. consists of real and imaginary part.
 
print(x)
print(f)
print(name)
print(big)
print(z)


s = "Hello Python"
print("len of s is " + str(len(s)))      # prints string length
print(s)      # prints whole string
print(s[0])   # prints "H"
print(s[1]) # prints "e"

print(s[0:2]) # prints "He"
print(s[2:4]) # prints "ll"
print(s[6:])  # prints "Python"

print(3/2)

s = "Hello Python"

print(s + ' ' + s) # print concatenated string.

#置換
print(s.replace('Hello','Thanks')) # print a string with a replaced word

#轉成大寫
# convert string to uppercase
s1 = s.upper()
print(s1)

#轉成小寫 
# convert to lowercase
s2 = s.lower()
print(s2)

#找出字串位置
p = s.find("Python")
print(p)

#置換
s4 = s.replace("Python", "Perl")
print(s4)





#list

l = [ "Drake", "Derp", "Derek", "Dominique" ]
 
print("len of l is " + str(len(l)))      # prints list length
print(l)     # prints all elements
print(l[0])  # print first element
print(l[1])  # prints second element

#排序
l = [ "Drake", "Derp", "Derek", "Dominique" ]
 
print(l)     # prints all elements
l.sort()    # sorts the list in alphabetical order
print(l)     # prints all elements


print("for迴圈")

for i in range(10, 20, 3):
    print(i)

print("while迴圈")

i = 10
while i < 30:
    print(i)
    i += 5
    if( i == 20):
        break

print("自定義函數")

def mycnt1():
    for i in range(10, 20, 5):
        print(i)

mycnt1()

print("自定義函數 加參數")

def mycnt2(n):
    for i in range(10, n, 5):
        print(i)

mycnt2(30)

print("自定義函數 加參數，有預設值")

def mycnt3(n = 20):
    for i in range(10, n, 5):
        print(i)

mycnt3()
mycnt3(30)


print("自定義函數 多個參數")

def mycnt4(n1 = 10, n2 = 20):
    for i in range(n1, n2, 5):
        print(i)

mycnt4()
mycnt4(5)
mycnt4(5, 15)

print("函數返回值")

def mysum(n1, n2):
    return n1 + n2

print(mysum(10, 20))


import os
os.system("ls")
os.system("pause")

