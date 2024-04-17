# Filename: pex05_11.py
def isprime(n):
    for pd in range(2, n // 2 + 1):
        if n % pd == 0:
            return False
    return True

for i in range(2, 100):
    if (isprime(i)):
        print("%3d"%i)