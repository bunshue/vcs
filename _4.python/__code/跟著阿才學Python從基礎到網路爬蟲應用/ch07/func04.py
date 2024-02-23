# 定義GetRoundArea函式，可傳入radius半徑，並傳回圓面積
def GetRoundArea(radius) :
    #傳回圓面積，圓面積公式為 半徑 *  半徑 * 3.14
    return radius * radius * 3.14

r = int(input("請輸入半徑："))
RoundArea = GetRoundArea(r)
print("圓形半徑 %d，面積為 %d" %(r, RoundArea))




