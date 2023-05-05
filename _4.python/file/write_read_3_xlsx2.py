#各種檔案寫讀範例 xlsx 2

print("寫讀 xlsx")

print("建立 xlsx")

filename = 'C:/_git/vcs/_1.data/______test_files2/test2.xlsx'

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
    
workbook.save(filename)    




import openpyxl
 
#  讀取檔案
workbook = openpyxl.load_workbook(filename)
# 取得第 1 個工作表
sheet = workbook.worksheets[0]

# 取得指定儲存格
print(sheet['A1'], sheet['A1'].value)

# 取得總行、列數
print(sheet.max_row, sheet.max_column)

# 顯示 cell資料
for i in range(1, sheet.max_row+1):
    for j in range(1, sheet.max_column+1):
        print(sheet.cell(row=i, column=j).value,end="   ")
    print()

sheet['A3'] = 'David'

filename2 = 'C:/_git/vcs/_1.data/______test_files2/test2b.xlsx'

workbook.save(filename2)









