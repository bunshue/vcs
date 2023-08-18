# ch5_6.py
height = input("請輸入身高(公分)：")
weight = input("請輸入體重(公斤)：")
bmi = int(weight) / ( (float(height) / 100) ** 2 )
if bmi >= 18.5 and bmi < 24:
    print("體重正常")

else:
    print("體重不正常")







