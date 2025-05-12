from pathlib import Path
from PIL import Image
from PIL import ImageDraw

print("------------------------------------------------------------")  # 60個
print("redline_PNGs")
print("------------------------------------------------------------")  # 60個

infolder = "testfolder"
value1 = "outputfolder3"
extlist = ["*.jpg", "*.png"]


# 【函數: 儲存png檔案】
def savepng(readfile, savefolder):
    try:
        img = Image.open(readfile)  # 載入圖片檔
        # -----------------------------------
        draw = ImageDraw.Draw(img)
        draw.line((0, 0, img.width, img.height), fill="RED", width=8)
        # -----------------------------------
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)  # 建立轉存資料夾
        filename = Path(readfile).stem + ".png"  # 建立檔案名稱
        img.save(savedir.joinpath(filename), format="PNG")  # 以png格式轉存
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


# 【執行函數】
msg = savefiles(infolder, value1)
print(msg)



print("------------------------------------------------------------")  # 60個
print("resize_PNGs")
print("------------------------------------------------------------")  # 60個

infolder = "testfolder"
value1 = "outputfolder2"
value2 = "100"
extlist = ["*.jpg", "*.png"]


# 【函數: 儲存png檔案】
def savepng(readfile, savefolder):
    maxsize = int(value2)
    try:
        img = Image.open(readfile)  # 載入圖片檔
        # -----------------------------------
        ratio = maxsize / max(img.size)  # 以長寬之中較長的一邊決定比率
        w = int(img.width * ratio)
        h = int(img.height * ratio)
        img = img.resize((w, h), Image.LANCZOS)  # 調整大小
        # -----------------------------------
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)  # 建立轉存資料夾
        filename = Path(readfile).stem + ".png"  # 建立檔案名稱
        img.save(savedir.joinpath(filename), format="PNG")  # 以png格式轉存
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
            print("aaaaa", str(p))
            filelist.append(str(p))  # 新增至列表
        for filename in sorted(filelist):  # 再替每個檔案排序
            print("bbbbb", filename)
            msg += savepng(filename, savefolder)
    return msg


# 【執行函數】
msg = savefiles(infolder, value1)
print(msg)

print("------------------------------------------------------------")  # 60個
print("save_JPGs")
print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個
print("save_PNGs")
print("------------------------------------------------------------")  # 60個

infolder = "testfolder"
value1 = "outputfolder1"
extlist = ["*.jpg", "*.png"]


# 【函數: 儲存png檔案】
def savepng(readfile, savefolder):
    try:
        img = Image.open(readfile)  # 載入圖片檔
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)  # 建立轉存資料夾
        filename = Path(readfile).stem + ".png"  # 建立檔案名稱
        img.save(savedir.joinpath(filename), format="PNG")  # 以png格式轉存
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


# 【執行函數】
msg = savefiles(infolder, value1)
print(msg)



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


