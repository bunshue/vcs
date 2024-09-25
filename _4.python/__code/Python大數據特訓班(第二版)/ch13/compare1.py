
# 1111data.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

df = []
baseurl = 'https://www.1111.com.tw/job-bank/job-index.asp?si=1&ks=電腦&ss=s&ps=100&page='  #電腦

#取得總頁數
html = requests.get(baseurl + '1')
soup = BeautifulSoup(html.text, 'lxml')
tem = soup.find('span', class_='Nexup').text  
page = int(tem.replace('1 / ', ''))
if page > 15:  #最多取15頁資料
    page = 15
#逐頁讀取資料
for i in range(page):
    url = baseurl + str(i+1)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    job = soup.select(".jbInfoin")  #取class=jbInfoin內容
    for j in range(len(job)):
        work = job[j].h3.a.text  #職務名稱
        work = work.replace('【誠徵】', '').replace('【急徵】', '').replace('誠徵', '')
        site = 'https:' + job[j].h3.a.get('href')  #工作網址
        company = job[j].h4.a.text  #公司名稱
        companysort = job[j].find('div', class_='csort').a.text  #公司類別
        area = job[j].find('span', class_='location').a.text  #工作地點
        tem = job[j].find('div', class_='needs').text
        temlist = tem.split('|')
        salary = temlist[0]  #薪資
        experiment = temlist[1]  #工作經驗
        school = temlist[2]  #學歷
        tem = job[j].find('div', class_='jbInfoTxt')
        temlist = tem.find_all('p')
        content = ''  #工作內容
        for k in range(len(temlist)):
            content = content + temlist[k].text

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
df.to_excel('tmp_1111data.xlsx', index=0)  #存為excel檔


