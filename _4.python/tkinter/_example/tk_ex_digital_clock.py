import time
import tkinter as tk

text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

print("------------------------------------------------------------")  # 60個

def digital_clock(): 
   show_time = time.strftime("%H:%M:%S")
   label1.config(text=show_time) 
   label1.after(200, digital_clock)

window = tk.Tk()
window.title("Digital Clock")
window.geometry("420x150")
window.resizable(1,1)

label1 = tk.Label(window, font=text_font, bg=background, fg=foreground, bd=border_width)
label1.grid(row=0, column=1)

digital_clock()

window.mainloop()

print("------------------------------------------------------------")  # 60個

def digital_clock():
   global program_start_time
   show_time = time.time() - program_start_time
   label1.config(text=show_time) 
   label1.after(37, digital_clock)

window = tk.Tk()
window.title("Counter")
window.geometry("1000x150")
window.resizable(1,1)

label1 = tk.Label(window, font=text_font, bg=background, fg=foreground, bd=border_width)
label1.grid(row=0, column=1)

program_start_time = time.time()

digital_clock()

window.mainloop()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



