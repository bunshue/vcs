import openpyxl
from openpyxl.styles import Alignment

wb = openpyxl.Workbook()
sh = wb.active
sh.column_dimensions["A"].width = 20 
sh["a1"] = "left,bottom"
sh["a1"].alignment = Alignment(horizontal="left",vertical="bottom")
sh["a2"] = "center,center"
sh["a2"].alignment = Alignment(horizontal="center",vertical="center")
sh["a3"] = "right,top"
sh["a3"].alignment = Alignment(horizontal="right",vertical="top")
sh["a4"] = "distributed,bottom"
sh["a4"].alignment = Alignment(horizontal="distributed",vertical="bottom")

wb.save(r"..\data\format_test.xlsx")