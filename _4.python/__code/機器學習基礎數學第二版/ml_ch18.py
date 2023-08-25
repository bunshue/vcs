import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch18\ch18_1.py

# ch18_1.py
import math

degrees = [30, 45, 60, 90, 120, 135, 150, 180]
for degree in degrees:
    print('角度 = {0:3d},   弧度 = {1:6.3f}'.format(degree, math.pi*degree/180))




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch18\ch18_2.py

# ch18_2.py
import math

degrees = [30, 60, 90, 120]
r = 10
for degree in degrees:
    curve = 2 * math.pi * r * degree / 360
    print('角度 = {0:3d},   弧長 = {1:6.3f}'.format(degree, curve))




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch18\ch18_3.py

# ch18_3.py
import math

degrees = [30, 60, 90, 120]
r = 10
for degree in degrees:
    area = math.pi * r * r * degree / 360
    print('角度 = {0:3d},   扇形面積 = {1:6.3f}'.format(degree, area))




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch18\ch18_4.py

# ch18_4.py
import math

degrees = [x*30 for x in range(0,13)]
for d in degrees:
    rad = math.radians(d)
    sin = math.sin(rad)
    cos = math.cos(rad)
    print('角度={0:3d}, 弧度={1:5.2f}, sin{2:3d}={3:5.2f}, cos{4:3d}={5:5.2f}'
          .format(d, rad, d, sin, d, cos))




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch18\ch18_5.py

# ch18_5.py
import matplotlib.pyplot as plt
import math

degrees = [x*15 for x in range(0,25)]
x = [math.cos(math.radians(d)) for d in degrees]
y = [math.sin(math.radians(d)) for d in degrees]

plt.scatter(x,y)
plt.axis('equal')
plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch18\ch18_6.py

# ch18_6.py
import matplotlib.pyplot as plt
import numpy as np

degrees = np.arange(0, 360)
x = np.cos(np.radians(degrees))
y = np.sin(np.radians(degrees))

plt.plot(x,y)
plt.axis('equal')
plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

