# ch13_47.py
import itertools
def mul(x, y):
    return (x * y)
for i in itertools.accumulate((1,2,3,4,5)):
    print(i)

for i in itertools.accumulate((1,2,3,4,5),mul):
    print(i)













