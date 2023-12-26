# ch27_9.py
import PyPDF2

pdfSSE = open('sse.pdf','rb')               # 開啟一般pdf檔案
pdfRdSSE = PyPDF2.PdfFileReader(pdfSSE)
ssePage = pdfRdSSE.getPage(0)

pdfSecret = open('secret.pdf', 'rb')        # 開啟浮水印pdf檔案
pdfRdSecret = PyPDF2.PdfFileReader(pdfSecret)
secretPage = pdfRdSecret.getPage(0)

ssePage.mergePage(secretPage)               # 執行重疊合併

pdfWr = PyPDF2.PdfFileWriter()              # 新的PDF物件
pdfWr.addPage(ssePage)                      # 將重疊頁放入新的PDF物件

mergePdf = open('out27_9.pdf', 'wb')        # 開啟二進位檔案供寫入
pdfWr.write(mergePdf)                       # 執行寫入
mergePdf.close()








