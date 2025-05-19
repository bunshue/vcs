# ch1_1.py
import cv2

img1 = cv2.imread("jk.jpg")  # 讀取影像
print(f"成功讀取 : {type(img1)}")
img2 = cv2.imread("none.jpg")  # 讀取影像
print(f"讀取失敗 : {type(img2)}")


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch01\ch1_2.py

# ch1_2.py
import cv2

img = cv2.imread("jk.jpg")  # 讀取影像
cv2.imshow("MyPicture", img)  # 顯示影像


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch01\ch1_3.py

# ch1_3.py
import cv2

img = cv2.imread("jk.jpg")  # 讀取影像
cv2.imshow("MyPicture", img)  # 顯示影像
cv2.destroyWindow("MyPicture")  # 關閉視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch01\ch1_4.py

# ch1_4.py
import cv2

img = cv2.imread("jk.jpg")  # 讀取影像
cv2.imshow("MyPicture", img)  # 顯示影像
ret_value = cv2.waitKey(0)  # 無限等待
cv2.destroyWindow("MyPicture")  # 關閉視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch01\ch1_5.py

# ch1_5.py
import cv2

img = cv2.imread("jk.jpg")  # 讀取影像
cv2.imshow("MyPicture", img)  # 顯示影像
ret_value = cv2.waitKey(5000)  # 等待 5 秒
cv2.destroyWindow("MyPicture")  # 關閉視窗
print(f"ret_value = {ret_value}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch01\ch1_5_1.py

# ch1_5_1.py
import cv2

img = cv2.imread("jk.jpg")  # 讀取影像
cv2.imshow("MyPicture", img)  # 顯示影像
ret_value = cv2.waitKey(0)  # 無限等待
if ret_value == ord("Q") or ret_value == ord("q"):
    cv2.destroyWindow("MyPicture")  # 關閉視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch01\ch1_6.py

# ch1_6.py
import cv2

cv2.namedWindow("MyPicture1")  # 使用預設
cv2.namedWindow("MyPicture2", cv2.WINDOW_NORMAL)  # 可以調整大小
img1 = cv2.imread("jk.jpg")  # 彩色讀取
img2 = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("MyPicture1", img1)  # 顯示影像img1
cv2.imshow("MyPicture2", img2)  # 顯示影像img2
cv2.waitKey(3000)  # 等待3秒
cv2.destroyWindow("MyPicture1")  # 刪除MyPicture1
cv2.waitKey(8000)  # 等待8秒
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch01\ch1_6_1.py

# ch1_6_1.py
import cv2

cv2.namedWindow("MyPicture1")  # 使用預設
cv2.namedWindow("MyPicture2", cv2.WINDOW_NORMAL)  # 可以調整大小
img1 = cv2.imread("jk.jpg")  # 彩色讀取
img2 = cv2.imread("jk.jpg", 0)  # 灰色讀取
cv2.imshow("MyPicture1", img1)  # 顯示影像img1
cv2.imshow("MyPicture2", img2)  # 顯示影像img2
cv2.waitKey(3000)  # 等待3秒
cv2.destroyWindow("MyPicture1")  # 刪除MyPicture1
cv2.waitKey(8000)  # 等待8秒
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch01\ch1_7.py

# ch1_7.py
import cv2

cv2.namedWindow("MyPicture")  # 使用預設
img = cv2.imread("jk.jpg")  # 彩色讀取
cv2.imshow("MyPicture", img)  # 顯示影像img
ret = cv2.imwrite("tmp_out1_7_1.tiff", img)  # 將檔案寫入out1_7_1.tiff
if ret:
    print("儲存檔案成功")
else:
    print("儲存檔案失敗")
ret = cv2.imwrite("tmp_out1_7_2.png", img)  # 將檔案寫入out1_7_2.png
if ret:
    print("儲存檔案成功")
else:
    print("儲存檔案失敗")
cv2.waitKey(3000)  # 等待3秒
cv2.destroyAllWindows()  # 刪除所有視窗


print("------------------------------------------------------------")  # 60個
