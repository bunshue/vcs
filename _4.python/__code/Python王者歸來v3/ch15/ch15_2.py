# ch15_2.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division(6, 3))           # 列出6/3





