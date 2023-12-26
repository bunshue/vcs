# ch27_4_1.py
import PyPDF2

pdfObj = open('encrypttravel.pdf','rb')
pdfRd = PyPDF2.PdfFileReader(pdfObj)
if pdfRd.decrypt('jiinkwe0'):           # 檢查密碼是否正確
    pageObj = pdfRd.getPage(0)          # 密碼正確則讀取第0頁
    txt = pageObj.extractText()
    print(txt)
else:
    print('解密失敗')












