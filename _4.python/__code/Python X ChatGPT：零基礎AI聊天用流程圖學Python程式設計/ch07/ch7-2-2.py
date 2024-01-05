# 函數: 計算指定範圍的總和
def sum_to_n(start, stop):
    total = 0
    for i in range(start, stop+1):
        total += i
    print("從", start, "加到", stop, " = ", total)

m = 5
sum_to_n(1, 5)  # 函數呼叫
sum_to_n(2, m + 2)

