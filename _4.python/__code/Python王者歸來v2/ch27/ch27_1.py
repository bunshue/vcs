# ch27_1.py
import PyPDF2

fn = 'travel.pdf'           # 設定欲讀取的PDF檔案
pdfObj = open(fn,'rb')      # 以二進位方式開啟
pdfRd = PyPDF2.PdfFileReader(pdfObj)
print("PDF頁數是 = ", pdfRd.numPages)



