import csv
f=open ('tScore.csv') # 建立檔案物件f，此物件操作StudentScore.csv
csvReader=csv.reader(f, delimiter='\t')  # 建立reader物件使用 '\t' 當分隔符號
listData = list(csvReader) #使用list()函數將data轉成串列再指定給Reader
for row in listData:    # 使用巢狀迴圈將ListData串列逐欄印出
    for col in row :
        print(col,'   ',end='')
    print()
f.close()
