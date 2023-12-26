# ch27_4.py
import PyPDF2

pdfObj = open('encrypttravel.pdf','rb')
pdfRd = PyPDF2.PdfFileReader(pdfObj)
if pdfRd.decrypt('jiinkwei'):           # 檢查密碼是否正確
    pageObj = pdfRd.getPage(0)          # 密碼正確則讀取第0頁
    txt = pageObj.extractText()
    print(txt)
else:
    print('解密失敗')












