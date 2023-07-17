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

