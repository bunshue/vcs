# General IO

print("歡迎光臨 Python")
name = input('請問您的大名')
print('Hi, %s.' % name)

print("計算BMI")
#height = float(input("請輸入你的身高"))
height = 1.55
print ("取得身高 %s "%height )

#weight = float(input("請輸入你的體重"))
weight = 52
print ("取得體重 %s" %weight )

#age = int(input("請輸入你的年齡"))
age = 30
print ("取得年齡 %s" %age )

bmi = weight/(height*height);
print ("你得 BMI 值%s" %bmi )

if age<45:
    if bmi<22:
        print("Low")
    else:
        print("Medium")
else:
    if bmi<22:
        print("Medium")
    else:
        print("High")
    




score = int(input("Please input your score:"))

if score >= 60:
    print("You pass the test, and your grade is", end="")
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 70:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("You fail the test!")


score = int(input("Please input your score:"))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("You fail the test!")




age = input("請輸入你的年紀：")
with_parent = raw_input("和父母一起來嗎？(Y/N)")

if age >= 18:
  print("可以看限制級電影")
elif age >=12:
  print("可以看輔導級電影")
elif (age >= 6 and age < 12) and (with_parent=='Y' or with_parent=='y'):
  print("可以看保護級電影")
else:
  print("只能看普遍級電影")









