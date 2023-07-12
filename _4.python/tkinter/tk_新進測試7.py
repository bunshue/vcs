import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

window = tk.Tk()

canvas = tk.Canvas(window, bg = 'yellow', width = 600, height = 300)
canvas.grid(columnspan = 3, rowspan = 3)

#tk顯示一張圖片
#filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename = 'logo.png'
logo = Image.open(filename)
logo = ImageTk.PhotoImage(logo)
label1 = tk.Label(image = logo)
label1.image = logo
label1.grid(column = 1, row = 0)


canvas = tk.Canvas(window, bg = 'pink', width = 600, height = 250)
canvas.grid(columnspan = 3)



pdf_filename = 'C:/_git/vcs/_4.python/_example/tk_pdf2text/test2.pdf'

read_pdf = PyPDF2.PdfReader(pdf_filename)
#page = read_pdf.getPage(0)
page = read_pdf.pages[0]
page_content = page.extract_text()

print(page_content)

window.mainloop()




