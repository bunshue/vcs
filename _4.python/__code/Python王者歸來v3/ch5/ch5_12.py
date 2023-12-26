# ch5_12.py
height = eval(input("請輸入身高(公分)："))
weight = eval(input("請輸入體重(公斤)："))
bmi = weight / (height / 100) ** 2 
if bmi >= 18.5 and bmi < 24:
    print(f"{bmi = :5.2f}體重正常")

else:
    print(f"{bmi = :5.2f}體重不正常")







