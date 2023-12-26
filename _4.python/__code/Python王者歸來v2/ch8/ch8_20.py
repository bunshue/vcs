# ch8_20.py
# 計算平均值
vals = (5,6,8,9)
mean = sum(vals) / len(vals)
print("平均值 : ", mean)

# 計算變異數
var = 0
for v in vals:
    var += ((v - mean)**2)
var = var / (len(vals))
print("變異數 : ", var)

# 計算標準差
dev = 0
for v in vals:
    dev += ((v - mean)**2)
dev = (dev / (len(vals)))**0.5
print("標準差 : ", dev)




