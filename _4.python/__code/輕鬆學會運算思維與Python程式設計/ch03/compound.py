"""
指派運算子練習
"""

a =3
b =1
c =2

x = a + b * c
print("{}".format(x)) #x=3+1*2=5
a += c 
print("a={0}".format(a,b))  #a=3+2=5
a -= b  
print("a={0}".format(a,b))  #a=5-1=4
a *= b
print("a={0}".format(a,b))  #a=4*1=4
a **= b
print("a={0}".format(a,b))  #a=4**1=4
a /= b
print("a={0}".format(a,b))  #a=4/1=4
a //= b
print("a={0}".format(a,b))  #a=4//1=4
a %= c
print("a={0}".format(a,b))  #a=4%2=0
s = "程式設計" + "很有趣"
print(s)
