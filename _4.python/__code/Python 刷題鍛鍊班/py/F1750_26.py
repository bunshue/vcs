# F1750 練習 26

import operator

def prefix_cal(to_solve):
    operation = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        }
    op, num1, num2 = to_solve.split()
    return operation[op](float(num1), float(num2))

print(prefix_cal('+ 2 3'))
