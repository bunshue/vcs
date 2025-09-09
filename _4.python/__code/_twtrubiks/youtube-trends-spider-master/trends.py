import sys
import os
import json
import requests
from bs4 import BeautifulSoup


# 移除特殊字元
def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c, "")
    return value.rstrip()


def crawler(link, table):
    r = requests.get(link)
    js = json.loads(r.text)

    # print "keys:", js.keys()
    # print js['html_content'].encode(sys.getfilesystemencoding())

    # 將資料餵給 BeautifulSoup
    soup = BeautifulSoup(js["html_content"], "html.parser")
    # 開始分析 抓取資料
    for info in soup.select(".video-item-info"):
        # title
        title = info.select("h4 a")[0].text
        title = remove(title, "\"'")
        # link
        link = "https://www.youtube.com" + info.select("h4 a")[0]["href"]
        # autor_name
        autor_name = info.select("a")[1].text
        autor_name = remove(autor_name, "\"'")
        # autor_link
        autor_link = "https://www.youtube.com" + info.select("a")[1]["href"]
        # watch
        watch = info.text
        startIndex = watch.find("觀看次數")
        watch = watch[startIndex:].strip()
        """
        print "title:", title.encode(sys.getfilesystemencoding())
        print "link:", link.encode(sys.getfilesystemencoding())
        print "autor_name:", autor_name.encode(sys.getfilesystemencoding())
        print "autor_link:", autor_link.encode(sys.getfilesystemencoding())              
        print "watch:", watch.encode(sys.getfilesystemencoding())                    
        print "======================="      
        """

def main():
    links = [
        (
            "https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=views&loc=twn&gender=--&age=--",
            "views_all",
        ),
        (
            "https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=views&loc=twn&gender=male&age=--",
            "views_male",
        ),
        (
            "https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=views&loc=twn&gender=female&age=--",
            "views_female",
        ),
        (
            "https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=shared&loc=twn&gender=--&age=--",
            "shared_all",
        ),
        (
            "https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=shared&loc=twn&gender=male&age=--",
            "shared_male",
        ),
        (
            "https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=shared&loc=twn&gender=female&age=--",
            "shared_female",
        ),
    ]
    """
    觀看次數最多
    全部   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=views&loc=twn&gender=--&age=-- 	       		  
    男性   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=views&loc=twn&gender=male&age=--	       		   
    女性   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=views&loc=twn&gender=female&age=--	       
  
    分享次數
    全部   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=shared&loc=twn&gender=--&age=--		   		  
    男性   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=shared&loc=twn&gender=male&age=--	       		   
    女性   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=shared&loc=twn&gender=female&age=--
    """

    count = 0
    print("Start parsing... ")

    for link in links:
        count += 1
        URL, tag = link[0], link[1]
        print("URL : ", URL)
        print("tag : ", tag)
        crawler(URL, tag)
    print("Completed")


if __name__ == "__main__":
    main()
