# ch34_3.py
import cv2
cv2.namedWindow("MyPicture")                            # 使用預設
img = cv2.imread("antarctica3.jpg")                     # 彩色讀取
cv2.line(img,(100,100),(1200,100),(255,0,0),2)          # 輸出線條
cv2.rectangle(img,(100,200),(1200,400),(0,0,255),2)     # 輸出矩陣
cv2.putText(img,"I Like Python",(400,350),              # 輸出文字
            cv2.FONT_ITALIC,3,(255,0,0),8)
cv2.imshow("MyPicture", img)                            # 顯示影像img
cv2.waitKey(3000)                                       # 等待3秒
cv2.destroyAllWindows()                                 # 刪除所有視窗






 
