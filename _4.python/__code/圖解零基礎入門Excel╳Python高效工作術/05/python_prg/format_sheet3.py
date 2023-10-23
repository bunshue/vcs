import openpyxl
from openpyxl.styles import Border, Side

wb = openpyxl.load_workbook(r"..\data\border.xlsx")
sh = wb.active

side1 = Side(style="hair", color="00FF00")
side2 = Side(style="dashDotDot", color="0000FF")
side3 = Side(style="double", color="FF0000")
for rows in sh["B2":"C4"]:
    for cell in rows:
        cell.border = Border(left=side1, right=side1, top=side1, bottom=side1 )
for rows in sh["E2":"F4"]:
    for cell in rows:
        cell.border = Border(left=side2, right=side2, top=side2, bottom=side2)
for rows in sh["H2":"I4"]:
    for cell in rows:
        cell.border = Border(left=side3, right=side3, top=side3, bottom=side3 )


wb.save(r"..\data\border_ed.xlsx")