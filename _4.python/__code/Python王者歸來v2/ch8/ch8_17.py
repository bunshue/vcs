# ch8_17.py
fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30']
zipData = zip(fields, info)         # 執行zip
print(type(zipData))                # 列印zip資料類型
player = list(zipData)              # 將zip資料轉成串列
print(player)                       # 列印串列













