import docx

filename = 'data/python_docx1.docx'

doc = docx.Document(filename)
for p in doc.paragraphs:
    print(p.text)

'''
pip install python-docx

'''
