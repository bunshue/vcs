import time
import tkinter as tk

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label1.config(text=time_live) 
   label1.after(200, digital_clock)

window = tk.Tk()
window.title("Digital Clock")
window.geometry("420x150")
window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

label1 = tk.Label(window, font=text_font, bg=background, fg=foreground, bd=border_width)
label1.grid(row=0, column=1)

digital_clock()

window.mainloop()
