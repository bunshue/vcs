# ex27_2.py
import PyPDF2

src = input("請輸入來源檔案名稱 : ")
dst = input("請輸入目的檔案名稱 : ")

pdfObj = open(src,'rb')
pdfRd = PyPDF2.PdfReader(pdfObj)

pdfWr = PyPDF2.PdfWriter()              # 新的PDF物件
for page in range(len(pdfRd.pages)):
    pdfWr.add_page(pdfRd.pages[page])   

pdfOutFile = open(dst, 'wb')            # 開啟二進位檔案供寫入
pdfWr.write(pdfOutFile)                 # 執行寫入
pdfOutFile.close()
















