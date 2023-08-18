# ch8_13.py
fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipData = zip(fields, info)                 # 執行zip
sold_info = list(zipData)                   # 將zip資料轉成串列
for city, sales in sold_info:
    print('{} 銷售金額是 {}'.format(city, sales))













