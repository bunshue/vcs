def bmi(height_cm, weight_kg):
    # 將身高從公分轉換成公尺
    height_m = height_cm / 100

    # 計算BMI值並返回
    bmi_value = weight_kg / (height_m * height_m)
    return bmi_value

# 讀取輸入值
height = float(input("請輸入身高（公分）： "))
weight = float(input("請輸入體重（公斤）： "))

# 呼叫bmi()函數計算BMI值
result = bmi(height, weight)

# 顯示BMI值
print("您的BMI值為： ", result)

