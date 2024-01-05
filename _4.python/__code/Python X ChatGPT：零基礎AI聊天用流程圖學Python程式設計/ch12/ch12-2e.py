weight = float(input("請輸入您的體重（公斤）："))
height = float(input("請輸入您的身高（公尺）："))

bmi = weight / (height ** 2)

print("您的BMI值為：", round(bmi, 2))

