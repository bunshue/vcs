#各種檔案寫讀範例 xlsx 2

import openpyxl
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_excel/python_ReadWrite_EXCEL5_population2.xlsx'

print("讀取 xlsx, 檔案 : " + filename)

workbook = openpyxl.load_workbook(filename)
sheet = workbook.active

list_values = list(sheet.values)
print('所有資料')
print(list_values)
print()

print('標題欄')
cols = list_values[0]
print(cols)

cnt = 0
for value_tuple in list_values[1:]:
    print('第', cnt, '筆資料 :', value_tuple)
    #print(type(value_tuple))
    cnt += 1

