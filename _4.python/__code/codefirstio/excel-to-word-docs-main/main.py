import openpyxl
from docxtpl import DocxTemplate
import datetime

# Load data from Excel
path = "D:\codefirst.io\Excel Sheet to Word Documents\student_data.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

list_values = list(sheet.values)
print(list_values)

# Generate docs
doc = DocxTemplate("certificate.docx")

for value_tuple in list_values[1:]:
    doc.render({"name": value_tuple[0],
                "course": value_tuple[1],
                "date": value_tuple[2],
                "instructor":value_tuple[3]})
    
    doc_name = "certificate" + value_tuple[0] + value_tuple[1] + ".docx"
    doc.save(doc_name)
