import random

# 產生六個不重複的1到49之間的隨機數字
lottery_numbers = random.sample(range(1, 50), 6)

# 將中獎號碼排序，以方便比對
lottery_numbers.sort()

# 印出中獎號碼
print("本期大樂透中獎號碼為：", lottery_numbers)
