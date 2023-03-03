# 程式7-10.py ( Python 3 version )

import sympy
a, b = 500,600
numbers = range(a,b)
prime_numbers = filter(sympy.isprime, numbers)
print("Prime numbers({}-{}):".format(a,b))
for prime_number in prime_numbers:
    print(prime_number, end=",")
print()
