import docx
doc = docx.Document("簡介.docx")
for p in doc.paragraphs:
    print(p.text)
