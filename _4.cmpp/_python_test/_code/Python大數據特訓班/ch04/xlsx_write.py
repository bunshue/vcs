import openpyxl        
workbook=openpyxl.Workbook()   #建立一個工作簿
# 取得第 1 個工作表
sheet = workbook.worksheets[0]

sheet['A1'] = 'Hello'
sheet['B1'] = 'World'
listtitle=["姓名","電話"]
sheet.append(listtitle)  
listdata=["chiou","0937-1234567"]
sheet.append(listdata)  
    
workbook.save('test.xlsx')    