# File: CH0301.py
# 使用eval()函式取得連續的輸入

num1, num2, num3 = eval(
    input('請輸入三個數值，以逗點隔開：'))
total = num1 + num2 + num3
print('數值合計：', total)
