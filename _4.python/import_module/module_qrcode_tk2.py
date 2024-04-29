"""
QR Code 產生器
"""
import qrcode as qr
import tkinter as tk
import tkinter.filedialog as fd
from PIL import ImageTk

base = tk.Tk()
base.title("QRcode Generator")
input_area = tk.Frame(base, relief=tk.RAISED, bd=2)
image_area = tk.Frame(base, relief=tk.SUNKEN, bd=2)
encode_text = tk.StringVar()
entry = tk.Entry(input_area, textvariable=encode_text).pack(side=tk.LEFT)
qr_label = tk.Label(image_area)


def generate():
    qr_label.qr_img = qr.make(encode_text.get())
    img_width, img_height = qr_label.qr_img.size
    qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img)
    qr_label.config(image=qr_label.tk_img, width=img_width, height=img_height)
    qr_label.pack()


encode_button = tk.Button(input_area, text="QRcode!", command=generate).pack(
    side=tk.LEFT
)
input_area.pack(pady=5)
image_area.pack(padx=3, pady=1)


def save():
    filename = fd.asksaveasfilename(title="儲存檔案", initialfile="qrcode.png")
    if filename and hasattr(qr_label, "qr_img"):
        qr_label.qr_img.save(filename)


def exit():
    base.destroy()


menubar = tk.Menu(base)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="save", command=save)
filemenu.add_separator()
filemenu.add_command(label="exit", command=exit)
base.config(menu=menubar)

base.mainloop()
