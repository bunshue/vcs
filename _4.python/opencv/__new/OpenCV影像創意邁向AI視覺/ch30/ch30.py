"""
第三十章 建立哈爾特徵分類器—車牌辨識

要先準備 srcCar 和 notCar
正樣本影像 srcCar  90 => dstCar => bmpCar
負樣本影像 notCar 295 => 灰階 => notCarGray

code_aaa : srcCar => dstCar
code_bbb : dstCar => bmpCar
code_ccc : notCar => notCarGray

哈爾特徵分類器工具
https://github.com/raunakdoesdev/Haar-Training

下載後改名成 Haar-Training-car-plate.my

把正樣本影像(bmpCar/*) 放在 Haar-Training-car-plate.my/training/positive/rawdata/ 之下

把負樣本影像(notCarGray/*) 放在 Haar-Training-car-plate.my/training/negative/ 之下
保留create_list.bat 用來建立 bg.txt 建立之

為正樣本加上標記
Haar-Training-car-plate.my/training/positive/objectmarker.exe 執行之
滑鼠框選車牌，按 SPACE+ENTER 換下一張
資料儲存在info.txt裏

標記檢查
code_ddd : positive/rawdata + info.txt => plate_mark

建立向量檔案
正樣本影像 => 向量檔案
Haar-Training-car-plate.my/training/samples_creation.bat

createsamples.exe -info positive/info.txt -vec vector/facevector.vec -num 500 -w 80 -h 40
改成
createsamples.exe -info positive/info.txt -vec vector/facevector.vec -num 90 -w 70 -h 20

執行之, 產出 vector/facevector.vec 向量檔案

訓練哈爾分類器

刪除 Haar-Training-car-plate.my/training/cascades/ 下的內容

Haar-Training-car-plate.my/training/haarTraining.bat
改成
haartraining.exe -data cascades -vec vector/facevector.vec -bg negative/bg.txt -npos 90 -nneg 295 -nstages 15 -mem 512 -mode ALL -w 70 -h 20 -nonsym

執行之, 開始訓練, 久, 可以在 cascades之下看到結果


建立哈爾特徵分類器資源檔
編輯 cascade2xml/convert.bat

執行之

開始車牌偵測 testCar
# code_eee1 code_eee2 code_eee3

"""
print("------------------------------------------------------------")  # 60個

import cv2
import os
import sys
import glob
import time
import shutil

