# ex3_4.py
times = int(384400 / 250)           # 分鐘總數
minutes = times % 60                # 分鐘數
hours = int(times / 60)             # 小時數
days = int(hours / 24)              # 天總數

print("天總數")
print(days)
print("小時數")
print(hours)
print("分鐘數")
print(minutes)

