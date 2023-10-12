'''
#numpy製作資料 修改資料 用matplotlib顯示

#numpy的操作 用matplotlib顯示
'''

import sys
import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

x = [x for x in range(0, 11)]                   
y = [7.5*y - 3.33 for y in x]
voucher = 25                            # unit = 100
ans_x = (25 + 3.33) / 7.5
print('拜訪次數 = {}'.format(int(ans_x*100)))
plt.axis([0, 4, 0, 30])
plt.plot(x, y)   
plt.plot(1, 5, '-x')
plt.plot(2, 10, '-x')
plt.plot(3, 20, '-x')
plt.plot(ans_x, 25, '-o')
plt.text(ans_x-0.6, 25+0.2, '('+str(int(ans_x*100))+','+str(2500)+')')
plt.xlabel('Times:unit=100')
plt.ylabel('Voucher:unit=100')
plt.grid()                              # 加格線

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


