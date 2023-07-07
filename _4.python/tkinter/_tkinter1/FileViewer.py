import tkinter as tk

window = tk.Tk()
window.title('')

frame1 = tk.Frame(window) # Hold four labels for displaying cards
frame1.pack()

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
text = tk.Text(frame1, wrap = tk.WORD, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

frame2 = tk.Frame(window) # Hold four labels for displaying cards
frame2.pack()

tk.Label(frame2, text = "Enter a filename: ").pack(side = tk.LEFT)
filename = tk.StringVar()
tk.Entry(frame2, width = 40, textvariable = filename).pack(side = tk.LEFT)
tk.Button(frame2, text = "Validate", command = '').pack()

window.mainloop()
