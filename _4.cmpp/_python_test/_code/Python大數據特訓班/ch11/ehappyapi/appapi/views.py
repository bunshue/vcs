def createDF(district):
    global df
    year3 = []  #存三天的年份資料(防止剛好跨年)
    colspans = []  #存colspan數值
    dates = []  #存日期
    days = []  #存星期幾
    urlbase = 'http://www.cwb.gov.tw/V7/forecast/town368/3Hr/'
    urltail = '.htm'
    url = urlbase + district + urltail  #完整網址
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    trs = soup.find_all('tr')  #取得所有「tr」標籤
    
    year3.append("%d" % datetime.datetime.now().year)
    year3.append("%d" % (datetime.datetime.now() + datetime.timedelta(days=1)).year) #第二天年份
    year3.append("%d" % (datetime.datetime.now() + datetime.timedelta(days=2)).year) #第三天年份
    tdall = trs[0].findAll('td')  #第1列:月、日及星期
    k=0
    for i in range(len(tdall)): 
        td = tdall[i]
        if i > 0:  #從第二個td開始處理
            if td.has_attr('colspan'):  #如果有colspan標籤
                colspans.append(td.attrs['colspan'])  #取得colspan屬性值
            else:
                colspans.append("1")
            monthdate = re.findall('\d+', td.text)  #取得月日,如05/02
            dates.append(year3[k] + '-' + monthdate[0] + '-' + monthdate[1])
            days.append(re.findall('[一|二|三|四|五|六|日]', td.text)[0]) #取得星期"幾"
            k+=1
    
    #處理第前2列
    ts = []  #存日期及時間
    weekdays = []  #存星期幾
    hours = trs[1].findAll('span')
    k = 0
    for i in range(0, len(colspans)):  
        for j in range(0, int(colspans[i])):  #複複取值
            ts.append(dates[i] + ' ' + hours[k].text)  #日期+時間
            k+=1
            weekdays.append('星期' + days[i])
    df['日期時間'] = ts
    df['星期'] = weekdays
    
    #處理第3列
    wxs = []  #存天氣狀況
    for img in trs[2].findAll('img'):
        wxs.append(img.attrs['alt'])  #文字資料位於alt屬性
    df['天氣狀況'] = wxs
    
    #處理第9列以外的第4到10列
    vals = []  
    for i in range(3, 10):
        if i is not 8:  #排除第9列
            tdall = trs[i].findAll('td')
            for j in range(len(tdall)):
                td = tdall[j]    
                if j > 0:  #從第2列開始才是資料
                    vals.append(td.text)
            df.iloc[:,i] = vals
            vals = []
    
    #處理第9列
    pops = []  #存降雨機率
    rep = 0  #重複次數
    tdall = trs[8].findAll('td')
    for i in range(len(tdall)): 
        td = tdall[i]
        if i > 0:
            if td.has_attr('colspan'):  #如果colspan存在
                rep = int(td.attrs['colspan'])  #colspan屬性值就是重複次數
            else:
                rep = 1  #若沒colspan就不重複取值
            for j in range(0, rep):  #重複取值
                pops.append(td.text)
    df['降雨機率'] = pops

from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import pandas
import re
import datetime

df = ''
def index(request):  #首頁
	return render(request, "index.html")

def threeday(request, district=None):
    global df
    columns = ['日期時間','星期','天氣狀況','溫度','體感溫度','蒲福風級','風向','相對溼度','降雨機率','舒適度']  #欄位名稱
    df = pandas.DataFrame(columns=columns)  #建立DataFrame
    createDF(district)
    json = df.to_json(orient='records', force_ascii=False)
    return HttpResponse(json)


