import os
from win32com import client
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 0
word.DisplayAlerts = 0
cpath=os.path.dirname(__file__)
doc = word.Documents.Open(cpath + "\\media\\test1.docx")
paragraphs = doc.Paragraphs
for p in paragraphs:
    text = p.Range.Text.strip()
    print(text)
doc.Close()
word.Quit()