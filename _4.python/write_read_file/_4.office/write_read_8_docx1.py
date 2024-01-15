import docx

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_word/python_docx1.docx'

doc = docx.Document(filename)
for p in doc.paragraphs:
    print(p.text)

'''
pip install python-docx

'''
