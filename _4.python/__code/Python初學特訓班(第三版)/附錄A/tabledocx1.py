import os
from win32com import client
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
cpath=os.path.dirname(__file__)
doc = word.Documents.Open(cpath + "\\media\\clipgraph.docx")
data = [ ["型號", "尺寸", "顏色", "價格"], ["A8", "5.0 吋", "白色", "8000"], \
         ["A10", "5.5 吋", "金黃", "22000"] ]
paragraphs = doc.Paragraphs
range1 = paragraphs(4).Range
table = doc.Tables.Add(range1, 3, 4)
for i in range(1,table.Rows.Count+1):
    for j in range(1,table.Columns.Count+1):
        table.Cell(i,j).Range.Text = data[i-1][j-1]
table.Cell(2,3).Range.Font.Color = 0x0000FF
#doc.Close()
#word.Quit()