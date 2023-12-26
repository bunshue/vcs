# ex3_8.py
dist = 384400                           # 地球到月亮距離
speed = 1225                            # 馬赫速度每小時1225公里
total_hours = dist / speed              # 計算小時數
print(total_hours)
days, hours = divmod(total_hours, 24)   # 商和餘數
xmins = 60 * (hours - int(hours))
mins, secs = divmod(xmins, 60)
secs = 60 * (secs - int(secs))
print("總供需要天數")
print(days)
print("小時數")
print(hours)
print("分鐘數")
print(int(xmins))
print("秒鐘數")
print(int(secs))






