# ex11_8.py
def pi(n):
    p = 0
    for i in range(1,n+1, 1):
        p += 4 *((-1)**(i+1)/(2*i-1))
    return p

print("  i      PI ")
print("================")
for i in range(1, 10000, 1000):
    print("%5d   %7.5f" % (i, pi(i)))






