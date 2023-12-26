# ch4_10.py
speed = input("請輸入火箭速度馬赫數：")
dist = 384400                       # 地球到月亮距離
speeds = 1225 * float(speed)        # 馬赫速度轉成每小時公里數
total_hours = int(dist // speeds)   # 計算小時數

days = total_hours // 24            # 商 = 計算天數
hours = total_hours % 24            # 餘數 = 計算小時數
print(f"總供需要 {days} 天, {hours} 小時")





