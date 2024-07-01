import tkinter as tk
import cv2

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"


def load_picture_color():
    img = cv2.imread(filename)
    cv2.imshow("show", img)  # 在show視窗顯示img圖像
    cv2.waitKey(0)


def load_picture_gray():
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("show", img)  # 在show視窗顯示img圖像
    cv2.waitKey(0)

def save_picture():
    print('save_picture()')
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(fn.get() + spinbox1.get(), img)

window = tk.Tk()
window.title("圖像")
window.geometry("400x200")

button1 = tk.Button(window, text="原圖載入", command=load_picture_color)

button1.pack(padx=5, pady=5)

button2 = tk.Button(window, text="灰階載入", command=load_picture_gray)
button2.pack(padx=5, pady=5)

tk.Label(window, text="檔名：").pack(side="left")

fn = tk.StringVar()
fn.set("test")
entry1 = tk.Entry(window, textvariable=fn, width=8)
entry1.pack(side="left")

tk.Label(window, text="副檔名：").pack(side="left")

spinbox1 = tk.Spinbox(window, values=[".bmp", ".jpg", ".png", ".tif"], width=5)
spinbox1.pack(side="left")

button3 = tk.Button(window, text="存成灰階", command=save_picture)
button3.pack(side="left")

window.mainloop()

cv2.destroyAllWindows()  # 關閉所有視窗
