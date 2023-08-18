# ch12_4.py
import math

N = 30
times = 10000000000000              # 電腦每秒可處理數列數目
day_secs = 60 * 60 * 24             # 一天秒數
year_secs = 365 * day_secs          # 一年秒數
combinations = math.factorial(N)    # 組合方式
years = combinations / (times * year_secs)
print("需要 %d 年才可以獲得結果" % years)






    
