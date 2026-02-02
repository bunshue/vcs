# -*- coding: utf-8 -*-
import sqlite3

class NbapttPipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect ("nbaptt.db") 
        self.cur = self.conn.cursor()
        sql = '''Create table nba_ptt(  
                title TEXT,
                author TEXT,
                date TEXT)'''
        self.cur.execute(sql)
    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
    def process_item(self, item, spider):
        title = item['title']
        author = item['author']
        price = item['date']
        x = (title, author, price)
        sql = '''insert into nba_ptt values(?,?,?)'''  
        self.conn.execute(sql,x)
        return item
