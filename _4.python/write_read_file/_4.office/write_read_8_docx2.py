'''
讀取excel檔, 製作word檔
'''

import openpyxl
from docxtpl import DocxTemplate
import datetime

filename = 'data/python_ReadWrite_EXCEL6_student_data2.xlsx'

workbook = openpyxl.load_workbook(filename)
sheet = workbook.active

list_values = list(sheet.values)
print(list_values)

filename = 'data/python_ReadWrite_WORD1_certificate.docx'

# Generate docs
doc = DocxTemplate(filename)

for value_tuple in list_values[1:]:
    doc.render({"name": value_tuple[0],
                "course": value_tuple[1],
                "date": value_tuple[2],
                "instructor":value_tuple[3]})
    
    doc_name = "tmp_certificate" + value_tuple[0] + value_tuple[1] + ".docx"
    print(doc_name)
    doc.save(doc_name)

