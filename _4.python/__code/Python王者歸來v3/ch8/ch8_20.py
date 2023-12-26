# ch8_20.py
fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipData = zip(fields, info)             # 執行zip
sold_info = tuple(zipData)              # 將zip資料轉成元組
for city, sales in sold_info:
    print(f'{city} 銷售金額是 {sales}')













