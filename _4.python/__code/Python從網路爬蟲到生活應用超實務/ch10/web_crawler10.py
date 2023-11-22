import sys
from selenium import webdriver
'''
url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for tag in tags:
    href = tag.get_attribute('href')
    if href:
        links.append(href)
        print(href)
print(len(links))
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tags = soup.select("#video-title")
links = []
for tag in tags:
    href = tag["href"]
    if href:
        links.append(href)
        print(href)
print(len(links))
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for tag in tags:
    href = tag.get_attribute('href')
    links.append(href)
print(len(links))

wait = WebDriverWait(driver, 10)
for link in links:
    driver.get(link)
    num = link.strip('https://www.youtube.com/watch?v=')
    title = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"div#container > h1"))).text
    description =  wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"div#description"))).text
    print("編號:", num)
    print("名稱:", title.strip())
    print("描述:", description.strip())
    print("---------------------------")
driver.quit()
'''
print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
print("正在下載影片:", yt.title)
video = yt.streams.first()
video.download()
print("影片下載完成...")

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-2-1a.py

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
print("正在下載影片:", yt.title)
yt.streams.first().download()
print("影片下載完成...")


sys.exit()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-2-1b.py

from pytube import YouTube
import os

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
print("正在下載影片:", yt.title)
pathdir = "Arduino"
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)
yt.streams.first().download(pathdir)
print("影片下載完成...")

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-2-2.py

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
print("影片名稱:", yt.title)
print("影片作者:", yt.author)
print("影片長度:", yt.length, "秒")
print("縮圖網址:", yt.thumbnail_url)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-2-2a.py

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
videos = yt.streams
print("影片格式數:", len(videos))
print("第1個:", videos.first())
print("第1個:", videos[0])
print("最後1個:", videos.last())

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-2-3.py

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
videos = yt.streams

results = videos.filter(progressive=True)
print("符合的影片數:", len(results))
print("第1個:", results.first())


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-2-3a.py

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
videos = yt.streams

results = videos.filter(adaptive=True)
print("符合的影片數:", len(results))
print("第1個:", results.first())


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-2-3b.py

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
videos = yt.streams

results = videos.filter(subtype="mp4",res="720p")
print("符合的影片數:", len(results))
print("第1個:", results.first())

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-3-1.py

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=9bZkp7q19f0")
results = yt.streams.filter(only_audio=True)
print("符合的影片數:", len(results))
print(results)
results[0].download()
print("下載完成...")

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-3-1a.py

from pytube import YouTube
from moviepy.editor import VideoFileClip

filename = "test"
yt = YouTube("https://www.youtube.com/watch?v=I0Btsq2bdRk&t=34s")
videos = yt.streams
results = videos.filter(subtype="mp4")
print("符合的影片數:", len(results))
print("第1個:", results.first())
results.first().download(filename=filename)

clip = VideoFileClip(filename + ".mp4")
clip.audio.write_audiofile(filename + ".mp3")


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-3-2.py

from pytube import YouTube

yt = YouTube("https://youtube.com/watch?v=XJGiS83eQLk")
captions = yt.captions
print("符合的字幕數:", len(captions))
print(captions)


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-3-2a.py

from pytube import YouTube

yt = YouTube("https://youtube.com/watch?v=XJGiS83eQLk")
caption = yt.captions["en"]
srt = caption.generate_srt_captions()
with open("youtube.srt", "w", encoding="utf-8") as fp:
    fp.write(srt)
print("字幕檔下載完成...")

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-4.py

from pytube import Playlist
import re

url = "https://www.youtube.com/watch?v=c9IeFunTWbU&list=PLOq648KQvJ234tvAIQAluCTyuhjYmZrHa&index=2&t=0s"
playlist = Playlist(url)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))
for url in playlist.video_urls:
    print(url)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-4a.py

from pytube import Playlist
from pytube import YouTube
import re, os

url = "https://www.youtube.com/watch?v=c9IeFunTWbU&list=PLOq648KQvJ234tvAIQAluCTyuhjYmZrHa&index=2&t=0s"
playlist = Playlist(url)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print(len(playlist.video_urls))
  
pathdir = "download"
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)
for url in playlist.video_urls:
    yt = YouTube(url)
    print("正在下載影片:", yt.title)
    video = yt.streams.first()
    video.download(pathdir)
print("影片清單下載完成...")
 
    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch10\ch10-5.py

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)

for x in range(5):
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(5)

tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for tag in tags:
    href = tag.get_attribute('href')
    if href:
        links.append(href)
print(len(links))

df = pd.DataFrame(columns=["id", "title", "description"])
wait = WebDriverWait(driver, 10)
for link in links:
    driver.get(link)
    num = link.strip('https://www.youtube.com/watch?v=')
    title = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"div#container > h1"))).text
    description =  wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"div#description"))).text
    df.loc[len(df)] = [num, title, description]
    
print(df.head())    
df.to_csv("YouTube.csv",index=False,encoding="utf-8")
driver.quit()

print('------------------------------------------------------------')	#60個

