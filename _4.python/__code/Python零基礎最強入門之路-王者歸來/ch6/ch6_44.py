# ch6_44.py
x = 10
y = 10
z = 15
r = 20
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print("x位址 = %d, y位址 = %d, z位址 = %d, r位址 = %d"
      % (id(x), id(y), id(z), id(r)))
r = x                               # r的值將變為10
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print("x位址 = %d, y位址 = %d, z位址 = %d, r位址 = %d"
      % (id(x), id(y), id(z), id(r)))