print("------------------------------------------------------------")  # 60個
'''
# code_aaa

srcDir = "srcCar"
dstDir = "dstCar"
width = 320
height = 240

print('圖片調整成相同大小(單層)', srcDir, '=>', dstDir)

# 刪除資料夾並重建之
if os.path.isdir(dstDir):
    shutil.rmtree(dstDir)  # 刪除資料夾
    time.sleep(3)  # 休息讓系統處理
os.mkdir(dstDir)  # 建立資料夾

# 圖片調整成相同大小(單層)
cars = glob.glob(srcDir + "/*.jpg")
for index, car in enumerate(cars, 1):               # 從1開始
    img_car = cv2.imread(car,cv2.IMREAD_COLOR)      # 讀車子影像
    img_car_resize = cv2.resize(img_car, (width, height))
    car_name = "car" + str(index) + ".jpg"          # 車子影像命名
    fullpath = dstDir + "\\" + car_name             # 完成路徑
    cv2.imwrite(fullpath, img_car_resize)           # 寫入車子影像

print("OK")
    
allcars = dstDir + "/*.JPG"                 # 建立檔案模式
""" many
cars = glob.glob(allcars)                   # 獲得檔案名稱
print(f"目前資料夾檔案名稱 = \n{cars}")     # 列印檔案名稱

# 拆解資料夾符號
for car in cars:
    carname = car.split("\\")               # 將字串轉成串列
    print(carname)
"""

print("------------------------------------------------------------")  # 60個

# code_bbb

dstDir = "dstCar"
bmpDir = "bmpCar"

# 刪除資料夾並重建之
if os.path.isdir(bmpDir):
    shutil.rmtree(bmpDir)  # 刪除資料夾
    time.sleep(3)  # 休息讓系統處理
os.mkdir(bmpDir)

allcars = dstDir + "/*.JPG"                         # 建立檔案模式
cars = glob.glob(allcars)                           # 獲得檔案名稱
#print(f"目前資料夾檔案名稱 = \n{cars}")            # 列印檔案名稱

# 拆解資料夾符號
for car in cars:
    carname = car.split("\\")                       # 將字串轉成串列
    #print(carname)
    car_img = cv2.imread(car,cv2.IMREAD_COLOR)  # 讀車子影像
    outname = carname[1].replace(".jpg", ".bmp")    # 將jpg改為bmp
    fullpath = bmpDir + "\\" + outname              # 完整檔名
    cv2.imwrite(fullpath, car_img)                  # 寫入資料夾
print("在 bmpCar 資料夾重新命名車輛副檔名成功")

print("------------------------------------------------------------")  # 60個

# code_ccc
# ch30_4.py

srcDir = "notCar"
dstDir = "notCarGray"
width = 500                                         # 負樣本寬     
height = 400                                        # 負樣本高

# 刪除資料夾並重建之
if os.path.isdir(dstDir):
    shutil.rmtree(dstDir)  # 刪除資料夾
    time.sleep(3)  # 休息讓系統處理
os.mkdir(dstDir)

allcars = srcDir + "/*.JPG"                         # 建立檔案模式
cars = glob.glob(allcars)                           # 獲得檔案名稱
for index, car in enumerate(cars, 1):
    img = cv2.imread(car,cv2.IMREAD_GRAYSCALE)      # 灰階讀車子影像
    img_resize = cv2.resize(img, (width, height))   # 調整負樣本影像
    imgname =  "notcar" + str(index)
    fullpath = dstDir + "\\" + imgname + ".jpg"
    cv2.imwrite(fullpath, img_resize)
print("在 notCar 資料夾將影像轉為灰階成功,同時存入notCarGray資料夾")

print("------------------------------------------------------------")  # 60個

# code_ddd 標記檢查
# ch30_5.py
# 標記檢查

dstDir = "plate-mark"
path = "Haar-Training-car-plate.my/training/positive/"

# 刪除資料夾並重建之
if os.path.isdir(dstDir):
    shutil.rmtree(dstDir)  # 刪除資料夾
    time.sleep(3)  # 休息讓系統處理
os.mkdir(dstDir)

fn = open(path + 'info.txt', 'r')
row = fn.readline()                                 # 讀取info.txt
while row:
    msg = row.split(' ')                            # 分割每一列文字
    img = cv2.imread(path + msg[0])                 # 讀檔案
    n = int(msg[1])
    for i in range(n):
        x = int(msg[2 + i * 4])                     # 取得左上方 x 座標
        y = int(msg[3 + i * 4])                     # 取得左上方 y 座標
        w = int(msg[4 + i * 4])                     # 取得 width 寬度
        h = int(msg[5 + i * 4])                     # 取得 height 高度
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    imgname = (msg[0].split("/"))[-1]               # 使用-1是確定最右索引
    print(imgname)                                  # 輸出處理過程
    cv2.imwrite(dstDir + "\\" + imgname, img)       # 寫入資料夾
    row = fn.readline()
fn.close()
print("繪製車牌框完成")
'''
print("------------------------------------------------------------")  # 60個

# code_eee1

pictPath = "haar_carplate.xml"                          # 哈爾特徵檔路徑
img = cv2.imread("testCar/cartest1.jpg")                # 讀辨識的影像
img = cv2.imread("testCar/cartest2.jpg")                # 讀辨識的影像
img = cv2.imread("testCar/cartest3.jpg")                # 讀辨識的影像

car_cascade = cv2.CascadeClassifier(pictPath)           # 讀哈爾特徵檔

# 執行辨識
plates = car_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=3,
         minSize=(20,20),maxSize=(155,50))  
if len(plates) > 0 :                                    # 有偵測到車牌
    for (x, y, w, h) in plates:                         # 標記車牌  
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print(plates)
else:
    print("偵測車牌失敗")

cv2.imshow('Car', img)                                  # 顯示所讀取的車輛
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


