# 定義函數
def print_msg():
    print("歡迎學習Python程式設計!")

def is_valid_num(no):
    if no >= 0 and no <= 200.0:
        return True
    else:
        return False

def convert_to_f(c):
    f = (9.0 * c) / 5.0 + 32.0
    return f
# 函數呼叫
print_msg()
c = 100
f = convert_to_f(c)
print("華氏: " + str(f))
if is_valid_num(c):
    print("合法!")
else:
    print("不合法")
