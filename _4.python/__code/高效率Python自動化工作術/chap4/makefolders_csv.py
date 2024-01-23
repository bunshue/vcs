from pathlib import Path
import csv

infile = "namelist.csv"
value1 = "outputfolder"

#【函數：根據CSV的內容建立資料夾】
def makefolders(readfile, savefolder):
    try:
        msg = ""
        Path(savefolder).mkdir(exist_ok=True)   #建立轉存檔案的資料夾
        f = Path(infile).open(encoding="UTF-8") #開啟檔案
        csvdata = csv.reader(f)                 #載入CSV的資料
        for row in csvdata:                     #取得每一列資料
            for foldername in row:              #逐次取得元素
                newfolder = Path(savefolder).joinpath(foldername)
                newfolder.mkdir(exist_ok=True)  #建立資料夾
                msg += "在" + savefolder + "建立了" + foldername + "了。\n"
        return msg
    except:
        return readfile + "：無法載入檔案。"
    
#【執行函數】
msg = makefolders(infile, value1)
print(msg)  #顯示結果