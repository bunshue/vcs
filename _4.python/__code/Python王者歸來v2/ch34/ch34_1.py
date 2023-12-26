# ch34_1.py
import cv2
cv2.namedWindow("MyPicture1")                       # 使用預設
cv2.namedWindow("MyPicture2", cv2.WINDOW_NORMAL)    # 可以調整大小
img1 = cv2.imread("jk.jpg")                         # 彩色讀取
img2 = cv2.imread("jk.jpg", 0)                      # 灰色讀取
cv2.imshow("MyPicture1", img1)                      # 顯示影像img1
cv2.imshow("MyPicture2", img2)                      # 顯示影像img2
cv2.waitKey(3000)                                   # 等待3秒
cv2.destroyWindow("MyPicture1")                     # 刪除MyPicture1
cv2.waitKey(3000)                                   # 等待3秒
cv2.destroyAllWindows()                             # 刪除所有視窗






 
