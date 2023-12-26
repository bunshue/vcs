# ch13_37.py
import random

# 假設生產線上有一批產品序列號
product_serials = list(range(1000, 2000))

# 抽檢10個產品進行品質檢查
samples = random.sample(product_serials, 10)

for serial in samples:
    # 這裡會有一個品質檢查的函數
    print(f"檢查序列號 : {serial}")


