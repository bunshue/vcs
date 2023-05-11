import os
from win32com import client
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
doc = word.Documents.Add()
range1 = doc.Range(0,0)  #檔案起始處
range1.InsertAfter("這是測試第一列\n這是測試第二列\n")
range1.InsertAfter("這是測試第三列\n這是測試第四列\n")
range1.InsertBefore("第一次插入到檔案最前方\n")
range1.InsertBefore("再次插入到檔案最前方\n")
cpath = os.path.dirname(__file__)
doc.SaveAs(cpath + "\\media\\test1.docx")
#doc.Close()
#word.Quit()