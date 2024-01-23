from pathlib import Path
import cv2
import datetime

infolder = "testfolder"
extlist = ["*.mp4", "*.mov"]

#【函數: 取得影片檔的播放時間】
def getplaytime(readfile):
    try:
        cap = cv2.VideoCapture(readfile)            #載入檔案
        frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)   #總影格數
        fps = cap.get(cv2.CAP_PROP_FPS)             #影格速率
        sec = int(frame / fps)                        #播放時間（秒）
        timestr = str(datetime.timedelta(seconds=sec))  #轉換成時分秒格式
        return sec, readfile + " " + timestr
    except:
        return 0, readfile + "：程式執行失敗。"
#【函數: 搜尋資料夾與子資料夾的影片檔】
def findfiles(infolder):
    totalsec = 0
    msg = ""
    for ext in extlist:                     #以多個副檔名調查
        filelist = []
        for p in Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
            filelist.append(str(p))         #新增至列表
        for filename in sorted(filelist):   #再替每個檔案排序
            val1, val2 = getplaytime(filename)
            totalsec += val1
            msg += val2 + "\n"
    totaltimestr = str(datetime.timedelta(seconds=totalsec))
    msg += "總播放時間 " + totaltimestr
    return msg

#【執行函數】
msg = findfiles(infolder)
print(msg)
