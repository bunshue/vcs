# ch7_9.py
start = 2
end = 9
step = 2
number1 = list(range(start, end, step))
print("start=%2d, end=%2d, step=%2d的串列 = " % (start, end, step), number1)
start = -2
end = 9
step = 3
number2 = list(range(start, end, step))
print("start=%2d, end=%2d, step=%2d的串列 = " % (start, end, step), number2)
start = 5
end = -5
step = -3
number3 = list(range(start, end, step))
print("start=%2d, end=%2d, step=%2d的串列 = " % (start, end, step), number3)
