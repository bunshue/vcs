import pandas as pd

# 開啟 csv 檔案
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/twstock_all.csv'

pd.options.mode.chained_assignment = None  #取消顯示pandas資料重設警告

df = pd.read_csv(filename, encoding='big5')  #以pandas讀取檔案
dfprice=pd.DataFrame(df['收盤價'])
    

print(df)

print()

print(dfprice)



