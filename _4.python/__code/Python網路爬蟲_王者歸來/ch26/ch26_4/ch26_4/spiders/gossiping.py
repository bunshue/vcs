# -*- coding: utf-8 -*-
import scrapy

class GossipingSpider(scrapy.Spider):
    name = 'gossiping'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/index.html']
    def parse(self, response):
        url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
        yield scrapy.Request(url, cookies={'over18':'1'}, callback=self.parse_info)   

    def parse_info(self, response):
        titles = response.xpath("//div[@class='title']/a/text()").extract()
        authors = response.xpath("//div[@class='meta']/div[@class='author']/text()").extract()
        for info in zip(titles, authors):
            print('標題 : ', info[0]),        
            print('作者 : ', info[1]), 
            gossiping_item = {                      
                "title" : info[0],
                "author" : info[1]
            }
            yield gossiping_item
