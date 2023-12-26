# ex4_12.py
x1, y1 = eval(input("請輸入第1個點的 x,y 座標 : "))
x2, y2 = eval(input("請輸入第2個點的 x,y 座標 : "))
x3, y3 = eval(input("請輸入第3個點的 x,y 座標 : "))

dist1 = ((x1 - x2) ** 2 + ((y1 - y2) ** 2)) ** 0.5
dist2 = ((x1 - x3) ** 2 + ((y1 - y3) ** 2)) ** 0.5
dist3 = ((x3 - x2) ** 2 + ((y3 - y2) ** 2)) ** 0.5
p = (dist1 + dist2 + dist3) / 2

area = (p * (p - dist1) * (p - dist2) * (p - dist3)) ** 0.5
print(f"三角形面積是 : {area:<10.2f}")









