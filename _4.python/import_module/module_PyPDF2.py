import PyPDF2

pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text1.pdf'

pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text3_one_page.pdf'
pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text4_many_pages.pdf'

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




