# 使用str.format()方法或 f_string
import math	#匯入math模組

radius = int(input('輸入半徑值-> '))
#print('PI = {0.pi}'.format(math)) # 輸出PI值
print(f'PI = {math.pi}')
#計算圓面積
area = (math.pi) * radius ** 2 
#print('圓面積 = {0:,.3f}'.format(area))
print(f'圓面積 = {area:,.3f}')

