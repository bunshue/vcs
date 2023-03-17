import sympy

a, b = 500,600
numbers = range(a,b)
prime_numbers = filter(sympy.isprime, numbers)

print("從 {} 到 {} 之間的質數 :".format(a,b))
for prime_number in prime_numbers:
    print(prime_number, end=",")
print()


from sympy import *
x,y,z=symbols('x y z')
init_printing()
Integral(sqrt(1/x),x)




