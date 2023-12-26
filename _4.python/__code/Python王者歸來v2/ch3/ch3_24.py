# ch3_24.py
dist = 384400                   # 地球到月亮距離
speed = 1225                    # 馬赫速度每小時1225公里
total_hours = dist // speed     # 計算小時數
days = total_hours // 24        # 商 = 計算天數
hours = total_hours % 24        # 餘數 = 計算小時數
print("總共需要天數")
print(days)
print("小時數")
print(hours)




