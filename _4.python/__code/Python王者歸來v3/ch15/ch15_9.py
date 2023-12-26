# ch15_9.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except Exception:           # 通用錯誤使用
        print("通用錯誤發生")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3





