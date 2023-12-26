# ch8_15.py
drinks = ("coffee", "tea", "wine")
# 解析enumerate物件
for drink in enumerate(drinks):             # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("****************")   
# 解析enumerate物件
for drink in enumerate(drinks, 10):         # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)










          


