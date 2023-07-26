# county.py
# 網址：http://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0

import requests
url = 'http://www.ibon.com.tw/retail_inquiry_ajax.aspx'
payload = {'strTargetField': 'COUNTY', 'strKeyWords': '南投縣'}
html = requests.post(url, data=payload)
html.encoding='utf-8'

from bs4 import BeautifulSoup
soup = BeautifulSoup(html.text, 'html.parser')
datas = soup.find_all('tr')
print(datas[0:3]) # 顯示前 3 筆表格資料

del datas[0]  # 去掉表頭
for data in datas:
    items = data.find_all('td')
    for item in items:
        print(item.text.strip() , end=',')
    print()

# excel_write.py
import pandas as pd

writer = pd.ExcelWriter('test.xlsx')
print(type(writer))

# 建立數據一
df1 = pd.DataFrame({"name":["david","tom","chiou"],
                    "id":[123,456,789] })
df1.to_excel(writer,sheet_name='sheet1',index=False)

# 建立數據二
df2 = pd.DataFrame({"電話":["0912-112233","0987-556677"],
                    "地址":["台北市","埔里鎮"] })
df2.to_excel(writer,sheet_name='工作表二')

# 儲存至 Excel文件中
writer.save()

# allcounty_pandas.py
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
