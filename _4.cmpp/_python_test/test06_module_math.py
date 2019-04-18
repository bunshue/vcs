import math

print("pi = ",math.pi)
print("pi = " + str(math.pi))

for count in range(20):
    print("sin(" + str(count) + ") = " + str(math.sin(2*math.pi*count/360)) + ", cos(" + str(count) + ") = " + str(math.cos(2*math.pi*count/360)))

