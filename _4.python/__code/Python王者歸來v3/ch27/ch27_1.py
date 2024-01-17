import PyPDF2

fn = 'travel.pdf'               # 欲讀取的PDF檔案
with open(fn,'rb') as file:     # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)
    print("PDF頁數是 = ", len(pdfRd.pages))

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = 'travel.pdf'               # 欲讀取的PDF檔案
with open(fn,'rb') as file:     # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
    page = pdfRd.pages[0]       # 讀第 0 頁
    txt = page.extract_text()   # 取得頁面內容
    print(txt)

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = 'member.pdf'               # 欲讀取的PDF檔案
with open(fn,'rb') as file:     # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
    page = pdfRd.pages[0]       # 讀第 0 頁
    txt = page.extract_text()   # 取得頁面內容
    print(txt)

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = 'travel.pdf'               # 欲讀取的PDF檔案
with open(fn,'rb') as file:     # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
    # 遍歷每頁
    for page in pdfRd.pages:
        text = page.extract_text()
        if text:
            print(f"{text}\n")
        else:
            print("這一頁沒有文字")

print("------------------------------------------------------------")  # 60個

import PyPDF2

def encryptYorN(fn):
    '''檢查檔案是否加密'''
    with open(fn,'rb') as file:     
        pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
        if pdfRd.is_encrypted:          # 由這個屬性判斷是否加密
            print(f"{fn:17s} : 檔案有加密")
        else:
            print(f"{fn:17s} : 檔案沒有加密")

encryptYorN('travel.pdf')
encryptYorN('encrypttravel.pdf')

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = 'encrypttravel.pdf'
with open(fn,'rb') as file:     
    pdfRd = PyPDF2.PdfReader(file)      # 讀 pdf
    if pdfRd.decrypt('jiinkwei'):       # 檢查密碼是否正確
        page = pdfRd.pages[0]           # 密碼正確則讀取第0頁
        txt = page.extract_text()
        print(txt)
    else:
        print('解密失敗')

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open('travel.pdf', 'rb') as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 將第一頁添加到寫入器
    page0 = pdfRd.pages[0]          # 第 0 頁
    pageR = page0.rotate(-90)       # 旋轉 -90 度
    pdfWr.add_page(pageR)
    # 寫入新的 PDF 文件
    with open('out27_8_1.pdf', 'wb') as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open('travel.pdf', 'rb') as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 遍歷所有頁面並將它們添加到寫入器
    for page in pdfRd.pages:
        pdfWr.add_page(page)

    # 設置密碼加密
    pdfWr.encrypt('deepwisdom')

    # 寫入新的 PDF 文件
    with open('out27_9.pdf', 'wb') as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個
