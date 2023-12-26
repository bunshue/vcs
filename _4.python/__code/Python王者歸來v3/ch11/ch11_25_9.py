# ch11_25_9.py
def sum(n):    
    if (n <= 1):                # 結束條件
        return 1
    else:
        return n + sum(n-1)     
    
print(f"total(5) = {sum(5)}")

