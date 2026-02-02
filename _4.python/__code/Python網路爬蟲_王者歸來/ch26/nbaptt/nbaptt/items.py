# -*- coding: utf-8 -*-
import scrapy

class NbapttItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()


