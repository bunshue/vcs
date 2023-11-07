import monitor_module as m  # ←匯入自訂模組並更名為 m
from email.mime.image import MIMEImage
import cv2


def get_mime_img(subject, fr, to, img):
    # 將 img 編碼為 JPGE 格式，[1]為返回資料, [0]為返回是否成功
    img_encode = cv2.imencode('.jpg', img)[1]
    # 再將資料轉為 bytes, 此即為要傳送的資料
    img_bytes = img_encode.tobytes()
    mime_img = MIMEImage(img_bytes)   # 建立 MIMEImage 物件
    mime_img['Content-type'] = 'application/octet-stream'
    mime_img['Content-Disposition'] = 'attachment; filename="pic.jpg"'
    mime_img['Subject'] = subject
    mime_img['From'] = fr
    mime_img['To'] = to
    return mime_img.as_string()  # ←轉為字串後傳回


gmail_addr = '您的Gmail郵件地址'
gmail_pwd = '您的Gmail密碼'
to_addrs = ['第一個收件者的郵件網路', '第二個收件者的郵件網路']

cap = cv2.VideoCapture(0)  # 打開攝影機
while cap.isOpened():
    success, img = cap.read()
    if success:
        cv2.imshow('frame', img)  # 在視窗中顯示影像
    k = cv2.waitKey(1)     # 讀取鍵盤輸入
    if k == ord('s'):  # ←如果按下 s 鍵
        msg = get_mime_img('小偷入侵', '鷹眼防盜監視器', '警察局', img)
        m.send_gmail(gmail_addr, gmail_pwd, to_addrs, msg)  # 以 gmail 寄出郵件
    elif k == ord('q'):   # 按下小寫 q 結束程式
        cv2.destroyAllWindows()
        cap.release()
        break
