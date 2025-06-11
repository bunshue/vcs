import tkinter as tk
import winsound


def fnPlay(e):
    i = btns.index(e.widget)
    winsound.Beep(frqs[i], 500)


win = tk.Tk()
win.title("電子琴")
win.geometry("300x200")
notes = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
frqs = [262, 294, 330, 349, 392, 440, 494]
btns = []
for i in range(7):
    btns.append(tk.Button(win, width=4, height=10, text=notes[i]))
    btns[i].pack(side="left", padx=2, pady=5)
    btns[i].bind("<Button-1>", fnPlay)

win.mainloop()
