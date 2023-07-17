import openpyxl   
# 建立一個工作簿     
workbook=openpyxl.Workbook()   
# 取得第 1 個工作表
sheet = workbook.worksheets[0]
# 以儲存格位置寫入資料
sheet['A1'] = '一年甲班'
# 以串列寫入資料
listtitle=['座號', '姓名', '國文', '英文', '數學']
sheet.append(listtitle)  
listdatas=[[1, '葉大雄', 65, 62, 40],
           [2, '陳靜香', 85, 90, 87],
           [3, '王聰明', 92, 90, 95]]
for listdata in listdatas:
    sheet.append(listdata)
# 儲存檔案   
workbook.save('test.xlsx')