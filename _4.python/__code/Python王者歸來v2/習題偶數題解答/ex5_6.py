# ex5_6.py
hourPay = 150
hours = eval(input("請輸入本週工作時數 : "))
if hours < 40:
    salary = hours * hourPay * 0.8        
elif hours == 40:    
    salary = hours * hourPay
elif hours > 40 and hours <= 50:
    salary = hours * hourPay * 1.2
else:               # 工作時數大於50小時
    salary = hours * hourPay * 1.6
    
print("本週薪資 : %d " % salary)
