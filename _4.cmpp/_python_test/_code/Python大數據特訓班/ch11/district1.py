import pandas

df = pandas.read_excel('712693030RPKUP4RX.xlsx')
header = df.iloc[2]  #取得標題
df1 = df[3:].copy()  #去除前三列
df1 = df1.rename(columns = header)  #重置標題
df2 = df1.drop(columns=['縣市代碼', '村里代碼', '村里名稱', '村里代碼'], axis=1)  #去除四行資料
df3 = df2.drop_duplicates()  #移除重複資料

df3.to_csv('district.csv', encoding='big5', index=False)
