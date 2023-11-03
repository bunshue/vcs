# ch7_12.py
start = 2
end = 9
step = 2
number1 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)
start = -2
end = 9
step = 3
number2 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)
start = 5
end = -5
step = -3
number3 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)
