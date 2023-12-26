# ch27_11.pdf
import PyPDF2

source_pdf = 'travel.pdf'
output_pdf = 'out27_11.pdf'

# 建立 PDF 讀寫器和寫入器實例
pdf_reader = PyPDF2.PdfReader(source_pdf)
pdf_writer = PyPDF2.PdfWriter()

# 遍歷 PDF 中的每一頁
for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    text = page.extract_text()
    if '大峽谷' in text:
        # 如果找到 '大峽谷', 則將該頁面添加到輸出 PDF 中
        pdf_writer.add_page(page)

# 將含有 '大峽谷' 的頁面寫入新的 PDF 文件
with open(output_pdf, 'wb') as output:
    pdf_writer.write(output)

print(f"含有 '大峽谷' 的頁面已輸出到 {output_pdf}")


