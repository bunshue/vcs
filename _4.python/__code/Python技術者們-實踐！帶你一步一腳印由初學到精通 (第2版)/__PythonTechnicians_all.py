import sys
import os
import re
import cv2
import time
import requests
import pandas as pd
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

print("------------------------------------------------------------")  # 60個

'''
def get_price(url):
    data = requests.get(url)  # GET請求
    data_prices = data.json()["stats"]  # 解析json格式，並取出'status'對應到的值
    df = pd.DataFrame(data_prices)  # 將list轉為dataframe
    df.columns = ["datetime", "twd"]  # 設定欄索引名稱
    df["datetime"] = pd.to_datetime(df["datetime"], unit="ms")  # 將毫秒轉為時間日期格式
    df.index = df["datetime"]  # 設定列索引
    return df


url = "https://www.coingecko.com/price_charts/1/twd/90_days.json"
bitcoin = get_price(url)
# 利用'twd'欄位的值計算窗口為100的均線, 並加入bitcoin的dataframe之中
bitcoin["ma"] = bitcoin["twd"].rolling(window=100).mean()

# 以'twd'和'ma'欄位的值繪圖
bitcoin[["twd", "ma"]].plot(
    kind="line", figsize=[15, 5], xlim=("2021-01-20", "2021-01-27")
)

plt.show()

print("------------------------------------------------------------")  # 60個

import bitcoin_module as m


def strategy(df, total, ma_num, stop_earn):
    df["ma"] = df["twd"].rolling(window=ma_num).mean()
    df = df[ma_num - 1 :]  # 將前面的none值去掉
    entry_price = 0  # 進場點
    max_price = 0  # 最高點
    min_price = 0  # 最低點
    state = "wait_long"  # 設定初始狀態為'等待做多'
    for i in range(len(df)):
        # 等待做多
        if state == "wait_long":
            if df["twd"][i] > df["ma"][i]:
                max_price = df["twd"][i]
                entry_price = df["twd"][i]
                state = "entry_long"
        # 等待做空
        elif state == "wait_short":
            if df["twd"][i] < df["ma"][i]:
                min_price = df["twd"][i]
                entry_price = df["twd"][i]
                state = "entry_short"
        # 進場做多
        elif state == "entry_long":
            if df["twd"][i] > max_price:
                max_price = df["twd"][i]
            if df["twd"][i] < max_price:
                total += df["twd"][i] - entry_price
                state = "wait_short"
            elif df["twd"][i] - entry_price > stop_earn and stop_earn != 0:
                total += df["twd"][i] - entry_price
                state = "wait_short"
        # 進場做空
        elif state == "entry_short":
            if df["twd"][i] < min_price:
                min_price = df["twd"][i]
            if df["twd"][i] > min_price:
                total += entry_price - df["twd"][i]
                state = "wait_long"
            elif entry_price - df["twd"][i] > stop_earn and stop_earn != 0:
                total += entry_price - df["twd"][i]
                state = "wait_long"
    return total


url = "https://www.coingecko.com/price_charts/1/twd/90_days.json"
bitcoin = m.get_price(url)
total = strategy(bitcoin, 1000000, 200, 1000)
# 期初資金為100萬, 均線為200, 停利點為1000

print("顯示出淨值 : ")
print(total)  # 顯示出淨值

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base = "https://japanwest.api.cognitive.microsoft.com/vision/v3.1/read/analyze?%"
recog_url = f"{base}/recognizeText?mode=Printed"
key = "您的金鑰"
# 查看結果的請求標頭
headers = {"Ocp-Apim-Subscription-Key": key}
headers_stream = {
    "Ocp-Apim-Subscription-Key": key,  # 辨識的請求標頭
    "Content-Type": "application/octet-stream",
}


def get_license(img):
    # 將 img 編碼為 jpg 格式，[1]返回資料, [0]返回是否成功
    img_encode = cv2.imencode(".jpg", img)[1]
    img_bytes = img_encode.tobytes()  # 再將資料轉為 bytes, 此即為要傳送的資料
    r1 = requests.post(recog_url, headers=headers_stream, data=img_bytes)  # 發出 POST
    if r1.status_code != 202:  # 202 代表接受請求
        print(r1.json())
        return "請求失敗"
    # --↓↓辨識請求成功↓↓--#
    result_url = r1.headers["Operation-Location"]  # 取得查看結果的請求路徑
    r2 = requests.get(result_url, headers=headers)  # 發出 GET 請求
    while r2.status_code == 200 and r2.json()["status"] != "succeeded":
        r2 = requests.get(result_url, headers=headers)  # 繼續發出 GET
        time.sleep(0.5)
        print("status: ", r2.json()["status"])  # 顯示辨識狀態

    # --↓↓辨識完成↓↓--#
    carcard = ""  # 紀錄車牌
    lines = r2.json()["analyzeResult"]["readResults"][0]["lines"]
    for i in range(len(lines)):
        text = lines[i]["text"]  # 取得辨識文字
        m = re.match(r"^[\w]{2,4}[-. ][\w]{2,4}$", text)  # 匹配是否為車牌格式
        if m != None:  # 匹配成功
            carcard = m.group()
            return carcard
    if carcard == "":  # 無匹配結果
        return "找不到車牌"


try:
    img = cv2.imread("car.jpg")  # 讀取圖片
    print("status:  Start")
    text = get_license(img)  # 辨識圖片中的車牌
    print("車牌：", text)
    cv2.imshow("Frame", img)  # 顯示圖片
    cv2.waitKey(0)  # 等待
    cv2.destroyAllWindows()  # 關閉視窗
except:
    print("讀取圖片失敗")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# 從麥克風讀取聲音

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
"""
'''
response = requests.get(" https://zh.wikipedia.org/zh-tw/愛因斯坦")
if response.status_code == 200:
    print(response.text)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def bot_get_wiki(keyword):
    response = requests.get("https://zh.wikipedia.org/zh-tw/" + keyword)
    bs = BeautifulSoup(response.text, "lxml")
    p_list = bs.find_all("p")
    for p in p_list:
        if keyword in p.text[0:10]:
            return p.text


