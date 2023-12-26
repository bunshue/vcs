# ch6_46.py
x = 10
y = 10
z = 15
r = z - 5
print("is測試")
boolean = x is y
print(f"x位址 = {id(x)}, y位址 = {id(y)}")
print(f"{x = }, {y = }, {boolean}")
boolean = x is z
print(f"x位址 = {id(x)}, z位址 = {id(z)}")
print(f"{x = }, {z = }, {boolean}")
boolean = x is r
print(f"x位址 = {id(x)}, r位址 = {id(r)}")
print(f"{x = }, {r = }, {boolean}")
print("="*60)
print("is not測試")
boolean = x is not y
print(f"x位址 = {id(x)}, y位址 = {id(y)}")
print(f"{x = }, {y = }, {boolean}")
boolean = x is not z
print(f"x位址 = {id(x)}, z位址 = {id(z)}")
print(f"{x = }, {z = }, {boolean}")
boolean = x is not r
print(f"x位址 = {id(x)}, r位址 = {id(r)}")
print(f"{x = }, {r = }, {boolean}")


