# 將兩個數值以decimal型別來處理

# 匯入decimal模組的Decimal()方法
from decimal import Decimal
num1 = Decimal('0.5534')
num2 = Decimal('0.427')
num3 = Decimal('0.37')
print('相加', num1 + num2 + num3)
print('相減', num1 - num2 - num3)
print('相乘', num1 * num2 * num3)
print('相除', num1 / num2)
