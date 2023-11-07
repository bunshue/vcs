import datetime

start_date_str = "20210125"
end_date_str = "20210201"

start_date = datetime.datetime.strptime(start_date_str, '%Y%m%d')
end_date = datetime.datetime.strptime(end_date_str, '%Y%m%d')

totaldays = (end_date - start_date).days + 1
dates = []
for daynumber in range(totaldays):
    date = (start_date + datetime.timedelta(days=daynumber))
    if date.weekday() < 6:
        dates.append(date.strftime('%Y%m%d'))
print(dates)
