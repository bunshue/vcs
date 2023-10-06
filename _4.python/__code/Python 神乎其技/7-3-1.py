# 7-3-1 用 dict 模擬 C 語言的 switch...case 語法

calculator = {
    '加': lambda x, y: x + y,
    '減': lambda x, y: x - y,
    '乘': lambda x, y: x * y,
    '除': lambda x, y: x / y,
    }

default = lambda: None

print(calculator.get('加', default)(1, 2))

print(calculator.get('乘', default)(3, 5))
