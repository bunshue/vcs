# ch18_2.py
import math

degrees = [30, 60, 90, 120]
r = 10
for degree in degrees:
    curve = 2 * math.pi * r * degree / 360
    print('角度 = {0:3d},   弧長 = {1:6.3f}'.format(degree, curve))



