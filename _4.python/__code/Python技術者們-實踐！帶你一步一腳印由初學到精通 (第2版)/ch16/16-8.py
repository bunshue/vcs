def face_add(img):                        # 建立自訂函式
    # 將 img 編碼為 jpg 格式，[1]返回資料, [0]返回是否成功
    img_encode = cv2.imencode('.jpg', img)[1]
    img_bytes = img_encode.tobytes()                # 再將資料轉為 bytes, 此即為要傳送的資料
    # 新增臉部資料的請求路徑
    face_url = f'{base}/persongroups/{gid}/persons/{pid}/persistedFaces'
    response = requests.post(face_url,              # POST 請求
                             headers=headers_stream,
                             data=img_bytes)
    if response.status_code == 200:
        print('新增臉部成功: ', response.json())
    else:
        print('新增臉部失敗: ', response.s)
