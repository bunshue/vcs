# ch34_2.py
import cv2
cv2.namedWindow("MyPicture")            # 使用預設
img = cv2.imread("jk.jpg")              # 彩色讀取
cv2.imshow("MyPicture", img)            # 顯示影像img
cv2.imwrite("out34_2.jpg", img)         # 將檔案寫入out34_2.jpg
cv2.waitKey(3000)                       # 等待3秒
cv2.destroyAllWindows()                 # 刪除所有視窗






 
