import csv
f=open ('StudentScore.csv')
data=csv.DictReader(f)  # 使用DictReader ()方法取得csv檔資料並傳回data字典型別
for row in data:   		# 逐一印出字典的內容
    print(row)	
f.close()
