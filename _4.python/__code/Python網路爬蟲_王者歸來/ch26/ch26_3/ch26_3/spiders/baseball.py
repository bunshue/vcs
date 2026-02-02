# -*- coding: utf-8 -*-
import scrapy

class BaseballSpider(scrapy.Spider):
    name = 'baseball'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Baseball/index.html']

    def parse(self, response):
        titles = response.xpath("//div[@class='title']/a/text()").extract()
        authors = response.xpath("//div[@class='meta']/div[@class='author']/text()").extract()
        for info in zip(titles, authors):
            print('標題 : ', info[0]),        
            print('作者 : ', info[1]), 
            baseball_item = {                      
                "title" : info[0],
                "author" : info[1]
            }
            yield baseball_item
