import requests
from bs4 import BeautifulSoup
import pandas as pd
# 取得所有縣市
url = 'http://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0'
r = requests.get(url)
r.encoding = 'utf-8'
html = BeautifulSoup(r.text, 'html.parser')
areas = html.find('select', id='Class1').find_all('option')
for i in range(len(areas)):
    areas[i] = areas[i].text 
    
# 開始批次擷取
with pd.ExcelWriter('711.xlsx') as writer:
    for county in areas:
        url = 'http://www.ibon.com.tw/retail_inquiry_ajax.aspx'
        payload = {'strTargetField': 'COUNTY', 'strKeyWords': county}
        r = requests.post(url, data=payload)
        r.encoding='utf-8'
        
        print(county,"下載中…")
        df = pd.read_html(r.text, header=0)[0]
        df.to_excel(writer, sheet_name=county,index=False)
        
# 儲存至 Excel文件中
writer.save()        
print("下載完畢")