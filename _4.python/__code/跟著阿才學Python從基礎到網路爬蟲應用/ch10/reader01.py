import csv
f=open ('StudentScore.csv') 	# 建立檔案物件f，此物件操作StudentScore.csv
csvReader =csv.reader(f)#使用csv的reader()方法取得檔案物件f的資料並傳回Reader物件
listData = list(csvReader)		# 使用list()函數將data轉換串列再指定給listData
for row in listData:   	# 將二維串列listData 逐列印出
    print(row) 			
f.close()				# 關閉檔案		
