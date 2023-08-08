for name in ('__repr__', '__str__', '__format__', '__reduce_ex__'):
    print(name)


for x in (15, 25, 35, 45, 55):
    print(x)

import random

data = [random.uniform(-2, 9) for _ in range(10)]

print(len(data))
print(type(data))
print(data)





'''    
_b85alphabet = (b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                b"abcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")


_b85chars = [bytes((i,)) for i in _b85alphabet]
print(_b85chars)
print()

_b85chars2 = [(a + b) for a in _b85chars for b in _b85chars]

print(_b85chars2)

'''
