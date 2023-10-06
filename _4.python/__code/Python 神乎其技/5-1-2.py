# 5-1-2 OrderedDict: 能記得鍵插入順序的 dict (Python 3.5 與更早版本)

import collections

d = collections.OrderedDict({'一':1, '二':2, '三':3})

print(d)

d['五'] = 5
d['四'] = 4

print(d)
print(d.keys())