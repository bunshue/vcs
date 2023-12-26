# ex4_16.py
import math

r = 6371                        # 地球半徑
x1, y1 = 39.9196, 116.3669      # 北京故宮經緯度
x2, y2 = 48.8595, 2.3369        # 羅浮宮經緯度

d = 6371*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                   math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                   math.cos(math.radians(y1-y2)))

print(f"distance = {d:6.2f}公里")








    


    







