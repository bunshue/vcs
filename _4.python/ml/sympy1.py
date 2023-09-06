import sympy

a, b = 500,600
numbers = range(a,b)
prime_numbers = filter(sympy.isprime, numbers)

print("從 {} 到 {} 之間的質數 :".format(a,b))
for prime_number in prime_numbers:
    print(prime_number, end=",")
print()

print('------------------------------------------------------------')	#60個

from sympy import *
x,y,z=symbols('x y z')
init_printing()
Integral(sqrt(1/x),x)

print('------------------------------------------------------------')	#60個
print('解聯立方程式')

from sympy import Symbol, solve

# 定義式子
a = Symbol('a')
b = Symbol('b')
ex1 = a + b - 1
ex2 = 5*a + b - 3

# 解聯立方程式
print(solve((ex1, ex2)))

print('------------------------------------------------------------')	#60個
print('解聯立方程式')

from sympy import Symbol, solve

x = Symbol('x')  # 定義文字
y = Symbol('y')

ex1 = -3/2*x + 6 - y  # 直線1的式子
ex2 = 1/2*x + 2 - y   # 直線2的式子

print(solve((ex1, ex2)))  # 解聯立方程式

print('------------------------------------------------------------')	#60個
print('解聯立方程式')

from sympy import Symbol, solve
a = Symbol('a')   # 定義文字
b = Symbol('b')
ex1 = -1*a + b - 2  # -a + b - 2 = 0
ex2 = 2*a + b - 4   # 2*a + b - 4 = 0
print(solve((ex1, ex2)))   # 解聯立方程式

print('------------------------------------------------------------')	#60個
print('解聯立方程式')

from sympy import Symbol, solve
k = Symbol('k')  # 定義文字
t = Symbol('t')
ex1 = 4*k - 4*t      # 4*k - 4*t = 0
ex2 = -6*k -2*t + 4  # -6*k - 2*t + 4
print(solve((ex1, ex2)))     # 解聯立方程式

print('------------------------------------------------------------')	#60個

