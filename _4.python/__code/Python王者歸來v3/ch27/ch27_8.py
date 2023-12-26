# ch27_8.py
import PyPDF2

# 打開原始 PDF 文件
with open('travel.pdf', 'rb') as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 將第一頁添加到寫入器
    page0 = pdfRd.pages[0]          # 第 0 頁
    pageR = page0.rotate(90)        # 旋轉 90 度
    pdfWr.add_page(pageR)
    # 寫入新的 PDF 文件
    with open('out27_8.pdf', 'wb') as output_file:
        pdfWr.write(output_file)


