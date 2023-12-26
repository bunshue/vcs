# ch27_12.py
def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

N = eval(input("請輸入數列的資料個數 : "))
times = 10000000000000          # 電腦每秒可處理數列數目
day_secs = 60 * 60 * 24         # 一天秒數
year_secs = 365 * day_secs      # 一年秒數
combinations = factorial(N)     # 組合方式
years = combinations / (times * year_secs)
print("資料個數 %d, 數列組合數 = %d " % (N, combinations))
print("需要 %d 年才可以獲得結果" % years)






    
