import pathlib  
import openpyxl 
from win32com import client

path = pathlib.Path("..\data\sales")    #指定相對路徑

xlApp = client.Dispatch("Excel.Application")
for pass_obj in path.iterdir():
    print(pass_obj)
    if pass_obj.match("*.xlsx"):
        print("match :", pass_obj)
        book = xlApp.workbooks.open(str(pass_obj.resolve()))
        for sheet in book.Worksheets:
            print('------------------------------')
            slip_no = str(int(sheet.Range("G2").value))
            file_name = slip_no + ".pdf"
            pdf_path = path / "pdf" / file_name
            
            sheet.ExportAsFixedFormat(0, str(pdf_path.resolve()))
            print(pdf_path)
            print(str(pdf_path.resolve()))
            print()

        book.Close()
xlApp.Quit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print('------------------------------------------------------------')	#60個



