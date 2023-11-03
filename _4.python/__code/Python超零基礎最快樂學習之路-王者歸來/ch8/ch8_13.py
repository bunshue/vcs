# ch8_13.py
dist = 384400                   # 地球到月亮距離
speed = 1225                    # 馬赫速度每小時1225公里
total_hours = dist // speed     # 計算小時數
data = divmod(total_hours, 24)  # 商和餘數
print("divmod傳回的資料型態是 : ", type(data))
print("總供需要 %d 天" % data[0])
print("%d 小時" % data[1])





