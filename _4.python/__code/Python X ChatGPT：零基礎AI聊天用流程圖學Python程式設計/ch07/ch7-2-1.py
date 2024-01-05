# 函數: 顯示訊息
def print_msg():
    print("歡迎學習Python程式設計!")

# 函數: 顯示1加到10的總和 
def sum_to_ten():
    total = 0   
    for i in range(1, 11): # for迴圈敘述
        total += i
    print("從1加到10 = ", total)

print_msg()   # 函數呼叫
sum_to_ten()
