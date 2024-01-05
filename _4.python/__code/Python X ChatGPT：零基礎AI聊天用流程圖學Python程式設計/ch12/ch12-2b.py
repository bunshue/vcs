height = float(input("請輸入身高（公分）： "))
weight = float(input("請輸入體重（公斤）： "))

# 將身高從公分轉換成公尺
height_m = height / 100

bmi = weight / (height_m * height_m)

print("您的BMI值為： ", bmi)

