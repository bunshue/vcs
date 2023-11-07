import requests
import cv2

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'    # api
key = '您的金鑰'                                                     # 你的金鑰
headers_stream = {'Ocp-Apim-Subscription-Key': key,     # 臉部偵測請求標頭
                  'Content-Type': 'application/octet-stream'}


def face_detect(img):
    detect_url = f'{base}/detect?returnFaceId=true'  # 臉部偵測的請求路徑
    # 將 img 編碼為 jpg 格式，[1]返回資料, [0]返回是否成功
    img_encode = cv2.imencode('.jpg', img)[1]
    img_bytes = img_encode.tobytes()                # 再將資料轉為 bytes, 此即為要傳送的資料
    response = requests.post(detect_url,
                             headers=headers_stream,
                             data=img_bytes)
    if response.status_code == 200:
        face = response.json()
        if not face:
            print("照片中沒有偵測到人臉")
        else:
            faceId = face[0]['faceId']              # 取得 FaceId
            return faceId
