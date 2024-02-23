import csv
searchName=input('請輸入學生姓名進行查詢成績：') #輸入查詢姓名
f=open ('StudentScore.csv')
data=csv.DictReader(f)  # 使用DictReader ()方法取得csv檔資料並傳回data字典型別
for row in data:   		# 逐一比對姓名是否符合searchName
    if(row['姓名']==searchName):
        print('{}成績資訊如下：'.format(row['姓名']))
        print('學號：{}'.format(row['學號']))
        print('國文：{}'.format(row['國文']))
        print('英語：{}'.format(row['英語']))
        print('數學：{}'.format(row['數學']))
        print('總分：{}'.format((int(row['國文'])+int(row['英語'])+int(row['數學']))))
        break  # 離開迴圈
else:  # 當迴圈沒有執行break，即會執行else區域，表示沒有找到符合姓名
    print("查無{}成績".format(searchName))
f.close()
