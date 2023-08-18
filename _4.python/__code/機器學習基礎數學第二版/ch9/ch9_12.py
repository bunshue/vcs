# ch9_12.py
a = 1
b = -1
c = -10

r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
if r1 > 0:
    times = int(r1 * 100)
else:
    if r2 > 0:
        times = int(r2 * 100)
print("拜訪次數 = {}".format(times))










    


    







