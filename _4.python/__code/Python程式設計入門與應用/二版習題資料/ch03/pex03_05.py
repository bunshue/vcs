# Filename: pex03_05.py
x1 = float(input("請輸入x1的座標值:"))
y1 = float(input("請輸入y1的座標值:"))
x2 = float(input("請輸入x2的座標值:"))
y2 = float(input("請輸入y2的座標值:"))
pdis=(x1-x2)**2+(y1-y2)**2
pdis=pdis**0.5
print("第一點(%6.2f,%6.2f)與第二點(%6.2f,%6.2f)之間的距離是%6.2f"%(x1,y1,x2,y2,pdis))