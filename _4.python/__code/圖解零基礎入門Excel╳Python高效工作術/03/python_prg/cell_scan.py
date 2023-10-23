import openpyxl


wb = openpyxl.load_workbook("..\data\sample.xlsx")
for sheet in wb:
    for row in sheet:
        for cell in row:
            print(cell.value)
