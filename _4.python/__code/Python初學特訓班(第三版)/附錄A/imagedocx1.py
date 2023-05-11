import os
from win32com import client
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
cpath=os.path.dirname(__file__)
doc = word.Documents.Open(cpath + "\\media\\clipgraph.docx")
paragraphs = doc.Paragraphs
range1 = paragraphs(4).Range
range1.InlineShapes.AddPicture(cpath + "\\media\\cell.jpg", False, True)
#doc.Close()
#word.Quit()