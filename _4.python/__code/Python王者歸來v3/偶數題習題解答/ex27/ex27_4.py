# ex27_4.py
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

    









