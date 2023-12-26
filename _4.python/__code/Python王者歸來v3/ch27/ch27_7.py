# ch27_7.py
import PyPDF2

# 打開原始 PDF 文件
with open('travel.pdf', 'rb') as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 遍歷所有頁面並將它們添加到寫入器
    for page in pdfRd.pages:
        pdfWr.add_page(page)
    # 寫入新的 PDF 文件
    with open('out27_7.pdf', 'wb') as output_file:
        pdfWr.write(output_file)
