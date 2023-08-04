import openpyxl
from docxtpl import DocxTemplate
import datetime

path = "C:/_git/vcs/_4.python/__code/codefirstio/excel-to-word-docs-main/student_data2.xlsx"

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
    print(doc_name)
    doc.save(doc_name)

