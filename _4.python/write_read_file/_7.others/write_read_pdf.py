"""
pdf 讀寫

pdf2image 需要先下載 poppler, 在 
https://github.com/oschwartz10612/poppler-windows

"""

import re
import sys

pdf_filename = "D:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text1.pdf"

print("------------------------------------------------------------")  # 60個

import PyPDF2

print('印出前10筆合法的密碼')
with open('data/dictionary.txt', 'r') as txt_file_stream:
    file_iter = iter(lambda: txt_file_stream.readline(), '')
    print(type(file_iter))
    cnt = 0
    for word in file_iter:
        word = re.sub(r'\s', '', word)
        print(word)
        cnt += 1
        if cnt > 10:
            break;
        

with open('data/Python_Tricks_encrypted.pdf', 'rb') as pdf_file_stream:
    reader = PyPDF2.PdfReader(pdf_file_stream)
    with open('data/dictionary.txt', 'r') as txt_file_stream:
        file_iter = iter(lambda: txt_file_stream.readline(), '')
        for word in file_iter:
            word = re.sub(r'\s', '', word)
            if reader.decrypt(word):
                print('取得密碼')
                print(word)
                break


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個
print("使用  pdf2image, pdf 轉 jpg")
print("------------------------------------------------------------")  # 60個

from pdf2image import convert_from_path

pages = convert_from_path(
    pdf_filename,
    100,
    poppler_path=r"D:\___backup\Release-24.08.0-0\poppler-24.08.0\Library\bin",
)

for i, page in enumerate(pages):
    pic_filename = "tmp_page" + str(i + 1) + ".png"
    # page.save(pic_filename, "PNG") # JPEG
    print("存檔檔名 :", pic_filename)


print("------------------------------------------------------------")  # 60個
print("使用  PyPDF2")
print("------------------------------------------------------------")  # 60個

import PyPDF2

pdf_filename = "D:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text1.pdf"

pdf_filename = "D:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text3_one_page.pdf"
pdf_filename = (
    "D:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text4_many_pages.pdf"
)

print("------------------------------------------------------------")  # 60個

read_pdf = PyPDF2.PdfReader(pdf_filename)

pages = len(read_pdf.pages)

print("此文件共有", pages, "頁")

page_content_all = ""
for i in range(pages):
    page = read_pdf.pages[i]
    # print(page)
    page_content = page.extract_text()
    page_content_all += page_content

print("pdf轉text")
print(page_content_all)

print("------------------------------------------------------------")  # 60個

# 读取PDF文件

pdf_filename = (
    "D:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text4_many_pages.pdf"
)

from PyPDF2 import PdfFileReader

with open(pdf_filename, "rb") as f:
    reader = PyPDF2.PdfReader(f, strict=False)
    # print(reader.numPages)
    print("頁數 : ", len(reader.pages))

    if reader.is_encrypted:
        reader.decrypt("")
    current_page = reader.pages[2]
    print(current_page)
    print(current_page.extract_text())


print("------------------------------------------------------------")  # 60個


import PyPDF2

filename = "D:/_git/vcs/_1.data/______test_files1/__RW/_pdf/note_Linux_workstation.pdf"

with open(filename, "rb") as file:  # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)
    print("PDF頁數是 = ", len(pdfRd.pages))

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開 PDF 文件
with open("data/sse.pdf", "rb") as ssefile, open("data/secret.pdf", "rb") as secretfile:
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
    with open("tmp_01.pdf", "wb") as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

source_pdf = "data/travel.pdf"
output_pdf = "tmp_02.pdf"

# 建立 PDF 讀寫器和寫入器實例
pdf_reader = PyPDF2.PdfReader(source_pdf)
pdf_writer = PyPDF2.PdfWriter()

# 遍歷 PDF 中的每一頁
for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    text = page.extract_text()
    if "大峽谷" in text:
        # 如果找到 '大峽谷', 則將該頁面添加到輸出 PDF 中
        pdf_writer.add_page(page)

# 將含有 '大峽谷' 的頁面寫入新的 PDF 文件
with open(output_pdf, "wb") as output:
    pdf_writer.write(output)

