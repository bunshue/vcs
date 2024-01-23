from docx import Document

infile = "test.docx"
value1 = "tmp_output.docx"
try:
    doc = Document(infile)
    doc.save(value1)
except:
    print("程式執行失敗。")
    
