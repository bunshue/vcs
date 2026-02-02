# -*- coding: utf-8 -*-
import scrapy
import time
import random
from nbaptt.items import NbapttItem

class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/NBA/index.html']

    def parse(self, response):
        for i in range(10):
            time.sleep(random.randint(1,3))
            url = 'https://www.ptt.cc/bbs/NBA/index'+str(6498-i)+'.html'
            yield scrapy.Request (url,callback=self.parse_info)
            
    def parse_info(self, response):
        titles = response.xpath("//div[@class='title']/a/text()").extract()
        authors = response.xpath("//div[@class='meta']/div[@class='author']/text()").extract()
        dates = response.xpath("//div[@class='meta']/div[@class='date']/text()").extract()
        for info in zip(titles, authors, dates):
            nba_item = {                      
                "title" : info[0],
                "author" : info[1],
                "date" : info[2]
            }
            yield nba_item

