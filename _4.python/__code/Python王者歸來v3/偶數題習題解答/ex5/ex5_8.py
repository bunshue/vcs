# ex5_8.py
height = input("請輸入身高(公分)：")
weight = input("請輸入體重(公斤)：")
bmi = int(weight) / ( (float(height) / 100) ** 2 )
if bmi < 18.5:
    print(f"BMI = {bmi:<4.2f} 體重過輕")
elif bmi >= 18.5 and bmi < 24:
    print(f"BMI = {bmi:<4.2f} 正常")
elif bmi >= 24 and bmi < 28:
    print(f"BMI = {bmi:<4.2f} 超重")
else:
    print(f"BMI = {bmi:<4.2f} 肥胖")










