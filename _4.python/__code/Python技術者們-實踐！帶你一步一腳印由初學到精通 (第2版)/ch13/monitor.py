import cv2
import monitor_module

#----------↓↓E-mail資料設定↓↓------------#
gmail_addr = '你的 Gmail 信箱'
gmail_pwd = '信箱密碼'
to_addrs = ['第一個收件者的 E-mail', '第二個收件者的 E-mail']
#----------↓↓簡訊資料設定↓↓------------#
sid = '你的 ACCOUNT SID'
token = '你的 AUTH TOKEN'
us_phone = '你的美國手機號碼'
tw_phone = '你的台灣手機號碼'

#--------------↓↓開啟攝影機開始運作↓↓------------------#
cap = cv2.VideoCapture(0)
skip = 1   # 設定不比對的次數, 由於前影像是空的, 略過一次比對

while cap.isOpened():
    success, img = cap.read()
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # 灰階處理
        img_now = cv2.GaussianBlur(gray, (13, 13), 5)       # 高斯模糊
        if skip > 0:  # ←如果 skip 大於 0 就略過不和前影像比對
            skip -= 1  # 將 skip 次數減 1
        else:  # ←如果 skip==0 就和前影像比對
            diff = cv2.absdiff(img_now, img_pre)   # 此影格與前影格的差異值

            #設定門檻值
            ret, thresh = cv2.threshold(diff, 25, 255,cv2.THRESH_BINARY)
            #找輪廓
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # 如果有偵測到輪廓
            if contours:
                cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
                """
                msg = monitor_module.get_mime_img('小偷入侵', '鷹眼防盜監視器', '警察局', img)
                monitor_module.send_gmail(gmail_addr, gmail_pwd,
                             to_addrs, msg)  # 以 gmail 寄出
                monitor_module.send_sms('小偷來了', sid, token, us_phone, tw_phone)
                """
                print('偵測到移動')
                skip = 10  # ←略過 N 次不比對
            else:
                print('靜止畫面')
        cv2.imshow('frame', img)
        img_pre = img_now.copy()

    k = cv2.waitKey(50)  # ←暫停 50 毫秒 (0.05 秒), 並檢查是否有按鍵輸入
    if k == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break
