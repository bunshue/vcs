import openpyxl
import random
from openpyxl.formatting.rule import ColorScaleRule


wb = openpyxl.Workbook()
sh = wb.active
values = random.sample(range(50,150), 10)
for i, value in enumerate(values):
    sh.cell(i + 1, 1 ).value = value

two_color_scale = ColorScaleRule(        
    start_type="min", start_color="FF0000",
    end_type="max", end_color="FFFFFF"
)

sh.conditional_formatting.add("A1:A10", two_color_scale)
 

wb.save(r"..\data\color_scale.xlsx")