from datetime import date, timedelta

# 某個日期區間，以1日為間隔值
begin = date(2021, 10, 1)
end = date(2021, 10, 15)
step = timedelta(days = 1)

result = []  #空的List，用來存放日期

# while迴圈 加入date物件
while begin < end:
    result.append(begin.strftime('%Y-%m-%d'))
    begin += step
    
width = 11 #欄寬   
# for/in 讀取並做格式化輸出
for item in result:
    print('{0:{width}}'.format(
        item, width = width), end = '')

