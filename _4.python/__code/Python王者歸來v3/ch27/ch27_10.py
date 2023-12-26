# ch27_10.py
import PyPDF2

# 打開 PDF 文件
with open('sse.pdf', 'rb') as ssefile, open('secret.pdf', 'rb') as secretfile:
    sse_pdf = PyPDF2.PdfReader(ssefile)
    secret_pdf = PyPDF2.PdfReader(secretfile)

    # 獲取兩個 PDF 的單頁
    sse_page = sse_pdf.pages[0]
    secret_page = secret_pdf.pages[0]

    # 合併頁面
    sse_page.merge_page(secret_page)

    # 建立 PDF 寫入器, 並添加合併後的頁面
    pdfWr = PyPDF2.PdfWriter()
    pdfWr.add_page(sse_page)

    # 寫入新的 PDF 文件
    with open('out27_10.pdf', 'wb') as output_file:
        pdfWr.write(output_file)









