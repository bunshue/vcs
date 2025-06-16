import sqlite3
import cv2
from datetime import datetime
import time
import requests

# 偵測正面人臉 haarcascade_frontalface_default.xml
xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"

base = ""  # api
key = ""  # 你的金鑰
headers_stream = {}  # stream 請求標頭
headers_json = {}  # json 請求標頭
headers = {}  # GET 的請求標頭


def face_init(b, k):
    global base, key, headers_stream, headers_json, headers
    base = b  # api
    key = k
    headers_stream = {
        "Ocp-Apim-Subscription-Key": key,  # stream 請求標頭
        "Content-Type": "application/octet-stream",
    }
    headers_json = {
        "Ocp-Apim-Subscription-Key": key,  # json 請求標頭
        "Content-Type": "application/json",
    }
    headers = {"Ocp-Apim-Subscription-Key": key}  # GET 的請求標頭


gid = ""  # 群組 Id
pid = ""  # 成員 Id


def face_use(g, p):
    global gid, pid
    gid = g
    pid = p


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
        print("新增臉部成功")
    else:
        print("新增臉部失敗:", response.text)


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


def face_identify(faceId):
    idy_url = f"{base}/identify"  # 臉部偵測的請求路徑
    body = str({"personGroupId": gid, "faceIds": [faceId]})
    response = requests.post(idy_url, headers=headers_json, data=body)  # 臉部驗證請求 POST
    if response.status_code == 200:
        person = response.json()
        if not person[0]["candidates"]:
            return None
        else:
            personId = person[0]["candidates"][0]["personId"]  # 取得 personId
            print(personId)
            return personId


def face_who(img):
    faceId = face_detect(img)  # 執行臉部偵測, 取得 faceId
    personId = face_identify(faceId)  # 用 faceId 進行臉部辨識, 找出群組中最像的人, 取得 personId
    if personId == None:
        print("查無相符身分")
    else:
        persons = person_list(gid)  # 取得群組的成員清單
        for p in persons:  # 取得清單中 personId 的姓名資訊
            if personId == p["personId"]:
                print("歡迎:", p["name"])
                db_save("mydatabase.sqlite", p["name"])  # 存入資料庫
                db_check("mydatabase.sqlite")  # 查看資料庫


def person_list(gid):
    pson_url = f"{base}/persongroups/{gid}/persons"  # 查看群組人員的請求路徑
    response = requests.get(pson_url, headers=headers)  # HTTP GET
    if response.status_code == 200:
        print("查詢人員完成")
        return response.json()
    else:
        print("查詢人員失敗:", response.json)  # 印出創建失敗原因


def db_save(db, name):
    connect = sqlite3.connect(db)  # 與資料庫連線
    # 新建 mytable 資料表  (如果尚未建立的話)
    sql = 'CREATE TABLE IF NOT EXISTS mytable \
            ("姓名" TEXT, "打卡時間" TEXT)'
    connect.execute(sql)  # 執行 SQL 語法
    # 取得現在時間
    save_time = str(datetime.now().strftime("%Y-%m-%d %H.%M.%S"))
    # 新增一筆資料的 SQL 語法
    sql = f'insert into mytable values("{name}", "{save_time}")'
    connect.execute(sql)  # 執行 SQL 語法
    connect.commit()  # 更新資料庫
    connect.close()  # 關閉資料庫


def db_check(db):
    try:
        connect = sqlite3.connect(db)  # 與資料庫連線
        connect.row_factory = sqlite3.Row  # 設定成 Row 物件
        sql = "select * from mytable"  # 選取資料表中所有資料的 SQL 語法
        cursor = connect.execute(sql)  # 執行 SQL 語法得到 cursor 物件
        dataset = cursor.fetchall()  # 取得所有資料
        col1 = dataset[0].keys()[0]  # 取得第一筆資料的第一個欄位名稱
        col2 = dataset[0].keys()[1]  # 取得第一筆資料的第二個欄位名稱
        print(f"{col1}\t{col2}")
        print("----\t  ----")
        for data in dataset:
            print(f"{data[0]}\t{data[1]}")
    except:
        print("讀取資料庫錯誤")
    connect.close()


# -----------------------------------#
def face_shot(function):
    isCnt = False  # 用來判斷是否正在進行倒數計時中
    face_detector = cv2.CascadeClassifier(xml_filename)  # 建立臉部辨識物件
    capture = cv2.VideoCapture(0)  # 開啟編號 0 的攝影機
    while capture.isOpened():  # 判斷攝影機是否開啟成功
        sucess, img = capture.read()  # 讀取攝影機影像
        if not sucess:
            print("讀取影像失敗")
            continue
        img_copy = img.copy()  # 複製影像
        faces = face_detector.detectMultiScale(  # 從攝影機影像中偵測人臉
            img, scaleFactor=1.1, minNeighbors=5, minSize=(200, 200)
        )
        if len(faces) == 1:  # 如果偵測到一張人臉
            if isCnt == False:
                t1 = time.time()  # 紀錄現在的時間
                isCnt = True  # 告訴程式目前進入倒數狀態
            cnter = 5 - int(time.time() - t1)  # 更新倒數計時器
            for x, y, w, h in faces:  # 畫出人臉位置
                cv2.rectangle(  # 繪製矩形
                    img_copy, (x, y), (x + w, y + h), (0, 255, 255), 2
                )
                cv2.putText(  # 繪製倒數數字
                    img_copy,
                    str(cnter),
                    (x + int(w / 2), y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2,
                )
            if cnter == 0:  # 倒數結束
                isCnt = False  # 告訴程式離開倒數狀態
                filename = datetime.now().strftime("%Y-%m-%d %H.%M.%S")  # 時間格式化
                cv2.imwrite(filename + ".jpg", img)  # 儲存影像檔案
                # -----------------------------------------#
                if function == "add":  # 打卡系統新增人員
                    face_add(img)
                elif function == "who":  # 進行人臉身分識別功能
                    face_who(img)
                # -----------------------------------------#
        else:  # 如果不是一張人臉
            isCnt = False  # 設定非倒數狀態

        cv2.imshow("Frame", img_copy)  # 顯示影像
        k = cv2.waitKey(1)  # 讀取按鍵輸入(若無會傳回 -1)
        if k == ord("q") or k == ord("Q"):  # 按下 q 離開迴圈, 結束程式
            print("exit")
            cv2.destroyAllWindows()  # 關閉視窗
            capture.release()  # 關閉攝影機
            break  # 離開無窮迴圈, 結束程式
    else:
        print("開啟攝影機失敗")


base = "https://japanwest.api.cognitive.microsoft.com/face/v1.0"  # api
key = "你的金鑰"  # 你的金鑰
gid = "gp01"  # 群組 Id
pid = "8d649904-55b4-4dce-a834-b4dfcdb0b667"  # 成員 Id

face_init(base, key)  # 初始化金鑰
face_use(gid, "8d649904-55b4-4dce-a834-b4dfcdb0b667")  # 指定要操作的 gid 和 pid
face_shot("who")  # 呼叫拍照函式來拍照並上傳到Azuse新增成員人臉影像


