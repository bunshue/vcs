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
    pdfRd = PyPDF2.PdfFileReader(pdfObj)
# New File
    newfn = fn.replace('.pdf', '_encry.pdf')
    pdfWr = PyPDF2.PdfFileWriter()
    pdfOutFile = open(newfn, 'wb')
    for page in range(pdfRd.numPages):
        pdfWr.addPage(pdfRd.getPage(page))
        pdfWr.encrypt('python')
        pdfWr.write(pdfOutFile)
    pdfOutFile.close()

    









