import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup


# 移除特殊字元
def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c, "")
    return value.rstrip()


def crawler(driver, table):
    print("aaaa")
    delay = 15  # seconds
    # selenium Wait 用法，可參考 http://selenium-python.readthedocs.org/en/latest/waits.html
    try:
        # 當 javascript or ajax 執行完畢時，在 <div id="videos-0-items">底下，會出多 class = "video-item"
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, "video-item"))
        )
        # 將資料餵給 BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")
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
            print("title:", title.encode(sys.getfilesystemencoding()))
            print("link:", link.encode(sys.getfilesystemencoding()))
            print("autor_name:", autor_name.encode(sys.getfilesystemencoding()))
            print("autor_link:", autor_link.encode(sys.getfilesystemencoding()))
            print("watch:", watch.encode(sys.getfilesystemencoding()))
            print("=======================")

    except TimeoutException:
        print("Loading took too much time!")


def main():
    links = [
        ("https://www.youtube.com/trendsdashboard#loc0=twn&age0=--", "views_all"),
        (
            "https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&gen0=male",
            "views_male",
        ),
        (
            "https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&gen0=female",
            "views_female",
        ),
        (
            "https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared",
            "shared_all",
        ),
        (
            "https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared&gen0=male",
            "shared_male",
        ),
        (
            "https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared&gen0=female",
            "shared_female",
        ),
    ]

    """
    觀看次數最多
    全部   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--
    男性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&gen0=male
    女性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&gen0=female
  
    分享次數
    全部   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared
    男性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared&gen0=male
    女性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared&gen0=female
    """
    count = 0
    print("Start parsing... ")

    # 建立瀏覽器物件
    driver = webdriver.Firefox()  # 使用Firefox

    for link in links:
        count += 1
        # link[0] = URL   link[1] = tag
        driver.get(link[0])
        driver.refresh()
        crawler(driver, link[1])
        print("download: " + str(100 * count / len(links)) + " %.")

    driver.quit()  # 關閉瀏覽器並且退出驅動程序
    print("Completed")


if __name__ == "__main__":
    main()
