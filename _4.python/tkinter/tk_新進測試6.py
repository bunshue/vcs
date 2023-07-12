import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)


from tkinter.filedialog import askopenfile #tk之openFileDialog

def open_file():
    button1_text.set("loading...")
    file = askopenfile(parent = window, mode = 'rb', title = "Choose a file", filetypes = [("Any file", "*.*")])
    if file:
        print('你選擇了檔案 : ', file)
        print(type(file))

    button1_text.set("Browse")

#瀏覽檔案按鈕
button1_text = tk.StringVar()
button1 = tk.Button(window, textvariable = button1_text, command = lambda:open_file(), font = "Raleway", bg = "#20bebe", fg = "white", height = 2, width = 15)
button1_text.set("Browse")
button1.grid(column = 1, row = 2)


page_content = 'this is a lion-mouse'
#tk之textBox
text_box = tk.Text(window, height = 10, width = 50, padx = 15, pady = 15)
text_box.insert(1.0, page_content)
text_box.tag_configure("center", justify = "center")
text_box.tag_add("center", 1.0, "end")
text_box.grid(column = 1, row = 3)

#顯示使用說明
label2 = tk.Label(window, text = "Select a PDF file on your computer to extract all its text", font = "Raleway")
label2.grid(columnspan = 3, column = 0, row = 1)



window.mainloop()
