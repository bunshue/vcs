# ch6_45.py
x = 10
y = 10
z = 15
r = 20
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print(f"x位址={id(x)}, y位址={id(y)}, z位址={id(z)}, r位址={id(r)}")
r = x                               # r的值將變為10
print(f"{x = }, {y = }, {z = }, {r = }")
print(f"x位址={id(x)}, y位址={id(y)}, z位址={id(z)}, r位址={id(r)}")






