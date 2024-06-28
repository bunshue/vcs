import tkinter as tk
from tkinter import ttk


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        # create the widgets
        menu_button1 = ttk.Button(self, text="Button 1")
        menu_button2 = ttk.Button(self, text="Button 2")
        menu_button3 = ttk.Button(self, text="Button 3")

        menu_slider1 = ttk.Scale(self, orient="vertical")
        menu_slider2 = ttk.Scale(self, orient="vertical")

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text="check 1")
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text="check 2")

        entry = ttk.Entry(self)

        # create the grid
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # place the widgets
        menu_button1.grid(row=0, column=0, sticky="nswe", columnspan=2)
        menu_button2.grid(row=0, column=2, sticky="nswe")
        menu_button3.grid(row=1, column=0, columnspan=3, sticky="nsew")

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky="nsew", pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky="nsew", pady=20)

        # toggle layout
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
        menu_toggle1.pack(side="left", expand=True)
        menu_toggle2.pack(side="left", expand=True)

        # entry layout
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        # Entry(self, 'Entry 1','Button 1','green')
        # Entry(self, 'Entry 2','Button 2','blue')
        my_list(self, "Entry 1", "Entry 2", "Entry 3", "Button 1", "blue")
        my_list(self, "Entry 1", "Entry 2", "Entry 3", "Button 1", "red")
        my_list(self, "Entry 1", "Entry 2", "Entry 3", "Button 1", "red")
        my_list(self, "Entry 1", "Entry 2", "Entry 3", "Button 1", "red")


class Entry(ttk.Frame):
    def __init__(self, parent, label_text, button_text, label_background):
        super().__init__(parent)

        label = ttk.Label(self, text=label_text, background=label_background)
        button = ttk.Button(self, text=button_text)

        label.pack(expand=True, fill="both")
        button.pack(expand=True, fill="both", pady=10)

        self.pack(side="left", expand=True, fill="both", padx=20, pady=20)


class my_list(ttk.Frame):
    def __init__(
        self,
        parent,
        entry_text1,
        entry_text2,
        entry_text3,
        button_text,
        button_background,
    ):
        super().__init__(parent)
        entry1 = tk.Entry(self, background="red", text=entry_text1)
        entry1.pack(side="left")
        entry2 = tk.Entry(self, background="green", text=entry_text2)
        entry2.pack(side="left")
        entry3 = tk.Entry(self, foreground="blue", text=entry_text3)
        entry3.pack(side="left")
        button = ttk.Button(self, text=button_text)
        button.pack(side="left")
        # self.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)
        self.pack()


window = tk.Tk()
window.geometry("800x600")
window.title("這是主視窗")

menu = Menu(window)
main = Main(window)

window.mainloop()
