# Filename: ex08_14.py
while True:
    try:
        x = int(input("請輸入一個數字: "))
        break
    except ValueError:
        print("抱歉!!您所輸入並非是有效的數字，請再輸入一次...")