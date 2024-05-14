import psutil

print("讀取電腦資訊")

print("------------------------------------------------------------")  # 60個

print("讀取CPU數量、使用率和使用頻率")

print(psutil.cpu_count())  # CPU 邏輯數量
print(psutil.cpu_count(logical=False))  # 實際物理 CPU 數量
print(psutil.cpu_percent(interval=0.5, percpu=True))  # CPU 使用率
# interval：每隔多少秒更新一次
# percpu：查看所有 CPU 使用率
print(psutil.cpu_freq())  # CPU 使用頻率

print("------------------------------------------------------------")  # 60個

print("讀取記憶體使用狀況")
print(psutil.virtual_memory())  # 記憶體資訊

print("------------------------------------------------------------")  # 60個

print("讀取硬碟狀況")
print(psutil.disk_partitions())  # 所有硬碟資訊
# print(psutil.disk_usage("硬碟 device 名稱"))  # 指定硬碟資訊 這一行有問題 black過不了

print("------------------------------------------------------------")  # 60個

print("讀取網路卡資訊")
print(psutil.net_io_counters())  # 網路封包
print(psutil.net_if_addrs())  # 網路卡的組態資訊, 包括 IP 地址、Mac地址、子網掩碼、廣播地址等等
print(psutil.net_connections())  # 目前機器的網路連線

print("------------------------------------------------------------")  # 60個

import datetime

print("讀取系統與使用者資訊")

print(psutil.users())  # 登陸的使用者資訊
print(psutil.boot_time())  # 系統啟動時間
print(datetime.datetime.fromtimestamp(psutil.boot_time()))  # 轉換成標準時間


print("------------------------------------------------------------")  # 60個

print("讀取應用程式資訊")

for prcs in psutil.process_iter():
    print(prcs.name)  # 印出所有正在執行的應用程式 ( 從中觀察 pid )

p = psutil.Process(pid=3987)  # 讀取特定應用程式
print(p.name())  # 應用程式名稱
print(p.exe())  # 應用程式所在路徑
print(p.cwd())  # 應用程式執行路徑
print(p.status())  # 應用程式狀態
print(p.username())  # 執行應用程式的使用者
print(p.cpu_times())  # 應用程式的 CPU 使用時間
print(p.memory_info())  # 應用程式的 RAM 使用資訊

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
