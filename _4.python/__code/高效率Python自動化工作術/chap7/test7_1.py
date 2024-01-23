from docx import Document

infile = "test.docx"
try:
    doc = Document(infile)
    for pa in doc.paragraphs:   #所有段落
        print("paragraph----")
        print(pa.text)
    for tbl in doc.tables:      #所有表
        print("table----")
        for row in tbl.rows:
            print("row----")
            for cell in row.cells:
                print(cell.text)
except:
    print("程式執行失敗。")
