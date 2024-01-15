'''
讀取word檔, 製作word檔

invoice : 發票，發貨單
'''

import datetime
from docxtpl import DocxTemplate

filename1 = 'data/python_ReadWrite_WORD2_invoice_template.docx'

doc = DocxTemplate(filename1)

invoice_list = [[2, "pen", 0.5, 1],
                [1, "paper pack", 5, 5],
                [2, "notebook", 2, 4]]

'''
doc.render({"name":"john", 
            "phone":"555-55555",
            "invoice_list": invoice_list,
            "subtotal":10,
            "salestax":"10%",
            "total":9})
'''
name = 'David Wang'
phone = '0912-345678'
subtotal = sum(item[3] for item in invoice_list) 
salestax = 0.1
total = subtotal*(1-salestax)

doc.render({"name":name,
            "phone":phone,
            "invoice_list": invoice_list,
            "subtotal":subtotal,
            "salestax":str(salestax*100)+"%",
            "total":total})

filename2 = "tmp_new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
doc.save(filename2)

