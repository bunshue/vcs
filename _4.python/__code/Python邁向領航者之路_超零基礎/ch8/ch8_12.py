# ch8_12.py
fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipData = zip(fields, info)                 # 執行zip
print('zipData資料類型', type(zipData))     # 列印zip資料類型
player = list(zipData)                      # 將zip資料轉成串列
print('player 資料類型', type(player))      # 列印player資料類型
print(player)                               # 列印串列













