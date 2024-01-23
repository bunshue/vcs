# Tuple物件配合Packing, Unpacking
score = [78, 56, 33] # List
chin, math, eng = score # Unpacking

print(f'國文：{chin:2d} 數學：{math:2d} 英文：{eng:2d}')
print(f'總分：{sum(score)}')

n = 'Eric'; b = '1998/4/17'; t = 175
tp = (n, b, t)         # Packing
name, birth, tall = tp # Unpacking

print(f'名字：{name:>4s}')
print(f'生日：{birth:9s}, 身高：{tall}')
