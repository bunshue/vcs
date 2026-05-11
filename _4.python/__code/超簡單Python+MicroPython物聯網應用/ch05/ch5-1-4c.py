def bigger(a, b):
    if a > b:
       return a, b
    else:
       return b, a            

t = bigger(10, 30)
print(t)
print(type(t))
