# ch11_25_2.py
def total(data):
    return sum(data)

x = (1,5,10)
myList = [min, max, sum, total]
for f in myList:
    print(f, f(x))


