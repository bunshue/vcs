import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile #tk之openFileDialog

window = tk.Tk()

canvas = tk.Canvas(window, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#tk顯示一張圖片
#filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename = 'logo.png'
logo = Image.open(filename)
logo = ImageTk.PhotoImage(logo)
label1 = tk.Label(image=logo)
label1.image = logo
label1.grid(column=1, row=0)

#顯示使用說明
label2 = tk.Label(window, text="Select a PDF file on your computer to extract all its text", font="Raleway")
label2.grid(columnspan=3, column=0, row=1)

def open_file():
    button1_text.set("loading...")
    file = askopenfile(parent=window, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        #page = read_pdf.getPage(0)
        page = read_pdf.pages[0]
        page_content = page.extract_text()

        #tk之textBox
        text_box = tk.Text(window, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

    button1_text.set("Browse")
        

#瀏覽檔案按鈕
button1_text = tk.StringVar()
button1 = tk.Button(window, textvariable=button1_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
button1_text.set("Browse")
button1.grid(column=1, row=2)

canvas = tk.Canvas(window, width=600, height=250)
canvas.grid(columnspan=3)

window.mainloop()


