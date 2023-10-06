# 7-3-2 用 dict 模擬 C 語言的 switch...case 語法 (2)

cal_dict = {
    '加': lambda x, y: x + y,
    '減': lambda x, y: x - y,
    '乘': lambda x, y: x * y,
    '除': lambda x, y: x / y,
    }

def calculator(x, operator, y):
    return cal_dict.get(operator, lambda: None)(x, y)

print(calculator(6, '乘', 7))

