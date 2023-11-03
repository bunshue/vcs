import datetime as d

def check(y,m):    
    temp_d=d.date(y,m,1)
    temp_year = temp_d.year
    temp_month= temp_d.month
    
    if temp_month == 12 :
        temp_month = 1
        temp_year += 1
    else:
        temp_month += 1   
        
    return d.date(temp_year,temp_month,1)+ d.timedelta(days=-1)

year=int(input("請輸入要查詢的西元年："))
month=int(input("請輸入要查詢的月份1-12："))
print("你要查詢的月份的最後一天是西元",check(year,month))
