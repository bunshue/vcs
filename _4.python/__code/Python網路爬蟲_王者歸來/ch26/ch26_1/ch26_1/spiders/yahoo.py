# -*- coding: utf-8 -*-
import scrapy
import bs4

class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['tw.yahoo.com']
    start_urls = ['http://tw.yahoo.com/']

    def parse(self, response):
        objSoup = bs4.BeautifulSoup(response.text, 'lxml')
        headline_news = objSoup.find_all('a', class_='story-title')
        for h in headline_news:
            news = {
                'news_info' : h.text,
                'links_info ': h.get('href')
                }
            yield news


