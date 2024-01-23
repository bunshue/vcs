'''
CH0302.py 認識正、負無限大
'''
import math #匯入math模組
a = 1E309
print('a = 1E309, 輸出', a)

# 輸出True，表示它是NaN
print('為NaN?', math.isnan(float(a/a)))
b = -1E309
print('b = -1309, 輸出', b)

# 輸出True，表示它是Inf
print('為Inf? ', math.isinf(float(-1E309)))
