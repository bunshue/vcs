print("------------------------------------------------------------")  # 60個

import speech_recognition as sr  # 匯入套件並命名為 sr


def bot_listen():
    recong = sr.Recognizer()  # 建立辨識物件
    with sr.Microphone() as source:  # 打開麥克風取得聲音
        audioData = recong.listen(source)  # 讓辨識物件聽到的聲音
    try:
        text = recong.recognize_google(audioData, language="zh-tw")  # 將聲音資料翻成文字
        return text
    except:
        return "聽不懂"


question = bot_listen()
print(question)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests

response = requests.get(" https://zh.wikipedia.org/zh-tw/愛因斯坦")
if response.status_code == 200:
    print(response.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
import requests


def bot_get_wiki(keyword):
    response = requests.get("https://zh.wikipedia.org/zh-tw/" + keyword)
    bs = BeautifulSoup(response.text, "lxml")
    p_list = bs.find_all("p")
    for p in p_list:
        if keyword in p.text[0:10]:
            return p.text


# ---------------------------------------#
content = bot_get_wiki("愛因斯坦")
print(content)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import re
import chatBot_module as m


def bot_speak_re(sentence):
    s1 = re.sub(r"\[[^\]]*\]", "", sentence)
    print(s1)
    en_list = re.findall(r"[a-zA-Z ]+", s1)
    s2 = re.sub(r"[a-zA-Z \-]+", "@English@", s1)
    all_list = s2.split("@")
    index = 0
    for text in all_list:
        if text != "English":
            m.bot_speak(text, "zh-tw")
        else:
            m.bot_speak(en_list[index], "en")
            index += 1


# -----------------------------------------------#
sentence = "阿爾伯特·愛因斯坦，或譯亞伯特·愛因斯坦（德語：Albert Einstein，1879年3月14日－1955年4月18日），猶太裔理論物理學家，創立了現代物理學的兩大支柱之一的相對論[註 2][2]:274[1]，也是質能等價公式（E = mc2）的發現者[3]。"
bot_speak_re(sentence)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
from hanziconv import HanziConv


def bot_get_google(question):
    url = f"https://www.google.com.tw/search?q={question}+維基百科"
    # 以下是要在 get 的表頭加上瀏覽器的資訊, 以偽裝成瀏覽器
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


# ----------------------------------------#
keyword = bot_get_google("誰是愛因斯坦")
print(keyword)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import chatBot_module as m

question = ""
answer = ""
QA = {"你是誰": "我是萱萱", "聽不懂": "請再說一次問題"}

question = m.bot_listen()  # 打開耳朵聽問題
print(question)
if question in QA:  # 如果問題存於 QA 字典中
    answer = QA[question]  # 取出問題的答案
    m.bot_speak(answer, "zh-tw")  # 唸出答案
    print(answer)
else:  # 問題不存於 QA 字典中, 進行網路爬蟲
    print("進行網路爬蟲")  # 爬蟲功能稍後加入


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
