import requests
from bs4 import BeautifulSoup
import pandas as pd

df = []
baseurl = 'https://www.1111.com.tw/job-bank/job-index.asp?si=1&ks=電腦&ss=s&ps=100&page='  #電腦

#取得總頁數
html = requests.get(baseurl + '1')
soup = BeautifulSoup(html.text, 'lxml')
tem = soup.find('select', class_='custom-select').text
page = int(tem.replace('1 / ', ''))
if page > 15:  #最多取15頁資料
    page = 15
#逐頁讀取資料
for i in range(page):
    url = baseurl + str(i+1)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    job = soup.select(".it-md")  #取class=jbInfoin內容
    for j in range(len(job)):
        work = job[j].find('div', class_='position0').a.text  #職務名稱
        work = work.replace('【誠徵】', '').replace('【急徵】', '').replace('誠徵', '')
        site = 'https://www.1111.com.tw' + job[j].find('div', class_='position0').a.get('href')  #工作網址
        company = job[j].find('div', class_='d-none d-md-flex jb-organ').a.text  #公司名稱
        companysort = job[j].find('span', class_='d-none d-md-block').text.replace('｜', '')  #公司類別
        tem = job[j].find('div', class_='text-truncate needs').select('span')        
        area = tem[0].text  #工作地點
        salary = tem[1].text  #薪資
        experiment = tem[2].text  #工作經驗
        school = tem[3].text  #學歷
        tem = job[j].find('div', class_='col-12 jbInfoTxt UnExtension').select('p')
        content = ''  #工作內容
        for k in range(len(tem)):
            content = content + tem[k].text

        dfmono = pd.DataFrame([{'職務名稱':work,
                              '工作網址': site,
                              '公司名稱': company,
                              '公司類別': companysort,
                              '工作地點':area,
                              '薪資':salary,
                              '工作經驗':experiment,
                              '學歷':school,
                              '工作內容':content }],
                              )
        df.append(dfmono)
    print('處理第 ' + str(i+1) + ' 頁完畢！')
df = pd.concat(df, ignore_index=True)
df.to_excel('1111data.xlsx', index=0)  #存為excel檔


# 1111city.py
import pandas as pd
import matplotlib.pyplot as plt

#繪圖中文字型
plt.rcParams["font.sans-serif"] = "mingliu"
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_excel('1111data.xlsx')
city = ['台北', '新北', '桃園', '台中', '台南', '高雄']  #六都
citycount = []  #存六都工作職缺數量的串列
for i in range(len(city)):
    df1 = df[df['工作地點'].str.contains(city[i])]  #取出包含指定地點的資料
    citycount.append(len(df1))

ser = pd.Series(citycount, index=city)  #串列轉Series
print(ser)
plt.axis('off')
ser.plot(kind='pie', title='六都電腦職缺數量', figsize=(6, 6))  #繪製圓餅圖

print("------------------------------------------------------------")  # 60個

# 1111salary.py

import pandas as pd
import re
import matplotlib.pyplot as plt

#繪圖中文字型
plt.rcParams["font.sans-serif"] = "mingliu"
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_excel('1111data.xlsx')
city = ['台北', '新北', '桃園', '台中', '台南', '高雄']  #六都
salarylist = []
for i in range(len(city)):
    df1 = df[(df['工作地點'].str.contains(city[i])) & (df['薪資'].str.contains('月薪'))]
    indexlist = df1.index  #取得資料索引
    total = 0  #薪資總額
    for j in range(len(df1)):
        salarytem = df1['薪資'][indexlist[j]].replace(',', '')  #以資料索引取得資料
        salanum = re.findall(r"\d+\.?\d*",salarytem)  #取出資料中的數值
        if len(salanum) == 1:  #若是1個數值即為薪資
            salary = int(salanum[0])
        else:  #若是2個數值則取平均數
            salary = (int(salanum[0])+int(salanum[1]))/2
        total += salary
    salarycity = int(total/len(df1))  #平均薪資
    salarylist.append(salarycity)

ser = pd.Series(salarylist, index=city)  #串列轉Series
print(ser)
plt.ylabel('單位：元')
ser.plot(kind='bar', title='六都電腦職缺薪資', figsize=(5, 5))  #繪製長條圖

print("------------------------------------------------------------")  # 60個


# dataframe.py
import pandas as pd

columns = ['姓名', '班級']
data = [['林大和','一年甲班'], ['張小明','一年乙班'], ['林美麗','一年乙班'],
        ['鄭中林','二年甲班'], ['林品朋','二年甲班'], ['陳明朋','二年乙班']]
df = pd.DataFrame(data, columns=columns)
#print(df)

df1 = df[df['班級']=='二年甲班']
#print(df1)
df2 = df[df['姓名'].str.contains('林')]
#print(df2)
df3 = df[(df['姓名'].str.contains('林')) & (df['班級'].str.contains('一年'))]
print(df3)
