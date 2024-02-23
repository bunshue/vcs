import csv
f=open ('StudentScore.csv')
data=csv.DictReader(f)  # 使用DictReader ()方法取得csv檔資料並傳回data字典型別
print("學號\t姓名\t國文\t英語\t數學\t總分")
for row in data:   		# 逐一印出字典的內容，並計算總分
    print("{}\t{}\t{}\t{}\t{}\t{}"
          .format(row['學號'],row['姓名'],row['國文'],row['英語'],row['數學'],
                  (int(row['國文'])+int(row['英語'])+int(row['數學']))))
f.close()
