import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個


ticks = time.time() #至今的tick數
print(ticks)

localtime = time.localtime(ticks)   #傳回時間元組
print(type(localtime))
print(localtime)

print('年 :', localtime[0])
print('月 :', localtime[1])
print('日 :', localtime[2])
print('時 :', localtime[3])
print('分 :', localtime[4])
print('秒 :', localtime[5])

#asctime() #傳回時間元組的日期時間字串
formattime = time.asctime(time.localtime(ticks))
print(formattime)


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


