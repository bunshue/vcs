import PyPDF2

pdf_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_pdf/pdf2text1.pdf'

read_pdf = PyPDF2.PdfReader(pdf_filename)
#page = read_pdf.getPage(0)
page = read_pdf.pages[0]
page_content = page.extract_text()

print('pdf轉text')
print(page_content)



