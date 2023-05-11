import os
from win32com import client
from win32com.client import constants
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 0
word.DisplayAlerts = 0
runpath = os.path.dirname(__file__) + "\\replace"  #處理<replace>資料夾
tree = os.walk(runpath)  #取得目錄樹
print("所有 Word 檔案：")
for dirname, subdir, files in tree:
    allfiles = []   
    for file in files:  # 取得所有.docx .doc檔，存入allfiles串列中
        ext = file.split(".")[-1]  #取得附加檔名
        if ext=="docx" or ext=="doc":  #取得所有.docx .doc檔
            allfiles.append(dirname + '\\' + file)  #加入allfiles串列     
         
    if len(allfiles) > 0:  #如果有符合條件的檔案
        for dfile in allfiles:
            print(dfile)
            doc = word.Documents.Open(dfile)  #開啟檔案
            word.Selection.Find.ClearFormatting()
            word.Selection.Find.Replacement.ClearFormatting()
            word.Selection.Find.Execute("方法",False,False,False,False,False,True,constants.wdFindContinue,False,"method",constants.wdReplaceAll)
            doc.Close()
word.Quit()