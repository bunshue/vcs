# ch11_37_10.py
things = {'iWatch手錶':(15000, 0.1),    # 定義商品
          'Asus  筆電':(35000, 0.7),
          'iPhone手機':(38000, 0.3),
          'Acer  筆電':(40000, 0.8),          
          'Go Pro攝影':(12000, 0.1),
         }

# 商品依價值排序
th = sorted(things.items(), key=lambda item:item[1][1])   
print('所有商品依價值排序如下')
print('商品', '        商品價格 ',  ' 商品重量')
for i in range(len(th)):
    print(f"{th[i][0]:8s}{th[i][1][0]:10d}{th[i][1][1]:10.2f}")




