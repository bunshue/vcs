t1 = (4, 2, 8, 9, 1)
print("t1 = " + str(t1))
s = len(t1)
print("len(t1) = " + str(s))
s = max(t1)
print("max(t1) = " + str(s))
s = min(t1)
print("min(t1) = " + str(s))
str1 = 'Hello World!'
t2 = tuple(str1)
print("t2 = " + str(t2))
for i, v in enumerate(t2, 0):
    print(str(i) + ":" + v, end=" ")
print()
s = sum(t1)
print("sum(t1) = " + str(s)) 
t3 = sorted(t1)
print("t3 = sorted(t1) = " + str(t3))
 