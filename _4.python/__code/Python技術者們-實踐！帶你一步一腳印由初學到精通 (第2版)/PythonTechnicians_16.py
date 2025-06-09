print("------------------------------------------------------------")  # 60個

import sqlite3
from datetime import datetime


def db_save(db, name):
    connect = sqlite3.connect(db)  # 與資料庫連線
    # 新建 mytable 資料表  (如果尚未建立的話)
    sql = 'CREATE TABLE IF NOT EXISTS mytable \
            ("姓名" TEXT, "打卡時間" TEXT)'
    connect.execute(sql)  # 執行 SQL 語法
    # 取得現在時間
    save_time = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    # 新增一筆資料的 SQL 語法
    sql = f'insert into mytable values("{name}", "{save_time}")'
    connect.execute(sql)  # 執行 SQL 語法
    connect.commit()  # 更新資料庫
    connect.close()  # 關閉資料庫
    print("儲存成功")

    # ------------------------------#


db_save("mydatabase.sqlite", "丹丹")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import sqlite3


def db_check(db):
    try:
        connect = sqlite3.connect(db)  # 與資料庫連線
        sql = "select * from mytable"  # 選取資料表中所有資料的 SQL 語法
        cursor = connect.execute(sql)  # 執行 SQL 語法得到 cursor 物件
        dataset = cursor.fetchall()  # 取得所有資料
        print("姓名\t打卡時間")
        print("----\t  ----")
        for data in dataset:
            print(f"{data[0]}\t{data[1]}")
    except:
        print("讀取資料庫錯誤")
    connect.close()

    # ---------------------------#


db_check("mydatabase.sqlite")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests

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

import requests

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

import requests

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

import requests

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


# ------------------------------------#
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

import requests

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

import requests

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

import requests
import cv2

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

import requests

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
