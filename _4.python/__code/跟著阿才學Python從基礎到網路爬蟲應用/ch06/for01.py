for i in range(1,6):
    print(i, end=",")
print() 

for i in range(5,0,-1):
    print(i, end=",")
print() 

sum=0
for i in range(1,100,2):
    sum += i
print("1+3+5+...<100=%d" %sum)

program = ["Python", "Java", "C#", "C++"]
for s in program:
    print(s, end=",")