# ch5_10.py
height = eval(input("請輸入身高(公分)："))
weight = eval(input("請輸入體重(公斤)："))
bmi = weight / (height / 100) ** 2 
if bmi >= 28:
    print(f"體重肥胖")
else:
    print(f"體重不肥胖")







