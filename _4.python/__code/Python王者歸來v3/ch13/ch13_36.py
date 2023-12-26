# ch13_36.py
import random

# 假設有一組伺服器
servers = ['Server1', 'Server2', 'Server3', 'Server4']

# 模擬1000次請求, 隨機分配到這些伺服器
requests = {server:0 for server in servers}
for _ in range(1000):
    selected_server = random.choice(servers)
    requests[selected_server] += 1

print(requests)         # 顯示每個伺服器獲得的請求數


