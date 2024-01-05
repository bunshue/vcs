def sum_to_n(start, stop):
    """
    計算從start加至stop的總和並輸出結果。
    :param start: 起始值
    :param stop: 終止值
    """
    total = 0  # 初始化總和為0
    for i in range(start, stop + 1):  # 計數器從start到stop
        total += i  # 累加計數器到總和
    print(f"從{start}加到{stop} = {total}")  # 輸出結果

# 呼叫函數
sum_to_n(1, 5)
