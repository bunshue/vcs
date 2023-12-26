# ch10_5.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_only1 = math - physics
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only1)
math_only2 = math.difference(physics)
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only2)
physics_only1 = physics - math
print("參加物理夏令營同時沒有參加數學夏令營的成員 ",physics_only1)
physics_only2 = physics.difference(math)
print("參加物理夏令營同時沒有參加數學夏令營的成員 ",physics_only2)



