# ch27_8.py
import PyPDF2

pdfObj = open('travel.pdf','rb')
pdfRd = PyPDF2.PdfFileReader(pdfObj)

pdfWr = PyPDF2.PdfFileWriter()              # 新的PDF物件
for pageNum in range(pdfRd.numPages):
    pdfWr.addPage(pdfRd.getPage(pageNum))   # 一次將一頁放入新的PDF物件

pdfWr.encrypt('deepstone')                  # 執行加密
encryptPdf = open('output.pdf', 'wb')       # 開啟二進位檔案供寫入
pdfWr.write(encryptPdf)                     # 執行寫入
encryptPdf.close()





