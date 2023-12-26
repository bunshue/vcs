# ch27_7.py
import PyPDF2

pdfObj = open('travel.pdf','rb')
pdfRd = PyPDF2.PdfFileReader(pdfObj)

pdfWr = PyPDF2.PdfFileWriter()          # 新的PDF物件
pageR = pdfRd.getPage(0)                # 原始第0頁
pageR = pageR.rotateClockwise(90)       # 第0頁炫轉90度
pdfWr.addPage(pageR)                    # 將炫轉後的第0頁放入新的PDF物件

pdfOutFile = open('out27_7.pdf', 'wb')  # 開啟二進位檔案供寫入
pdfWr.write(pdfOutFile)                 # 執行寫入
pdfOutFile.close()















