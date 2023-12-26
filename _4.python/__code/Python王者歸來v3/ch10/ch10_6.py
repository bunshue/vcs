# ch10_6.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_sydi_physics1 = math ^ physics
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics1)
math_sydi_physics2 = math.symmetric_difference(physics)
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics2)




