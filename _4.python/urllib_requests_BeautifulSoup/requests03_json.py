import requests
import re
import json

url = "https://www.cpc.com.tw/historyprice.aspx?n=2890"
html_data = requests.get(url)

m = re.search("var pieSeries = (.*);", html_data.text)
jsonstr = m.group(0).strip('var pieSeries = ').strip(";")
j = json.loads(jsonstr)
#print(j)
for item in reversed(j):    #反向排序, 利用 reversed 反轉了排序(原內容由舊到新, 利用這個改為由新到舊)
    new_line = 0
    for data in item['data']:
        if(data['name'] == '超級/高級柴油'):
            new_line = 0
            continue
        else:
            new_line = 1
        print("date:" + item['name'])   #第一層的 name 為日期
        print(data['name'] + ":" + str(data['y']))  #後面再接一層 array data 其中的 name 為產品名, 而 y 為單價
    if (new_line == 1):
        print("================")
