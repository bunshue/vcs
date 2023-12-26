# ch27_5.py
import PyPDF2

fn = 'encrypttravel.pdf'
with open(fn,'rb') as file:     
    pdfRd = PyPDF2.PdfReader(file)      # 讀 pdf
    if pdfRd.decrypt('jiinkwei'):       # 檢查密碼是否正確
        page = pdfRd.pages[0]           # 密碼正確則讀取第0頁
        txt = page.extract_text()
        print(txt)
    else:
        print('解密失敗')












