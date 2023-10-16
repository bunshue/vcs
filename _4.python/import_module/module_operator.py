import operator

cal_dict = {
    '加': operator.add,
    '減': operator.sub,
    '乘': operator.mul,
    '除': operator.truediv,
    '整除': operator.floordiv,
    '次方': operator.pow,
    '無': lambda: None,
    }

def calculator(x, operator, y):
    return cal_dict.get(operator, cal_dict['無'])(x, y)

print(calculator(10, '整除', 3))
