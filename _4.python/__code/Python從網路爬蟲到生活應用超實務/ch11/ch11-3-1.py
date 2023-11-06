import time, requests, json
from bs4 import BeautifulSoup

URL = "https://www.ptt.cc" 
url = URL + "/bbs/NBA/index.html"

def get_resource(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/63.0.3239.132 Safari/537.36"}
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        r.encoding = "utf8"
        soup = BeautifulSoup(r.text, "lxml")        
    else:
        print("HTTP請求錯誤..." + url)
        soup = None
    return soup    

def get_articles(soup, date):
    articles = []  
    # 取得上一頁的超連結
    paging_div = soup.find("div", class_="btn-group btn-group-paging")
    paging_a = paging_div.find_all("a", class_="btn")
    prev_url = paging_a[1]["href"]

    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        # 判斷文章的日期
        if tag.find("div",class_="date").text.strip() == date:
            push_count = 0    # 取得推文數
            push_str = tag.find("div", class_="nrec").text
            if push_str:
                try:
                    push_count = int(push_str)  # 轉換成數字
                except ValueError:  # 轉換失敗，可能是'爆'或 'X1','X2'
                    if push_str == '爆':
                        push_count = 99
                    elif push_str.startswith('X'):
                        push_count = -10
            # 取得貼文的超連結和標題文字
            if tag.find("a"):  # 有超連結，表示文章存在
                href = tag.find("a")["href"]
                title = tag.find("a").text
                author = tag.find("div", class_="author").string 
                articles.append({
                    "title": title,
                    "href": href,
                    "push_count": push_count,
                    "author": author
                })
    
    return articles, prev_url

all_articles = []
print("抓取網路資料中...")
soup = get_resource(url)
if soup:
    # 取得今天日期, 去掉開頭'0'符合PTT的日期格式
    today = time.strftime("%m/%d").lstrip('0') 
    # 取得目前頁面的今日文章清單
    current_articles, prev_url = get_articles(soup, today) 
    while current_articles: 
        all_articles += current_articles
        print("等待2秒鐘...")
        time.sleep(2) 
        # 剖析上一頁繼續尋找是否有今日的文章
        soup = get_resource(URL + prev_url)
        current_articles, prev_url = get_articles(soup, today)

print("今天總共有: " + str(len(all_articles)) + " 篇文章")
with open("ptt_NBA.json", "w", encoding="utf-8") as fp: 
    json.dump(all_articles,fp,indent=2,sort_keys=True,ensure_ascii=False)
