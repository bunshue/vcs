# ch15_4.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")
    except TypeError:           # 除法的資料型態不符
        print("除法資料型態不符")

print(division(10, 2))          # 列出10/2
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3





