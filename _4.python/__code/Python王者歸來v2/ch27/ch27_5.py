# ch27_5.py
import PyPDF2

pdfObj = open('travel.pdf','rb')
pdfRd = PyPDF2.PdfFileReader(pdfObj)

pdfWr = PyPDF2.PdfFileWriter()          # 新的PDF物件
pdfWr.addPage(pdfRd.getPage(0))         # 將第0頁放入新的PDF物件

pdfOutFile = open('out27_5.pdf', 'wb')  # 開啟二進位檔案供寫入
pdfWr.write(pdfOutFile)                 # 執行寫入
pdfOutFile.close()
















