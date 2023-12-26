# ch27_6.py
import PyPDF2

# 打開原始 PDF 文件
with open('travel.pdf', 'rb') as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 將第一頁添加到寫入器
    pdfWr.add_page(pdfRd.pages[0])
    # 寫入新的 PDF 文件
    with open('out27_6.pdf', 'wb') as output_file:
        pdfWr.write(output_file)


