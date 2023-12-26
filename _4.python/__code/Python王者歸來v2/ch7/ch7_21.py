# ch7_21.py
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{i}*{j}={result:<3d}", end=" ")
    print()         # 換行輸出
    
