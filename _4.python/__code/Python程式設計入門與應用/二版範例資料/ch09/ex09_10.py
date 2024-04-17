# Filename: ex09_10.py
import tkinter as tk
import tkinter.font as tkfont
def radbut_click():
    selected_item = area.get()
    lab_result.config(text=AREA_OPTIONS[selected_item][0])
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
AREA_OPTIONS=(('屏東縣',0),('高雄市',1),('台南市',2),('台東縣',3))
area = tk.IntVar()
area.set(0)
for item, value in AREA_OPTIONS:
    radbut = tk.Radiobutton(win, text=item, variable=area, value=value, command=radbut_click, font=default_font)
    radbut.pack()
lab_result = tk.Label(win, font=default_font, fg='black')
lab_result.pack(padx=10, pady=(5,10))       
win.mainloop()