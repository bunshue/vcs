import time as t

print(t.time())
print(t.localtime())

field=t.localtime(t.time())#以元組資料的名稱去取得資料
print('tm_year= ',field.tm_year)
print('tm_mon= ',field.tm_mon)
print('tm_mday= ',field.tm_mday)
print('tm_hour= ',field.tm_hour)
print('tm_min= ',field.tm_min)
print('tm_mec= ',field.tm_sec)
print('tm_wday= ',field.tm_wday)
print('tm_yday= ',field.tm_yday)
print('tm_isdst= ',field.tm_isdst)

for j in range(9):#以元組的索引值取得的資料內容
    print('以元組的索引值取得資料= ',field[j])
            
print("我有一句話想對你說:")
t.sleep(1) #程式停1秒
print("學習Python的過程唯然漫長,但最終的果實是甜美的")
print("程式執行到目前的時間是"+str(t.process_time()))
t.sleep(2) #程式停2秒
print("程式執行到目前的時間是"+str(t.perf_counter()))

