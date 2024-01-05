height = float(input("請輸入身高(cm): "))
weight = float(input("請輸入體重(kg): "))
height = height / 100.0
BMI = weight / (height * height)
print("BMI = ", BMI)
