def sum_to_ten():
    """
    計算從1加至10的總和並輸出結果。
    """
    total = 0  # 初始化總和為0
    for i in range(1, 11):  # 計數器從1到10
        total += i  # 累加計數器到總和
    print("從1加到10 = ", total)  # 輸出結果

# 呼叫函數
sum_to_ten()
