import math	#匯入math模組

# 使用math類別的相關方法
num1, num2 = eval(
    input('輸入兩個數值做計算-> '))

# 求平方、立方根
print('平方根：', math.sqrt(num1), ', ', num2 ** 0.5)
print(num1, '^ 3 = ', math.pow(num1, 3))
print(num2, '立方根：', math.pow(num2, 1.0/3))

print('餘數：', math.fmod(num1, num2),
      ', GCD =', math.gcd(num1, num2))
print('兩數平方後相加再開根號', math.hypot(num1, num2))

#自然對數
print('指數函式：', math.e)
print('方法exp(4) =', math.exp(4))

