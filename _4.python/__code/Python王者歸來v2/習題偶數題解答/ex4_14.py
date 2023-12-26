# ex4_14.py
import math

r = 6371                # 地球半徑
x1, y1 = eval(input("請輸入第一個地點的經緯度 : "))
x2, y2 = eval(input("請輸入第二個地點的經緯度 : "))

d = 6371*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                   math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                   math.cos(math.radians(y1-y2)))

print(f"distance = {d:<10.2f}")








    


    