print(f"含有 '大峽谷' 的頁面已輸出到 {output_pdf}")

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = "data/travel.pdf"  # 欲讀取的PDF檔案
with open(fn, "rb") as file:  # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
    page = pdfRd.pages[0]  # 讀第 0 頁
    txt = page.extract_text()  # 取得頁面內容
    print(txt)

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = "data/member.pdf"  # 欲讀取的PDF檔案
with open(fn, "rb") as file:  # 以二進位方式開啟
    pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
    page = pdfRd.pages[0]  # 讀第 0 頁
    txt = page.extract_text()  # 取得頁面內容
    print(txt)

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = "data/travel.pdf"  # 欲讀取的PDF檔案
with open(fn, "rb") as file:  # 以二進位方式開啟
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
    # 檢查檔案是否加密
    with open(fn, "rb") as file:
        pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
        if pdfRd.is_encrypted:  # 由這個屬性判斷是否加密
            print(f"{fn:17s} : 檔案有加密")
        else:
            print(f"{fn:17s} : 檔案沒有加密")


encryptYorN("data/travel.pdf")
encryptYorN("data/encrypttravel.pdf")

print("------------------------------------------------------------")  # 60個

import PyPDF2

fn = "data/encrypttravel.pdf"
with open(fn, "rb") as file:
    pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
    if pdfRd.decrypt("jiinkwei"):  # 檢查密碼是否正確
        page = pdfRd.pages[0]  # 密碼正確則讀取第0頁
        txt = page.extract_text()
        print(txt)
    else:
        print("解密失敗")

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open("data/travel.pdf", "rb") as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 將第一頁添加到寫入器
    pdfWr.add_page(pdfRd.pages[0])
    # 寫入新的 PDF 文件
    with open("tmp_03.pdf", "wb") as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open("data/travel.pdf", "rb") as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 遍歷所有頁面並將它們添加到寫入器
    for page in pdfRd.pages:
        pdfWr.add_page(page)
    # 寫入新的 PDF 文件
    with open("tmp_04.pdf", "wb") as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open("data/travel.pdf", "rb") as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 將第一頁添加到寫入器
    page0 = pdfRd.pages[0]  # 第 0 頁
    pageR = page0.rotate(90)  # 旋轉 90 度
    pdfWr.add_page(pageR)
    # 寫入新的 PDF 文件
    with open("tmp_05.pdf", "wb") as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open("data/travel.pdf", "rb") as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 將第一頁添加到寫入器
    page0 = pdfRd.pages[0]  # 第 0 頁
    pageR = page0.rotate(-90)  # 旋轉 -90 度
    pdfWr.add_page(pageR)
    # 寫入新的 PDF 文件
    with open("tmp_06.pdf", "wb") as output_file:
        pdfWr.write(output_file)

print("------------------------------------------------------------")  # 60個

import PyPDF2

# 打開原始 PDF 文件
with open("data/travel.pdf", "rb") as file:
    pdfRd = PyPDF2.PdfReader(file)

    # 建立 PDF 寫入器
    pdfWr = PyPDF2.PdfWriter()
    # 遍歷所有頁面並將它們添加到寫入器
    for page in pdfRd.pages:
        pdfWr.add_page(page)

    # 設置密碼加密
    pdfWr.encrypt("deepwisdom")

    # 寫入新的 PDF 文件
    with open("tmp_07.pdf", "wb") as output_file:
        pdfWr.write(output_file)

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

pdf_filename = "D:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text1.pdf"

pdf_filename = "D:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text3_one_page.pdf"
pdf_filename = (
    "D:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text4_many_pages.pdf"
)

print("------------------------------------------------------------")  # 60個

import pdfplumber

pdf = pdfplumber.open(pdf_filename)  # 開啟 pdf
print(pdf.pages)  # [<Page:1>, <Page:2>, <Page:3>]，共有三頁


print("------------------------------------------------------------")  # 60個

import pdfplumber

pdf = pdfplumber.open(pdf_filename)
page = pdf.pages[0]  # 讀取第一頁
text = page.extract_text()  # 取出文字
print(text)


print("------------------------------------------------------------")  # 60個

import pdfplumber

