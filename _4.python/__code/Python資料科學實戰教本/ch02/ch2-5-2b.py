d1 = {x:x*x for x in range(10)}
print("{x:x*x for x in range(10)}")
print(str(d1))
d2 = {x:x*x for x in range(10) if x % 2 == 1}
print("{x:x*x for x in range(11) if x%2==1}")
print(str(d2))


