# ch10_4.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
allmember1 = math | physics
print("參加數學或物理夏令營的成員 ",allmember1)
allmember2 = math.union(physics)
print("參加數學或物理夏令營的成員 ",allmember2)


