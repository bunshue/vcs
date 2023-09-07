'''
sqlite

'''


print('------------------------------------------------------------')	#60個



from bs4 import BeautifulSoup
import time, random
import sqlite3
import requests

url = "https://tw.appledaily.com/new/realtime/"
dbfile = "applenews.db"
conn = sqlite3.connect(dbfile)
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
headlines = soup.find("ul", {"class": "rtddd slvl"})
items = headlines.find_all("li")
for item in items:
    time.sleep(random.randint(0,2))
    content_url = item.find("a")["href"]
    content = requests.get(content_url).text
    content_soup = BeautifulSoup(content, "lxml")
    title = content_soup.find("h1").text
    print(title)
    article = content_soup.find("article", {"class":"ndArticle_content clearmen"})
    data = article.find("p").text
    sql_str = "insert into news(url, title, content) values('{}','{}','{}')".format(content_url, title, data)
    conn.execute(sql_str)
conn.commit()
conn.close()

print("Done!")

print('------------------------------------------------------------')	#60個

import sqlite3
dbfile = "applenews.db"
conn = sqlite3.connect(dbfile)

sql_str = "select * from news;"
rows = conn.execute(sql_str)
for row in rows:
    for field in row:
        print(field)
conn.close()

print('------------------------------------------------------------')	#60個

import sqlite3
dbfile = "applenews.db"
conn = sqlite3.connect(dbfile)

sql_str = "select count(*) from news;"
result = conn.execute(sql_str)
count = result.fetchone()[0]
print(count)

print('------------------------------------------------------------')	#60個

from bs4 import BeautifulSoup
import time, random
import sqlite3
import requests
url = "https://tw.appledaily.com/new/realtime/"
dbfile = "applenews.db"
conn = sqlite3.connect(dbfile)
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
headlines = soup.find("ul", {"class": "rtddd slvl"})
items = headlines.find_all("li")
for item in items:
    time.sleep(random.randint(0,2))
    content_url = item.find("a")["href"]
    
    sql_str = "select count(*) from news where url='{}';".format(content_url)
    result = conn.execute(sql_str)
    count = result.fetchone()[0]
    if count == 0:
        content = requests.get(content_url).text
        content_soup = BeautifulSoup(content, "lxml")
        title = content_soup.find("h1").text
        print(title)
        article = content_soup.find("article", {"class":"ndArticle_content clearmen"})
        data = article.find("p").text
        data = data.replace("'", "")
        data = data.replace('"', "")
        sql_str = "insert into news(url, title, content) values('{}','{}','{}');".format(content_url, title, data)
        conn.execute(sql_str)
conn.commit()
conn.close()
print("Done!")

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


