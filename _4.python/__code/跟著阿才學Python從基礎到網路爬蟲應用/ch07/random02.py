import random  # 引用random亂數套件
#  將 1~49 的整數放入num串列中
num = []
for i in range(49):
    num.append(i+1)
# 使用 random套件的sample函式由num中隨機取得不重複的7個元素
lot = random.sample(num, 7)

print("大樂透  號碼：", end="")
# 印出 lot[0]~lot[5]
for i in range(6):
   print(lot[i], end=", ")
   
print()
print("大樂透特別號：%2d" %(lot[6])) # 印出 lot[6]

