import calendar
import tkinter as tk

window = tk.Tk()
window.config(background="grey")
window.title("Calender for the year")
window.geometry("550x600")

year = 2024
content = calendar.calendar(year)
calYear = tk.Label(window, text=content, font="Consolas 10 bold")
calYear.grid(row=5, column=1, padx=20)

window.mainloop()
