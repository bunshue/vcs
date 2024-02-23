# ch12_3.py
 
day_secs = 60 * 60 * 24         # 一天秒數
year_secs = 365 * day_secs      # 一年秒數

value = (2 ** 64) - 1
years = value // year_secs
print("需要約 %d 年才可以獲得結果" % years)



          


