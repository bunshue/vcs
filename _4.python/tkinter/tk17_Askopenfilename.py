import tkinter as tk

from tkinter import filedialog 

def openFile():
    pdf_filename = filedialog.askopenfilename(title = '開啟PDF檔案', 
                                                  initialdir = 'C:/dddddddddd/____download',
                                                  filetypes=[('PDF files', '*.pdf')])
    print(pdf_filename)
    
    filename_label.configure(text=pdf_filename)    
    outputfile_text.delete("1.0", tk.END)
    
    current_text = 'aaaaaaaa'
    outputfile_text.insert(tk.END, current_text)

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
title = '開啟PDF檔案'
window.title(title)

filename_label = tk.Label(window, text = '未選取檔案')
outputfile_text = tk.Text(window)
openfile_button = tk.Button(window, text = '開啟PDF檔案', command = openFile)

filename_label.pack()
outputfile_text.pack()
openfile_button.pack()

window.mainloop()

