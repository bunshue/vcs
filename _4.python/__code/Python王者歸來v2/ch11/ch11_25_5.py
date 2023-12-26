# ch11_25_5.py
def dist(x1,y1,x2,y2):          # 計算2點之距離函數
    def mySqrt(z):              # 計算開根號值
        return z ** 0.5
    dx = (x1 - x2) ** 2
    dy = (y1 - y2) ** 2
    return mySqrt(dx+dy)

print(dist(0,0,1,1))






