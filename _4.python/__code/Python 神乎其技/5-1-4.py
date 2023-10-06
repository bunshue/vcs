# 5-1-4 defaultdict: 替資料做分類素

from collections import defaultdict

dog_names = ['Bucky', 'Lucky', 'Randy', 'Buddy', 'Bolt', 'Larry']
dd = defaultdict(list)

for name in dog_names:
    dd[name[0]].append(name)

print(dd.keys())
print(dd['B'])
print(dd['L'])
print(dd['R'])


dd = defaultdict(int)

for name in dog_names:
    dd[name[0]] += 1

print(dd['B'])
print(dd['L'])
print(dd['R'])