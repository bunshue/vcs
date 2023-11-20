import sys

print('------------------------------------------------------------')	#60個

a=33
b="abc"
c=33.4
print("Hello")                            
print(a)                                        
print("b="+str(a))                       
print("c=%f" % c)
print("c=%.1f  b=%s" % (c,b))
print(a+c)                               

print('------------------------------------------------------------')	#60個

v1 = int(2.7) # 2
print(v1)
v2 = int(-3.9) # -3
print(v2)
v3 = int("2") # 2
print(v3)
v4 = int("11", 16) # 17, base 16
print(v4)
v6 = float(2) # 2.0
print(v6)
v7 = float("2.7") # 2.7
print(v7)
v8 = float("2.7E-2") # 0.027
print(v8)
v9 = float(False) # 0.0
print(v9)
vA = float(True) # 1.0
print(vA)
vB = str(4.5) # "4.5"
print(vB)
vC = list([1, 3, 5]) # "[1, 3, 5]"
print(vC)
vD = bool(True) # False; bool fn since Python 2.2.1
print(vD)

print('------------------------------------------------------------')	#60個

a=5
b=2.2
print(a+b)
print(a-b)
print(a*2)
print(a/2)
print(a<<1)
print(a>>1)
print(a%3)

d=4.3
print(d/3)
print(d//3)

print('------------------------------------------------------------')	#60個

a=4
b=2.2
c="hello"

#print c
print(c)
print("a="+str(a))
print("a=%d" % a)
print("a="+str(a)+" b="+str(b))
print("a=%d b=%f" % (a,b))
print("a=%d b=%.1f" % (a,b))
print("a="+str(a)+" b="+str(b)+" c="+c)
print("a=%d b=%0.1f c=%s" % (a,b,c))

print('------------------------------------------------------------')	#60個

a=[[11,22,33],
   [44,55,66],
   [77,88,99]]
print(a[1])
print(a[1][0])

print('------------------------------------------------------------')	#60個

a=range(10)
print(a)         # Pyton 2.x
print(list(a))   # Pyton 3.x
print(a[2])

print('------------------------------------------------------------')	#60個

a=range(2,6)
print(a)         # Pyton 2.x
print(list(a))   # Pyton 3.x

print('------------------------------------------------------------')	#60個

a=range(0,6,2)
print(a)         # Pyton 2.x
print(list(a))   # Pyton 3.x

print('------------------------------------------------------------')	#60個

a=range(6,0,-2)
print(a)         # Pyton 2.x
print(list(a))   # Pyton 3.x


print('------------------------------------------------------------')	#60個

for x in range(10):  #0,1,2....,9
    print(x)
print("end")


print('------------------------------------------------------------')	#60個

a=range(10)
print(list(a))
for x in a:
    print(x)
print("end")

print('------------------------------------------------------------')	#60個

for x in range(2,6):
    print(x)
print("end")

print('------------------------------------------------------------')	#60個

for x in range(0,6,2):    # [0,2,4]
    print(x)
print("end")




"""
for (x=0;x<6;x=x+2){
   print(x)
}
"""





print('------------------------------------------------------------')	#60個

for x in range(6,0,-2):    #[6,4,2]
    print(x)
print("end")


print('------------------------------------------------------------')	#60個

a=['Apple', 'Watermelon', 'Banana']
for x in a:
    print(x)
print("end")


print('------------------------------------------------------------')	#60個

for x in range(1,10):
   for y in range(1,10):
       print(str(x)+" * "+ str(y) + " = " +str(x*y))
print("end")



print('------------------------------------------------------------')	#60個

try:            #python 3.x
   name= input("名字:")
   print(" 你好! " + name)
except:         #python 2.x
   name= raw_input("名字:").decode("utf-8")
   nameutf8 = unicode(name).encode('utf-8')
   print(" 你好! " + nameutf8)

print('------------------------------------------------------------')	#60個

x=0
while x<5:
    print(x)
    x=x+1

print("end")


"""
while (x<5){
    print(x)
    x=x+1
}
"""

print('------------------------------------------------------------')	#60個

x=0
while x<=20:
    print(x)
    x=x+5
print("end")


print('------------------------------------------------------------')	#60個

x=0
while x<9:
    x=x+1
    y=1
    while y<10:
        #if x!=4 and y!=4:
        print(str(x)+"*"+str(y)+"="+str(x*y))
        y=y+1
print("end")



print('------------------------------------------------------------')	#60個


