# ch5_6.py
print("計算票價")
age = input("請輸入年齡: ")
age = int(age)
ticket = 100
if age >= 80 or age <= 6:
    ticket = ticket * 0.2
    print("票價是: %d" % ticket)
elif age >= 60 or age <= 12:
    ticket = ticket * 0.5
    print("票價是: %d" % ticket)
else:
    print("票價是: %d" % ticket)
    
