# Filename: pex03_11.py
x1, y1, x2, y2, x3, y3 = eval(input("請依序輸入三角形的三點座標值:"))
side1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
side2 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5
side3 = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5
s = (side1 + side2 + side3) / 2;
parea = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print("這三角形的面積為%6.2f"%(parea))