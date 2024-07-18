import sys

import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

'''
print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

print('有用到 pickle')
print('grid 範例')

import pickle
import os.path
from tkinter import *  # Import tkinter
import tkinter.messagebox


class Address:
    def __init__(self, name, street, city, state, zip):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip


class AddressBook:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("AddressBook")  # Set title

        self.nameVar = StringVar()
        self.streetVar = StringVar()
        self.cityVar = StringVar()
        self.stateVar = StringVar()
        self.zipVar = StringVar()

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="Name").grid(row=1, column=1, sticky=W)
        Entry(frame1, textvariable=self.nameVar, width=40).grid(row=1, column=2)

        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text="Street").grid(row=1, column=1, sticky=W)
        Entry(frame2, textvariable=self.streetVar, width=40).grid(row=1, column=2)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text="City", width=5).grid(row=1, column=1, sticky=W)
        Entry(frame3, textvariable=self.cityVar).grid(row=1, column=2)
        Label(frame3, text="State").grid(row=1, column=3, sticky=W)
        Entry(frame3, textvariable=self.stateVar, width=5).grid(row=1, column=4)
        Label(frame3, text="ZIP").grid(row=1, column=5, sticky=W)
        Entry(frame3, textvariable=self.zipVar, width=5).grid(row=1, column=6)

        frame4 = Frame(window)
        frame4.pack()
        Button(frame4, text="Add", command=self.processAdd).grid(row=1, column=1)
        btFirst = Button(frame4, text="First", command=self.processFirst).grid(
            row=1, column=2
        )
        btNext = Button(frame4, text="Next", command=self.processNext).grid(
            row=1, column=3
        )
        btPrevious = Button(frame4, text="Previous", command=self.processPrevious).grid(
            row=1, column=4
        )
        btLast = Button(frame4, text="Last", command=self.processLast).grid(
            row=1, column=5
        )

        self.addressList = self.loadAddress()
        self.current = 0

        length = len(self.addressList)

        if length > 0:
            self.setAddress()
            print("aaaaaaaaaaaaa, len =", length)
            for i in range(length):
                print(i)
                print(self.addressList[i].name)
                print(self.addressList[i].street)
                print(self.addressList[i].city)
                print(self.addressList[i].state)
                print(self.addressList[i].zip)

        window.mainloop()  # Create an event loop

    def saveAddress(self):
        outfile = open("address.dat", "wb")
        pickle.dump(self.addressList, outfile)
        tkinter.messagebox.showinfo("Address saved", "A new address is saved")
        outfile.close()

    def loadAddress(self):
        if not os.path.isfile("address.dat"):
            return []  # Return an empty list

        print("使用 pickle 讀取檔案")

        try:
            infile = open("address.dat", "rb")
            addressList = pickle.load(infile)
        except EOFError:
            addressList = []

        infile.close()
        print(addressList)
        return addressList

    def processAdd(self):
        address = Address(
            self.nameVar.get(),
            self.streetVar.get(),
            self.cityVar.get(),
            self.stateVar.get(),
            self.zipVar.get(),
        )
        self.addressList.append(address)
        self.saveAddress()

    def processFirst(self):
        self.current = 0
        self.setAddress()

    def processNext(self):
        if self.current < len(self.addressList) - 1:
            self.current += 1
            self.setAddress()

    def processPrevious(self):
        pass  # Left as exercise

    def processLast(self):
        pass  # Left as exercise

    def setAddress(self):
        self.nameVar.set(self.addressList[self.current].name)
        self.streetVar.set(self.addressList[self.current].street)
        self.cityVar.set(self.addressList[self.current].city)
        self.stateVar.set(self.addressList[self.current].state)
        self.zipVar.set(self.addressList[self.current].zip)


AddressBook()  # Create GUI


print("------------------------------------------------------------")  # 60個

# GridManagerDemo

from tkinter import *  # Import tkinter


class GridManagerDemo:
    window = Tk()  # Create a window
    window.title("Grid Manager Demo")  # Set title

    message = Message(
        window, text="This Message widget occupies three rows and two columns"
    )
    message.grid(row=1, column=1, rowspan=3, columnspan=2)
    Label(window, text="First Name:").grid(row=1, column=3)
    Entry(window).grid(row=1, column=4, padx=5, pady=5)
    Label(window, text="Last Name:").grid(row=2, column=3)
    Entry(window).grid(row=2, column=4)
    Button(window, text="Get Name").grid(row=3, padx=5, pady=5, column=4, sticky=E)

    window.mainloop()  # Create an event loop


GridManagerDemo()  # Create GUI

print("------------------------------------------------------------")  # 60個

# PackManagerDemoWithSide

from tkinter import *  # Import tkinter


class PackManagerDemoWithSide:
    window = Tk()  # Create a window
    window.title("Pack Manager Demo 2")  # Set title

    Label(window, text="Blue", bg="blue").pack(side=LEFT)
    Label(window, text="Red", bg="red").pack(side=LEFT, fill=BOTH, expand=1)
    Label(window, text="Green", bg="green").pack(side=LEFT, fill=BOTH)

    window.mainloop()  # Create an event loop


PackManagerDemoWithSide()  # Create GUI
'''
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("800x600")
window.title("這是主視窗")

frame1 = tk.Frame(window)
frame1.pack()

#Entry 之 Text 之 對齊
tk.Entry(frame1, width=5, justify=tk.RIGHT).pack(side=tk.LEFT)
tk.Entry(frame1, width=5, justify=tk.RIGHT).pack(side=tk.LEFT)
tk.Entry(frame1, width=5, justify=tk.RIGHT).pack(side=tk.LEFT)


print("Toolbox 測試")
tk.Button(window, text="OK").pack(side=tk.LEFT)
tk.Button(window, text="Cancel").pack(side=tk.LEFT)
tk.Label(window, text="Enter your name:").pack(side=tk.LEFT)
tk.Entry(window, text="Type Name").pack(side=tk.LEFT)
tk.Checkbutton(window, text="Bold").pack(side=tk.LEFT)
tk.Checkbutton(window, text="Italic").pack(side=tk.LEFT)
tk.Radiobutton(window, text="Red").pack(side=tk.LEFT)
tk.Radiobutton(window, text="Yellow").pack(side=tk.LEFT)







window.mainloop()


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



