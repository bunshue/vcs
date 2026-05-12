h = 3 + 4j
print(type(h))
print(h)

print(abs(h))

print("------------------------------------------------------------")  # 60個

print("HEX: \x48\x45\x58")

print("------------------------------------------------------------")  # 60個

name = "陳會安"
balance = 5000
print("姓名: %s 的帳戶餘額是 %d" % (name, balance))

print("------------------------------------------------------------")  # 60個

x, y = 10, 20
s = "Y= {} X= {}".format(x, y)
print(s)

print("------------------------------------------------------------")  # 60個

x, y = 10, 20
s = "Y= {1} X= {0}".format(x, y)
print(s)

print("------------------------------------------------------------")  # 60個




#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-2.py

a, b = 3, 4
print("小於:( 3 < 4 )=", a < b)
print("大於:( 3 > 4 )=", a > b)
print("小於等於:( 3 <= 4 )=", a <= b)
print("大於等於:( 3 >= 4 )=", a >= b)
print("等於:( 3 == 4 )=", a == b)
print("不等於:( 3 != 4 )=", a != b)
print("a =", str(a), " b =", str(b))
print("( 2 <= a <= 5 )=", 2 <= a <= 5)
print("( 12 >= b >= 5 )=", 12 >= b >= 5)

print("------------------------------------------------------------")  # 60個

#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-2a.py

a, b = 3, 4
c = a < b
d = a == b 
print("c條件運算式(a < b)=", c)
print("d條件運算式(a == b)=", d)
print("NOT邏輯運算子: (not c)=", (not c))
print("AND邏輯運算子: (c and d)=", (c and d))
print("OR邏輯運算子: (c or d)=", (c or d))


print("------------------------------------------------------------")  # 60個

#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-3-5.py

a, b, c = 3, 5, 2
if a > b and a > c:
    print("變數 a 最大!")
else:
    if b > c: 
        print("變數 b 最大!")
    else:
        print("變數 c 最大!")
        

print("------------------------------------------------------------")  # 60個

m = 100
s = 0
for i in range(1, m + 1):
    s = s + i
print("總和 = ", s)

print("------------------------------------------------------------")  # 60個

#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-4-2.py

for a in range(5):
    print("a = ", a)
    

print("------------------------------------------------------------")  # 60個

#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-4-2a.py

for b in range(1, 5):
    print("b = ", b)
    

print("------------------------------------------------------------")  # 60個

#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-4-2b.py

for c in range(1, 11, 2):
    print("c = ", c)
    

print("------------------------------------------------------------")  # 60個

#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-4-3.py

m, r, n = 100, 1, 1
while r <= m:
    r = r * n
    n = n + 1
print("大於100的階層n!=", n-1)

print("------------------------------------------------------------")  # 60個

#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-4-4.py

for i in range(1, 10):
    j = 1
    while j <= 9:
        print(str(i),"*",str(j),"=",str(i*j),"",end="")
        j = j + 1
    print("")
    

print("------------------------------------------------------------")  # 60個

#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-4-5.py

i = 1
while True:
    print(i, end=" ")
    i = i + 1
    if i > 5:
        break
print("\n----------------")
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i, end=" ")
    

print("------------------------------------------------------------")  # 60個

#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-5.py

s = 0
for i in range(1, 6):
    s = s + i
else:
    print("for迴圈結束!")
    print("總和 = ", s)
    

print("------------------------------------------------------------")  # 60個

#檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch03\ch3-5a.py

r = n = 1
while n <= 5:
    r = r * n
    n = n + 1
else:
    print("while迴圈結束!")
    print("5!=", r)
    

print("------------------------------------------------------------")  # 60個




