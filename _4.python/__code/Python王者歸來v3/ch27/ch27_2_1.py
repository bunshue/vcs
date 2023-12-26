# ch27_2_1.py
import PyPDF2

fn = 'member.pdf'               # 欲讀取的PDF檔案
with open(fn,'rb') as file:     # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
    page = pdfRd.pages[0]       # 讀第 0 頁
    txt = page.extract_text()   # 取得頁面內容
    print(txt)
    



