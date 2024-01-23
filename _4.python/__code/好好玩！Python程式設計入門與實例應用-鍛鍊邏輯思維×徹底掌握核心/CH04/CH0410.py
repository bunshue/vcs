# while廻圈做分數加總

# total儲存總分，score儲存分數設，初值為0.0
total = score = 0.0
count = 0 # 計數器
score = float(input('輸入分數，按-1結束-> '))

# 當score大於「零」時就持續進行
while score >= 0.0 :    
    total = total + score
    count = count + 1
    # 檢查變數 score 非 -1 才做加總
    score = float(input('輸入分數，按-1結束-> '))

average = total / count # 計算平均值
print('共', count, '科，總分:', total,', 平均:', average)

    


