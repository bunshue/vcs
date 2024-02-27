import sys

import PyPDF2

pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text1.pdf'

pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text3_one_page.pdf'
pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text4_many_pages.pdf'

print('------------------------------------------------------------')	#60個

read_pdf = PyPDF2.PdfReader(pdf_filename)

pages = len(read_pdf.pages)

print('此文件共有', pages, '頁')

page_content_all = ''
for i in range (pages):
    page = read_pdf.pages[i]
    #print(page)
    page_content = page.extract_text()
    page_content_all += page_content

print('pdf轉text')
print(page_content_all)

print('------------------------------------------------------------')	#60個

#读取PDF文件

pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text4_many_pages.pdf'

from PyPDF2 import PdfFileReader

with open(pdf_filename, 'rb') as f:
    reader = PyPDF2.PdfReader(f, strict=False)
    #print(reader.numPages)
    print('頁數 : ', len(reader.pages))
    
    if reader.is_encrypted:
        reader.decrypt('')
    current_page = reader.pages[2]
    print(current_page)
    print(current_page.extract_text())


print('------------------------------------------------------------')	#60個


import PyPDF2

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/note_Linux_workstation.pdf'

with open(filename, 'rb') as file:     # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)
    print("PDF頁數是 = ", len(pdfRd.pages))

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開 PDF 文件
with open('data/sse.pdf', 'rb') as ssefile, open('data/secret.pdf', 'rb') as secretfile:
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
    with open('tmp_01.pdf', 'wb') as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

source_pdf = 'data/travel.pdf'
output_pdf = 'tmp_02.pdf'

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

fn = 'data/travel.pdf'               # 欲讀取的PDF檔案
with open(fn,'rb') as file:     # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
    page = pdfRd.pages[0]       # 讀第 0 頁
    txt = page.extract_text()   # 取得頁面內容
    print(txt)

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = 'data/member.pdf'               # 欲讀取的PDF檔案
with open(fn,'rb') as file:     # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
    page = pdfRd.pages[0]       # 讀第 0 頁
    txt = page.extract_text()   # 取得頁面內容
    print(txt)

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = 'data/travel.pdf'               # 欲讀取的PDF檔案
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
    #檢查檔案是否加密
    with open(fn,'rb') as file:     
        pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
        if pdfRd.is_encrypted:          # 由這個屬性判斷是否加密
            print(f"{fn:17s} : 檔案有加密")
        else:
            print(f"{fn:17s} : 檔案沒有加密")

encryptYorN('data/travel.pdf')
encryptYorN('data/encrypttravel.pdf')

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = 'data/encrypttravel.pdf'
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
with open('data/travel.pdf', 'rb') as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 將第一頁添加到寫入器
    pdfWr.add_page(pdfRd.pages[0])
    # 寫入新的 PDF 文件
    with open('tmp_03.pdf', 'wb') as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open('data/travel.pdf', 'rb') as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 遍歷所有頁面並將它們添加到寫入器
    for page in pdfRd.pages:
        pdfWr.add_page(page)
    # 寫入新的 PDF 文件
    with open('tmp_04.pdf', 'wb') as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open('data/travel.pdf', 'rb') as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 將第一頁添加到寫入器
    page0 = pdfRd.pages[0]          # 第 0 頁
    pageR = page0.rotate(90)        # 旋轉 90 度
    pdfWr.add_page(pageR)
    # 寫入新的 PDF 文件
    with open('tmp_05.pdf', 'wb') as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open('data/travel.pdf', 'rb') as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 將第一頁添加到寫入器
    page0 = pdfRd.pages[0]          # 第 0 頁
    pageR = page0.rotate(-90)       # 旋轉 -90 度
    pdfWr.add_page(pageR)
    # 寫入新的 PDF 文件
    with open('tmp_06.pdf', 'wb') as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open('data/travel.pdf', 'rb') as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 遍歷所有頁面並將它們添加到寫入器
    for page in pdfRd.pages:
        pdfWr.add_page(page)

    # 設置密碼加密
    pdfWr.encrypt('deepwisdom')

    # 寫入新的 PDF 文件
    with open('tmp_07.pdf', 'wb') as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

"""
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

print("------------------------------------------------------------")  # 60個

import PyPDF2
import os

dirpdf = []   
for x, y, fns in os.walk('.'):
    for fn in fns:
        if fn.endswith('.pdf'):
            dirpdf.append(fn)

for fn in dirpdf:
    pdfObj = open(fn, 'rb')
    pdfRd = PyPDF2.PdfReader(pdfObj)
# New File
    newfn = fn.replace('.pdf', '_encry.pdf')
    pdfWr = PyPDF2.PdfWriter()
    pdfOutFile = open(newfn, 'wb')
    for page in range(len(pdfRd.pages)):
        pdfWr.add_page(pdfRd.pages[page])
        pdfWr.encrypt('python')
        pdfWr.write(pdfOutFile)
    pdfOutFile.close()
"""
print("------------------------------------------------------------")  # 60個








print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



