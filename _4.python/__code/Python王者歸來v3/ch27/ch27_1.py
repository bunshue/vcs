# ch27_1.py
import PyPDF2

fn = 'travel.pdf'               # 欲讀取的PDF檔案
with open(fn,'rb') as file:     # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)
    print("PDF頁數是 = ", len(pdfRd.pages))



