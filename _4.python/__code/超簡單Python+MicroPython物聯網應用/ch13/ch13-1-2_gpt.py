import ntptime
import utime
from xtools import connect_wifi_led

# 連接WiFi
connect_wifi_led()

# 從網路獲取UTC時間
ntptime.settime()

# 獲取當前本地時間並轉換為元組格式
local_time = utime.localtime()

# 中原標準時間是UTC+8，因此需要將時間增加8小時
CST_OFFSET = 8 * 3600
cst_time = utime.localtime(utime.mktime(local_time) + CST_OFFSET)

# 顯示年、月、日、時、分、秒
year, month, day, hour, minute, second, _, _ = cst_time
print("年:", year)
print("月:", month)
print("日:", day)
print("時:", hour)
print("分:", minute)
print("秒:", second)

