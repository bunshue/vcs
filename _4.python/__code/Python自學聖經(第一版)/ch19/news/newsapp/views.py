from django.shortcuts import render
from newsapp import models
import math

page1 = 1  #目前頁面

def index(request, pageindex=None):
	global page1  #重複開啟本網頁時需保留 page1 的值
	pagesize = 8  #每頁顯示的資料筆數
	newsall = models.NewsUnit.objects.all().order_by('-id')  #讀取新聞資料表,依時間遞減排序
	datasize = len(newsall)  #新聞筆數
	totpage = math.ceil(datasize / pagesize)  #總頁數
	if pageindex==None:  #無參數
		page1 = 1
		newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
	elif pageindex=='1':  #上一頁
		start = (page1-2)*pagesize  #該頁第1筆資料
		if start >= 0:  #有前頁資料就顯示
			newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':  #下一頁
		start = page1*pagesize  #該頁第1筆資料
		if start < datasize:  #有下頁資料就顯示
			newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':  #由詳細頁面返回首頁
		start = (page1-1)*pagesize  #取得原有頁面第1筆資料
		newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]

	currentpage = page1  #將目頁前頁面以區域變數傳回html
	return render(request, "index.html", locals())

def detail(request, detailid=None):
	unit = models.NewsUnit.objects.get(id=detailid)  #根據參數取出資料
	category = unit.catego
	title = unit.title
	pubtime = unit.pubtime
	nickname = unit.nickname
	message = unit.message
	unit.press += 1  #點擊數加1
	unit.save()  #儲存資料
	
	return render(request, "detail.html", locals())
