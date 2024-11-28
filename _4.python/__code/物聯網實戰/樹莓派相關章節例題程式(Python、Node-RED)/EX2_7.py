# Example 2.7
def factorial(n):
    if n < 0:
        return None
    return n*factorial(n-1) if n > 0 else 1
a = factorial(5)
print(a)
print(factorial(-5))
if factorial(-5) == None:
    print('Not positive number')
