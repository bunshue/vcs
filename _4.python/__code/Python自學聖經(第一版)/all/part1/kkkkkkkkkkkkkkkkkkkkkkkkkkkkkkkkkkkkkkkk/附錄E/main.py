import urequests # 不可使用 requests
import time

r=urequests.get("http://www.e-happy.com.tw")
r.encoding='utf-8'
time.sleep(3)
print("下載完畢!")
if (r.status_code==200):
    print(r.raw.read(100))

