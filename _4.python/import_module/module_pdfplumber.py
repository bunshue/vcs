import sys

print('------------------------------------------------------------')	#60個

pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text1.pdf'

pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text3_one_page.pdf'
pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text4_many_pages.pdf'

print('------------------------------------------------------------')	#60個




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


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




