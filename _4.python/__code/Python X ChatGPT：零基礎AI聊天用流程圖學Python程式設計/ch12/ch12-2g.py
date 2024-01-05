import math

def bmi(height_cm, weight):
    height_m = height_cm / 100
    return weight / math.pow(height_m, 2)

height_cm = float(input("請輸入身高（公分）："))
weight = float(input("請輸入體重（公斤）："))

result = bmi(height_cm, weight)
print("您的BMI值為： ", result)

