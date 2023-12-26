# ex17_8.py
from PIL import Image
import pytesseract
import time

carDict = {}
myPath = "d:\\Python\\ex\\"
while True:
    carPlate = input("請掃描或輸入車牌(Q/q代表結束) : ")
    if carPlate == 'Q' or carPlate == 'q':
        break
    carPlate = myPath + carPlate
    keyText = pytesseract.image_to_string(Image.open(carPlate))    
    if keyText in carDict:
        exitTime = time.asctime()
        print("車輛出場時間 : ", keyText, ":", exitTime)
        exitSecond = time.time()
        dxSecond = exitSecond - carDict[keyText]
        hour = dxSecond % 3600          # 由餘數判斷是否進位
        hours = dxSecond // 3600        # 計算小時數
        if hour != 0:
            hours += 1
        print("停車費用 : ", hours * 60, " 元 ")
        del carDict[keyText]
    else:
        entryTime = time.asctime()
        print("車輛入場時間 : ", keyText, ":", entryTime)
        entrySecond = time.time()
        carDict[keyText] = entrySecond



