# ch18_4.py
import math

degrees = [x*30 for x in range(0,13)]
for d in degrees:
    rad = math.radians(d)
    sin = math.sin(rad)
    cos = math.cos(rad)
    print('角度={0:3d}, 弧度={1:5.2f}, sin{2:3d}={3:5.2f}, cos{4:3d}={5:5.2f}'
          .format(d, rad, d, sin, d, cos))



