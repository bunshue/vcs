import qrcode as qr

import tkinter as tk
import tkinter.filedialog as fd

from PIL import ImageTk

base = tk.Tk()
base.title('QRcode Generator')
input_area = tk.Frame(base, relief=tk.RAISED, bd=2)
image_area = tk.Frame(base, relief=tk.SUNKEN, bd=2)
encode_text = tk.StringVar()
entry = tk.Entry(input_area, textvariable=encode_text).pack(side=tk.LEFT)
qr_label = tk.Label(image_area)
def generate():
    qr_label.qr_img = qr.make(encode_text.get())
    img_width, img_height = qr_label.qr_img.size
    qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img)
    qr_label.config(image=qr_label.tk_img,width=img_width,height=img_height)
    qr_label.pack()

encode_button = tk.Button(input_area, text='QRcode!',command=generate).pack(side=tk.LEFT)
input_area.pack(pady=5)
image_area.pack(padx=3, pady=1)
def save():
    filename = fd.asksaveasfilename(title='儲存檔案', initialfile='qrcode.png')
    if filename and hasattr(qr_label, 'qr_img'): 
        qr_label.qr_img.save(filename)

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

context_menu = tk.Menu(base, tearoff=0)
context_menu.add_command(label="儲存圖片", command=save)

base.bind('<Button-3>', show_context_menu)

base.mainloop()
