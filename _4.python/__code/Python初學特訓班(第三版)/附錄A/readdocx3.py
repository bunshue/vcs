import os
from win32com import client
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 0
word.DisplayAlerts = 0
cpath=os.path.dirname(__file__)
doc = word.Documents.Open(cpath + "\\media\\test1.docx")
paragraphs = doc.Paragraphs
print("第一段：" + paragraphs(1).Range.Text.strip())
print("第三段：" + paragraphs(3).Range.Text.strip())
doc.Close()
word.Quit()