# ch18_3.py
import math

degrees = [30, 60, 90, 120]
r = 10
for degree in degrees:
    area = math.pi * r * r * degree / 360
    print('角度 = {0:3d},   扇形面積 = {1:6.3f}'.format(degree, area))



