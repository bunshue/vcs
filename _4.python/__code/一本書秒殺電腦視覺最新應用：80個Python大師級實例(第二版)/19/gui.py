from tkinter import ttk
import tkinter
from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
from test_tf import ocr_handle

root = Tk()
root.title("GUI")

path = StringVar()
file_entry = Entry(root, state='readonly', text=path)

global now_img

def choosepic():
    path_ = askopenfilename()
    if len(path_) < 1:
        return
    path.set(path_)
    global now_img
    now_img = file_entry.get()
    img_open = Image.open(file_entry.get())
    img_open = img_open.resize((360, 270))
    img = ImageTk.PhotoImage(img_open)
    image_label.config(image=img)
    image_label.image = img

def btn():
    global now_img
    res = ocr_handle(now_img)
    tkinter.messagebox.showinfo('提示', '识别结果是：%s'%res)
    exit(0)


mainframe = ttk.Frame(root, padding="5 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="选择图片", command=choosepic).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="CNN识别", command=btn).grid(column=4, row=4, sticky=W)

image_label = ttk.Label(root,compound=CENTER)
image_label.grid(column=0,row=5, sticky=W)
bg = "./brid.png"
pil_image = Image.open(bg)
pil_image = pil_image.resize((360, 270))
img = ImageTk.PhotoImage(pil_image)
image_label.configure(image=img)

root.mainloop()
