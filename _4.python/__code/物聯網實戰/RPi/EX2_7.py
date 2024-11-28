def factorial(n):
    if n < 0:
        return None
    Fac = 1
    for k in range(1, n+1):
        Fac = Fac*k
    return Fac
a=factorial(5)
print(a)
print(factorial(-5))
if factorial(-5) == None:
    print('Not positive number')
