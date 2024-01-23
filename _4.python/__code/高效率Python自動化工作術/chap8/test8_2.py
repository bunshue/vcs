import openpyxl

infile = "test.xlsx"
value1 = "output.xlsx"
try:
    wb = openpyxl.load_workbook(infile)
    wb.save(value1)   #Excel轉存檔案
except:
    print("程式執行失敗。")
