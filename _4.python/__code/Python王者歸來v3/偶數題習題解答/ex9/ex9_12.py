# ex9_12.py
season = {'Spring':'春季',
          'Summer':'夏季',
          'Fall':'秋季',
          'Winter':'冬季'}

wd = input("請輸入欲查詢的單字 : ")
if wd in season:
    print(wd, " 中文字義是 : ", season[wd])
else:
    print("查無此單字")













