# -*- coding: utf-8 -*-
import scrapy

class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/NBA/index.html']

    def parse(self, response):
        titles = response.css("div.r-ent div.title a::text").extract()
        authors = response.css("div.r-ent div.author::text").extract()
        for info in zip(titles, authors):
            print('標題 : ', info[0]),        
            print('作者 : ', info[1]), 
            nba_item = {                      
                "title" : info[0],
                "author" : info[1]
            }
            yield nba_item

