# ch27_3.py
import PyPDF2

fn = 'travel.pdf'               # 欲讀取的PDF檔案
with open(fn,'rb') as file:     # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
    # 遍歷每頁
    for page in pdfRd.pages:
        text = page.extract_text()
        if text:
            print(f"{text}\n")
        else:
            print("這一頁沒有文字")



