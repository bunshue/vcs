# Filename: pex05_09.py
def pdistance(px1,py1,px2,py2):
    presult=(px1-px2)**2+(py1-py2)**2
    presult=presult**0.5    
    return presult

x1 = float(input("請輸入x1的座標值:"))
y1 = float(input("請輸入y1的座標值:"))
x2 = float(input("請輸入x2的座標值:"))
y2 = float(input("請輸入y2的座標值:"))
print("第一點(%6.2f,%6.2f)與第二點(%6.2f,%6.2f)之間的距離是%6.2f"%(x1,y1,x2,y2,pdistance(x1,y1,x2,y2)))