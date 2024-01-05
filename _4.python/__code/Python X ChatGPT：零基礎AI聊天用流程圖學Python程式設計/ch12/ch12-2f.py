height = float(input("請輸入您的身高（公分）：")) / 100
weight = float(input("請輸入您的體重（公斤）："))

bmi = weight / (height ** 2)

print("您的BMI值為：", round(bmi, 2))

