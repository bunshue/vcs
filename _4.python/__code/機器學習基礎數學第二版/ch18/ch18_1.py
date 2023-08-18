# ch18_1.py
import math

degrees = [30, 45, 60, 90, 120, 135, 150, 180]
for degree in degrees:
    print('角度 = {0:3d},   弧度 = {1:6.3f}'.format(degree, math.pi*degree/180))



