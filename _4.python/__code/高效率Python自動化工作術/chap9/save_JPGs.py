from pathlib import Path
from PIL import Image

# 【2. 設定於應用程式顯示的字串】
infolder = "testfolder"
label1, value1 = "轉存資料夾", "outputfolder4"
extlist = ["*.jpg", "*.png"]


# 【3.函數: 儲存png檔案】
def savepng(readfile, savefolder):
    try:
        img = Image.open(readfile)  # 載入圖片檔
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)  # 建立轉存資料夾
        # -----------------------------------
        filename = Path(readfile).stem + ".jpg"  # 建立檔案名稱
        savepath = savedir.joinpath(filename)
        if img.format == "PNG":
            newimg = Image.new("RGB", img.size, "white")
            newimg.paste(img, mask=img.split()[3])  # 在白底背景繪製圖片
            newimg.save(savepath, format="JPEG", quality=95)  # 轉存為JPG圖檔
        elif img.format == "JPEG":
            img.save(savepath, format="JPEG", quality=95)  # 轉存為JPG圖檔
        # -----------------------------------
        msg = "在" + savefolder + "轉存" + filename + "了喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"


# 【函數: 處理資料夾之內的圖片檔】
def savefiles(infolder, savefolder):
    msg = ""
    for ext in extlist:  # 以多個副檔名調查
        filelist = []
        for p in Path(infolder).glob(ext):  # 將這個資料夾的檔案
            filelist.append(str(p))  # 新增至列表
        for filename in sorted(filelist):  # 再替每個檔案排序
            msg += savepng(filename, savefolder)
    return msg


msg = savefiles(infolder, value1)