pdf = pdfplumber.open(pdf_filename)
page = pdf.pages[1]  # 讀取第二頁
table = page.extract_table()  # 取出表格
print(table)
pdf.close()


print("------------------------------------------------------------")  # 60個

import pdfplumber

pdf = pdfplumber.open(pdf_filename, password="12345678")  # 輸入密碼
page = pdf.pages[0]
text = page.extract_text()
print(table)
pdf.close()


print("------------------------------------------------------------")  # 60個

import pdfplumber

pdf = pdfplumber.open(pdf_filename)
page = pdf.pages[0]
text = page.extract_text()
print(text)
pdf.close()

f = open("test.txt", "w+")  # 使用 w+ 模式開啟 test.txt
f.write(text)  # 寫入內容
f.close()  # 關閉 test.txt


print("------------------------------------------------------------")  # 60個

import pdfplumber

pdf = pdfplumber.open(pdf_filename)
page = pdf.pages[1]
table = page.extract_table()
print(table)
pdf.close()

import csv

csvfile = open("test-csv.csv", "w+")  # 建立 CSV 檔案
write = csv.writer(csvfile)  # 建立寫入物件
for i in table:
    write.writerow(i)  # 讀取表格每一列寫入 CSV
print("ok")


print("------------------------------------------------------------")  # 60個

from pikepdf import Pdf

pdf = Pdf.open(pdf_filename, password="1234")  # 開啟 pdf
pdf_pwd = Pdf.open("tmptmp-pwd.pdf", password="1234")  # 開啟需要密碼的 pdf
print(pdf)
print(pdf_pwd)


print("------------------------------------------------------------")  # 60個

from pikepdf import Pdf, Permissions, Encryption

pdf = Pdf.open("tmptmp-pwd.pdf", password="1234")  # 開啟密碼為 1234 的 pdf
no_extracting = Permissions(extract=False)
# 儲存為密碼是 qqqq 的 pdf
pdf.save(
    "tmp_new.pdf", encryption=Encryption(user="qqqq", owner="qqqq", allow=no_extracting)
)


print("------------------------------------------------------------")  # 60個


from pikepdf import Pdf

pdf = Pdf.open(pdf_filename)  # 開啟 pdf
pages = pdf.pages  # 將每一頁的內容變成串列
output = Pdf.new()  # 建立新的 pdf 物件
output.pages.append(pages[0])  # 添加頁面內容
output.save("tmp_new2.pdf")  # 儲存為新的 pdf


print("------------------------------------------------------------")  # 60個


from pikepdf import Pdf

pdf = Pdf.open(pdf_filename)
pages = pdf.pages
n = 1
for i in pages:
    output = Pdf.new()
    output.pages.append(i)
    output.save(f"tmp_new3_{n}.pdf")  # 格式化檔案名稱
    n = n + 1  # 編號加 1


print("------------------------------------------------------------")  # 60個


from pikepdf import Pdf

pdf = Pdf.open("test.pdf")
pages = pdf.pages
output = Pdf.new()
output.pages.extend(pages[1:3])  # 改用 extend，放入特定範圍的頁面
output.save("tmp_new4.pdf")


print("------------------------------------------------------------")  # 60個


from pikepdf import Pdf

pdf1 = Pdf.open("tmptmp_1.pdf")  # 讀取第一份 pdf
pdf2 = Pdf.open("tmptmp_2.pdf")  # 讀取第二份 pdf
pdf3 = Pdf.open("tmptmp_3.pdf")  # 讀取第三份 pdf

output = Pdf.new()  # 建立新的 pdf 物件
output.pages.append(pdf1.pages[0])  # 添加第一頁到第一份
output.pages.append(pdf2.pages[0])  # 添加第一頁到第二份
output.pages.append(pdf3.pages[0])  # 添加第一頁到第三份
output.save("tmp_output1.pdf")


print("------------------------------------------------------------")  # 60個


from pikepdf import Pdf

pdf1 = Pdf.open("tmptmp_more_1.pdf")  # 讀取第一份多頁面 pdf
pdf2 = Pdf.open("tmptmp_more_2.pdf")  # 讀取第一份多頁面 pdf
pdf3 = Pdf.open("tmptmp_more_1.pdf")  # 讀取第一份多頁面 pdf

