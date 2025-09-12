#  機器人的耳朵函式
from bs4 import BeautifulSoup
from hanziconv import HanziConv
import os
import re
import requests
import speech_recognition as sr


def bot_listen():
    recong = sr.Recognizer()  # 建立辨識物件
    with sr.Microphone() as source:  # 打開麥克風取得聲音
        audioData = recong.listen(source)  # 讓辨識物件聽到的聲音
    try:
        text = recong.recognize_google(audioData, language="zh-tw")  # 將聲音資料翻成文字
        return text
    except:
        return "聽不懂"


# 	抓取維基百科愛因斯坦網頁內的文章第一段


def bot_get_wiki(keyword):
    response = requests.get("https://zh.wikipedia.org/zh-tw/" + keyword)
    bs = BeautifulSoup(response.text, "lxml")
    p_list = bs.find_all("p")
    for p in p_list:
        if keyword in p.text[0:10]:
            return p.text


# 唸出常規表達式處理後的字串


def bot_speak_re(sentence):
    s1 = re.sub(r"\[[^\]]*\]", "", sentence)
    print(s1)
    en_list = re.findall(r"[a-zA-Z ]+", s1)
    s2 = re.sub(r"[a-zA-Z \-]+", "@English@", s1)
    all_list = s2.split("@")
    index = 0
    for text in all_list:
        if text != "English":
            print(text)
        else:
            bot_speak(en_list[index], "en")
            index += 1


# 對 Google 搜尋結果進行網路爬蟲


def bot_get_google(question):
    url = "https://www.google.com.tw/search?q=" + question + "+維基百科"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/70.0.3538.102 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, "lxml")
        wiki_url = bs.find("cite")
        # kwd = wiki_url.text.split('/')[-1]
        kwd = wiki_url.text.split("›")[-1].replace(" ", "")  # 修正
        keyword_trad = HanziConv.toTraditional(kwd)
        return keyword_trad
    else:
        print("請求失敗")
