# ch5_11.py
height = eval(input("請輸入身高(公分)："))
weight = eval(input("請輸入體重(公斤)："))
if bmi := weight / ( height / 100) ** 2 >= 28:      # Python 3.8
    print(f"體重肥胖")
else:
    print(f"體重不肥胖")