content = bot_get_wiki("愛因斯坦")
print(content)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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


sentence = "阿爾伯特·愛因斯坦，或譯亞伯特·愛因斯坦（德語：Albert Einstein，1879年3月14日－1955年4月18日），猶太裔理論物理學家，創立了現代物理學的兩大支柱之一的相對論[註 2][2]:274[1]，也是質能等價公式（E = mc2）的發現者[3]。"
bot_speak_re(sentence)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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
        print(response.text)
        bs = BeautifulSoup(response.text, "lxml")
        wiki_url = bs.find("cite")
        # kwd = wiki_url.text.split('/')[-1]
        kwd = wiki_url.text.split("›")[-1].replace(" ", "")  # 修正
        keyword_trad = HanziConv.toTraditional(kwd)
        return keyword_trad
    else:
        print("請求失敗")


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

base = "https://japanwest.api.cognitive.microsoft.com/face/v1.0"  # api
gp_url = base + "/persongroups/gp01"  # 創建群組的請求路徑
key = "您的金鑰"  # 你的 key
headers_json = {
    "Ocp-Apim-Subscription-Key": key,  # 請求標頭
    "Content-Type": "application/json",
}
body = {"name": "旗標科技公司", "userData": "位於台北市"}  # 建立請求主體內容
body = str(body).encode("utf-8")  # 請求主體的編碼

response = requests.put(gp_url, headers=headers_json, data=body)  # HTTP PUT
if response.status_code == 200:  # 請求成功返回狀態碼 200
    print("創建群組成功")
else:
    print("創建失敗:", response.json())  # 印出創建失敗原因

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base = "https://japanwest.api.cognitive.microsoft.com/face/v1.0"  # api
gp_url = base + "/persongroups/gp01"  # 創建群組的請求路徑
key = "您的金鑰"  # 你的 key
headers = {"Ocp-Apim-Subscription-Key": key}  # 請求標頭
response = requests.get(gp_url, headers=headers)  # HTTP GET
if response.status_code == 200:
    print(response.json())
else:
    print("查詢失敗", response.json())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base = "https://japanwest.api.cognitive.microsoft.com/face/v1.0"  # api
pson_url = f"{base}/persongroups/gp01/persons"  # 新增人員的請求路徑
key = "您的金鑰"  # 你的 key
headers_json = {
    "Ocp-Apim-Subscription-Key": key,  # 請求標頭
    "Content-Type": "application/json",
}
body = {"name": "周詠", "userData": "苗栗人"}  # 建立請求主體內容
body = str(body).encode("utf-8")  # 請求主體的編碼

response = requests.post(pson_url, headers=headers_json, data=body)  # HTTP POST
if response.status_code == 200:
    print("新增人員完成: ", response.json())
else:
    print("新增失敗:", response.json())  # 印出創建失敗原因

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base = "https://japanwest.api.cognitive.microsoft.com/face/v1.0"  # api
key = "您的金鑰"  # 你的 key
headers = {"Ocp-Apim-Subscription-Key": key}  # 請求標頭


