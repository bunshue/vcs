# 函數: 顯示年齡
def print_age(age):
    if age <= 18:
        print("年齡太小!")        
        return  # 終止函數執行
    print("年齡 = ", age)            

# 函數: 檢查數值是否合法
def is_valid_num(no):
    if no >= 0 and no <= 200.0:
        return True  # 合法
    else:
        return False # 不合法

# 函數: 攝氏轉華氏溫度 
def convert_to_f(c):
    f = (9.0 * c) / 5.0 + 32.0
    return f

c = 100.00
print_age(15)  # 函數呼叫
print_age(22)
# 有回傳值的函數呼叫
if is_valid_num(c):
    print("合法!")
else:
    print("不合法")
f = convert_to_f(c)
print("攝氏", c, " = 華氏", f)


