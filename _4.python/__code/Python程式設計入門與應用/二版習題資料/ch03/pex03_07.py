# Filename: pex03_07.py
pradius = float(input("請輸入圖柱的半徑:"))
plength = float(input("請輸入圓柱的長度:"))
parea = pradius*pradius*3.14159
pvolume = parea*plength
print("圓柱的半徑%6.2f長度%6.2f體積為%6.2f"%(pradius,plength,pvolume))