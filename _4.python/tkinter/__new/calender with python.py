import calendar
import tkinter as tk

def showCalender():
    gui = tk.Tk()
    gui.config(background='grey')
    gui.title("Calender for the year")
    gui.geometry("550x600")
    
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = tk.Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()

window = tk.Tk()
window.config(background='grey')
window.title("Calender")
window.geometry("250x140")

cal = tk.Label(window, text="Calender",bg='grey',font=("times", 28, "bold"))
year = tk.Label(window, text="Enter year", bg='dark grey')
year_field=tk.Entry(window)
button = tk.Button(window, text='Show Calender', fg='Black',bg='Blue',command=showCalender)
Exit = tk.Button(window, text='Exit', fg='Black', bg='Blue', command=exit)

cal.grid(row=1, column=1)
year.grid(row=2, column=1)
year_field.grid(row=3, column=1)
button.grid(row=4, column=1)
Exit.grid(row=6, column=1)

window.mainloop()

