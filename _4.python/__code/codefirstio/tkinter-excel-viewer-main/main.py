import tkinter
from tkinter import ttk
import openpyxl

def load_data():
    path = "D:\codefirst.io\Tkinter Excel Viewer\list-countries-world.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    list_values = list(sheet.values)
    cols = list_values[0]
    tree = ttk.Treeview(window, column= cols, show="headings")
    for col_name in cols:
        tree.heading(col_name, text = col_name)
    tree.pack(expand=True, fill='y')
    
    for value_tuple in list_values[1:]:
        tree.insert('',tkinter.END, values=value_tuple)


window = tkinter.Tk()
window.title("Excel Viewer")

load_data()

window.mainloop()
