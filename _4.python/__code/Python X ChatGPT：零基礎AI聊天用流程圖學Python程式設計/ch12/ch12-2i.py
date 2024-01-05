# 讀取使用者輸入的身高（公分），並轉換成公尺
height = float(input("請輸入您的身高（公分）：")) / 100

# 讀取使用者輸入的體重（公斤）
weight = float(input("請輸入您的體重（公斤）："))

# 計算BMI值
bmi = weight / (height ** 2)

# 輸出BMI值，並四捨五入到小數點後兩位
print("您的BMI值為：", round(bmi, 2))
