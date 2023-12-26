# ch15_13.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except (ZeroDivisionError, TypeError) as e:   # 2個異常
        print(e)

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3





