
print("請輸入你的身高"),
height = input()
h = float(height)
print ("取得身高 %s "%h )

print("請輸入你的體重"),
weight = input()
w = float(weight)
print ("取得體重 %s" %h )

print("請輸入你的年齡"),
age = input()
a = int(age)
print ("取得年齡 %s" %age )

bmi = w/(h*h);
print ("你得 BMI 值%s" %bmi )

if a<45:
    if bmi<22:
        print("Low")
    else:
        print("Medium")
else:
    if bmi<22:
        print("Medium")
    else:
        print("High")
    




