x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
t = (x,y,z)
print(t)
for i in zip(*t):
    print(i)

