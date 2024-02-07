import tkinter as tk
    
window = tk.Tk()
window.title("用Label顯示文字及圖片")         # 視窗標題

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dog.gif'

pic = tk.PhotoImage(file=filename)
label1 = tk.Label(window,image=pic).pack(side="right")

description ="""
故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。
"""
label2 = tk.Label(window,text=description,bg="lightyellow",
             justify=tk.LEFT,padx=10).pack(side="left")

window.mainloop()