def person_list(gid):
    pson_url = base + f"/persongroups/{gid}/persons"  # 查看群組人員的請求路徑
    response = requests.get(pson_url, headers=headers)  # HTTP GET
    if response.status_code == 200:
        print("查詢人員完成")
        return response.json()
    else:
        print("查詢人員失敗:", response.json())  # 印出創建失敗原因


persons = person_list("gp01")  # 查詢群組 gp01 的成員清單
print(persons)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def face_add(img):  # 建立自訂函式
    # 將 img 編碼為 jpg 格式，[1]返回資料, [0]返回是否成功
    img_encode = cv2.imencode(".jpg", img)[1]
    img_bytes = img_encode.tobytes()  # 再將資料轉為 bytes, 此即為要傳送的資料
    # 新增臉部資料的請求路徑
    face_url = f"{base}/persongroups/{gid}/persons/{pid}/persistedFaces"
    response = requests.post(
        face_url, headers=headers_stream, data=img_bytes  # POST 請求
    )
    if response.status_code == 200:
        print("新增臉部成功: ", response.json())
    else:
        print("新增臉部失敗: ", response.s)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import face_module as m  # 匯入自訂模組

base = "https://japanwest.api.cognitive.microsoft.com/face/v1.0"  # api
key = "您的金鑰"  # 你的金鑰
gid = "gp01"  # 群組 Id
pid = "8d649904-55b4-4dce-a834-b4dfcdb0b667"  # 成員 Id

m.face_init(base, key)  # 初始化端點和金鋪
m.face_use(gid, pid)  # 指定要操作的 gid 和 pid
m.face_shot("add")  # 不斷進行拍照並上傳到Azuse新增成員人臉影像

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base = "https://japanwest.api.cognitive.microsoft.com/face/v1.0"  # api
gId = "gp01"  # 要訓練的群組
train_url = f"{base}/persongroups/{gId}/train"  # 請求路徑
key = "您的金鑰"  # 你的金鑰
headers = {"Ocp-Apim-Subscription-Key": key}  # 請求標頭
response = requests.post(train_url, headers=headers)  # POST 請求
if response.status_code == 202:
    print("開始訓練...")
else:
    print("訓練失敗", response.json())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base = "https://japanwest.api.cognitive.microsoft.com/face/v1.0"  # api
gId = "gp01"  # 要訓練的群組
train_url = f"{base}/persongroups/{gId}/training"  # 請求路徑
key = "您的金鑰"  # 你的金鑰
headers = {"Ocp-Apim-Subscription-Key": key}  # 請求標頭
response = requests.get(train_url, headers=headers)  # GET 請求
if response.status_code == 200:
    print("訓練結果：", response.json())
else:
    print("查看失敗", response.json())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base = "https://japanwest.api.cognitive.microsoft.com/face/v1.0"  # api
key = "您的金鑰"  # 你的金鑰
headers_stream = {
    "Ocp-Apim-Subscription-Key": key,  # 臉部偵測請求標頭
    "Content-Type": "application/octet-stream",
}


def face_detect(img):
    detect_url = f"{base}/detect?returnFaceId=true"  # 臉部偵測的請求路徑
    # 將 img 編碼為 jpg 格式，[1]返回資料, [0]返回是否成功
    img_encode = cv2.imencode(".jpg", img)[1]
    img_bytes = img_encode.tobytes()  # 再將資料轉為 bytes, 此即為要傳送的資料
    response = requests.post(detect_url, headers=headers_stream, data=img_bytes)
    if response.status_code == 200:
        face = response.json()
        if not face:
            print("照片中沒有偵測到人臉")
        else:
            faceId = face[0]["faceId"]  # 取得 FaceId
            return faceId


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base = "https://japanwest.api.cognitive.microsoft.com/face/v1.0"  # api
key = "您的金鑰"  # 你的金鑰
headers_json = {"Ocp-Apim-Subscription-Key": key, "Content-Type": "application/json"}


def face_identify(faceId):
    # 臉部偵測的請求路徑
    idy_url = f"{base}/identify"
    body = str({"personGroupId": "群組 id", "faceIds": [faceId]})
    response = requests.post(idy_url, headers=headers_json, data=body)  # 臉部驗證請求 POST
    if response.status_code == 200:
        person = response.json()
        if not person[0]["candidates"]:
            print("找不到相符的身分")
            return None
        else:
            print(person)
            personId = person[0]["candidates"][0]["personId"]  # 取得 personId
            print(personId)
            return personId


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
