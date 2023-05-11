import os
from win32com import client as client
from win32com.client import constants
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
cpath=os.path.dirname(__file__)
doc = word.Documents.Open(cpath + "\\media\\clipgraph.docx")
word.Selection.Find.ClearFormatting()
word.Selection.Find.Replacement.ClearFormatting()
word.Selection.Find.Execute("方法",False,False,False,False,False,True,constants.wdFindContinue,False,"method",constants.wdReplaceAll)
#doc.Close()
#word.Quit()