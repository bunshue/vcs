# ch27_2_1.py
import PyPDF2

fn = 'travel.pdf'                       # 設定欲讀取的PDF檔案
pdfObj = open(fn,'rb')                  # 以二進位方式開啟
pdfRd = PyPDF2.PdfFileReader(pdfObj)    # 讀取PDF檔案
pageObj = pdfRd.getPage(1)              # 將第1頁內容讀入pageObj
txt = pageObj.extractText()             # 擷取頁面內容
print(txt)






