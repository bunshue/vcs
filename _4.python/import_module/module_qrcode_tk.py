"""
QR Code 產生器
"""
import qrcode as qr
import tkinter as tk
import tkinter.filedialog as fd
from PIL import ImageTk

window = tk.Tk()
window.title("QRcode Generator")

input_area = tk.Frame(window, relief=tk.RAISED, bd=2)
image_area = tk.Frame(window, relief=tk.SUNKEN, bd=2)

# 此變數用來儲存將轉換成qrcode的字串
encode_text = tk.StringVar()
entry = tk.Entry(input_area, textvariable=encode_text).pack(side=tk.LEFT)

# 用來顯示qr_code的label
qr_label = tk.Label(image_area)


def generate():
    qr_label.qr_img = qr.make(encode_text.get())
    img_width, img_height = qr_label.qr_img.size
    qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img)
    qr_label.config(image=qr_label.tk_img, width=img_width, height=img_height)
    qr_label.pack()


# 開始產生qrcode的觸發按鈕
encode_button = tk.Button(input_area, text="QRcode!", command=generate).pack(
    side=tk.LEFT
)

# 描繪框線
input_area.pack(pady=5)
image_area.pack(padx=3, pady=1)


# 儲存選單
def save():
    filename = fd.asksaveasfilename(title="儲存檔案", initialfile="qrcode.png")
    if filename and hasattr(qr_label, "qr_img"):
        qr_label.qr_img.save(filename)


# 結束選單
def exit():
    window.destroy()


# 建立選單畫面
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="save", command=save)
filemenu.add_separator()
filemenu.add_command(label="exit", command=exit)
window.config(menu=menubar)

window.mainloop()