output = Pdf.new()
output.pages.extend(pdf1.pages)  # 添加所有頁面到第一份
output.pages.extend(pdf2.pages)  # 添加所有頁面到第二份
output.pages.extend(pdf3.pages)  # 添加所有頁面到第三份
output.save("tmp_output2.pdf")


print("------------------------------------------------------------")  # 60個

from pikepdf import Pdf

pdf1 = Pdf.open(pdf_filename)  # 開啟第一份 pdf
pdf2 = Pdf.open("new.pdf")  # 開啟第二份 pdf
pdf1.pages.insert(1, pdf2.pages[0])  # 在第一份的第一頁後方，插入第二份的第一頁
pdf1.save("tmp_output3.pdf")


print("------------------------------------------------------------")  # 60個

from pikepdf import Pdf

pdf = Pdf.open("tmptmp.pdf")  # 開啟 pdf
del pdf.pages[1:2]  # 刪除第二頁
pdf.save("tmp_output4.pdf")


print("------------------------------------------------------------")  # 60個

from pikepdf import Pdf

pdf1 = Pdf.open("tmptmp.pdf")  # 開啟第一份 pdf
pdf2 = Pdf.open("new.pdf")  # 開啟第二份 pdf
pdf1.pages[2] = pdf2.pages[0]  # 將第一份的第三頁，換成第一份的第一頁
pdf1.save("tmp_output5.pdf")


print("------------------------------------------------------------")  # 60個

from pikepdf import Pdf

pdf = Pdf.open("output.pdf")
pdf.pages.reverse()  # 反轉 pdf
pdf.save("tmp_output6.pdf")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# pip install pdfminer.six

from pdfminer.high_level import extract_text

infile = "data/test1111.pdf"
try:
    text = extract_text(infile)  # 擷取文字
    print(text)
except:
    print("程式執行失敗")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pathlib import Path
from pdfminer.high_level import extract_text

infile = "data/test1111.pdf"


# 【函數: 從PDF檔案擷取Text】
def extracttext(readfile):
    try:
        text = extract_text(readfile)
        return text
    except:
        return readfile + "：程式執行失敗。"


# 【執行函數】
msg = extracttext(infile)
print(msg)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pathlib import Path
from pdfminer.high_level import extract_text

infolder = "data/test_pdf_folder"
value1 = "這個是"
value2 = "*.pdf"


# 【函數：搜尋文字檔】
def findfile(readfile, findword):
    try:
        msg = ""
        text = extract_text(readfile)  # 擷取文字
        cnt = text.count(findword)  # 搜尋字串
        if cnt > 0:  # 找到的話
            msg = readfile + "：" + "找到" + str(cnt) + "個了。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"


# 【函數: 搜尋資料夾與子資料夾的文字檔】
def findfiles(infolder, findword, ext):
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext):  # 將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))  # 新增至列表
    for filename in sorted(filelist):  # 再替每個檔案排序
        msg += findfile(filename, findword)
    return msg


# 【執行函數】
msg = findfiles(infolder, value1, value2)
print(msg)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pathlib import Path
from pdfminer.high_level import extract_text

infolder = "data/test_pdf_folder"
value1 = ".個是"
value2 = "*.pdf"


# 【函數：利用正規表示法搜尋PDF檔案】
def findfile(readfile, findword):
    try:
        msg = ""
        ptn = re.compile(findword)  # 建立搜尋模式
        text = extract_text(readfile)  # 擷取文字
        cnt = len(re.findall(ptn, text))  # 搜尋字串
        if cnt > 0:  # 找到的話
            msg = readfile + "：" + "找到" + str(cnt) + "個了。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"


# 【函數：以正規表示法搜尋資料夾與子資料夾的所有文字檔】
def findfiles(infolder, findword, ext):
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext):  # 將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))  # 新增至列表
    for filename in sorted(filelist):  # 再替每個檔案排序
        msg += findfile(filename, findword)
    return msg


# 【執行函數】
msg = findfiles(infolder, value1, value2)
print(msg)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
