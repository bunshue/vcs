# ch15_18.py
def division(x, y):
    try:                             # try - except指令
        return x / y
    except:                          # 捕捉所有異常
        print("異常發生")
    finally:                         # 離開函數前先執行此程式碼
        print("階段任務完成")

print(division(10, 2),"\n")          # 列出10/2
print(division(5, 0),"\n")           # 列出5/0
print(division('a', 'b'),"\n")       # 列出'a' / 'b'
print(division(6, 3),"\n")           # 列出6/3





