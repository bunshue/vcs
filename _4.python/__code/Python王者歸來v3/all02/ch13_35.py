# ch13_35.py
import random

# 假設一家公司想要測試兩種不同的廣告設計, 以看哪一種效果更好
ad_designs = ['Design A', 'Design B']

# 公司有一個1000人的郵件列表, 想要隨機選擇一半接收A廣告, 一半接收B廣告
recipients = {'Design A': [], 'Design B': []}

# 隨機分配郵件
for i in range(1, 1001):
    chosen_design = random.choice(ad_designs)       # 隨機選擇一種設計
    recipients[chosen_design].append(f'user_{i}')

# 確保每種設計都有500個用戶
while len(recipients['Design A']) != 500:
    if len(recipients['Design A']) > 500:
        user_to_move = recipients['Design A'].pop()
        recipients['Design B'].append(user_to_move)
    else:
        user_to_move = recipients['Design B'].pop()
        recipients['Design A'].append(user_to_move)

# 假設這裡會發送郵件，然後根據用戶反饋進行分析

# 輸出每種設計的接收者數量，確保它們是平均分配的
print(f"A 廣告接收者數量 : {len(recipients['Design A'])}")
print(f"B 廣告接收者數量 : {len(recipients['Design B'])}")


