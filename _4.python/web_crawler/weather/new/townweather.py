import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# 檢查是否有鄉鎮市區代碼檔
if not os.path.isfile('district.csv'):
    df = pd.read_excel('https://www.stat.gov.tw/public/Attachment/712693030RPKUP4RX.xlsx', header=3)
    df.drop(columns=['縣市代碼', '村里代碼', '村里名稱', '村里代碼', '村里代碼.1'], axis=1, inplace=True)
    df.drop_duplicates(inplace=True)
    df.to_csv('district.csv', encoding='big5', index=False)


dftown = pd.read_csv('district.csv', encoding='big5')  #區鄉鎮名稱代碼資料
town = input('請輸入查詢的鄉鎮市區名稱：')  #要查詢的區鄉鎮名稱 
dfs = dftown[(dftown['縣市名稱']==town[:3]) & (dftown['區鄉鎮名稱']==town[3:])]
if len(dfs) > 0:  #區鄉鎮名稱存在
    town_no = str(dfs.iloc[0,1])
    url = 'https://www.cwb.gov.tw/V8/C/W/Town/MOD/3hr/' + town_no + '_3hr_PC.html'  #三日預報網頁
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    
    # 整理時間日期欄
    for t in soup.find_all('span', class_='t'):
        t.replaceWith(t.text + ',')
    for d in soup.find_all('span', class_='d'):
        d.replaceWith(d.text)
    # 整理天氣示意圖欄
    for img in soup.find_all('img'):
        img.replaceWith(img.get('alt'))
    # 整理溫度及體感溫度欄
    for c in soup.find_all('span', class_='tem-C'):
        c.replaceWith(c.text)
    for f in soup.find_all('span', class_='tem-F'):
        f.replaceWith('') 
    # 整理蒲福風級 
    for w1 in soup.find_all('span', class_='wind_1'):
        w1.replaceWith(w1.text + ',')
    for w2 in soup.find_all('span', class_='wind_2'):
        w2.replaceWith('')    
        
    # pandas讀取表格
    df = pd.read_html(str(soup))[0]
    # 資料轉置
    df1 = df.T
    # 刪除不需要的欄
    df1.drop(columns=[1,3,5,7,9,11], axis=1, inplace=True)
    # 重設索引
    df1.reset_index(inplace=True)
    # 將index拆分成時間、日期二欄
    df1[['時間','日期']] = df1['index'].str.split(',', expand=True)
    # 將10拆分成蒲福風級、風向二欄
    df1[['蒲福風級','風向']] = df1[10].str.split(',', expand=True)
    # 刪除index及10二欄
    df1.drop(columns=['index', 10], inplace=True)
    # 修改欄位名稱
    columns = ['天氣狀況','溫度','降雨機率','體感溫度','相對溼度','舒適度','時間','日期','蒲福風級','風向']
    df1.columns = columns
    # 欄位重新排序
    df1 = df1[['時間','日期','天氣狀況','溫度','降雨機率','體感溫度','相對溼度','舒適度','蒲福風級','風向']]
    # 轉為json回傳
    print(df1.to_json(orient='records', force_ascii=False))

else:
    print('無此鄉鎮市區名稱！')