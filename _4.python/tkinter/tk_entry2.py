import tkinter as tk
from tkinter import ttk

# list of events
# pythontutorial.net/tkinter/tkinter-event-binding

def get_pos(event):
	print(f'x: {event.x} y: {event.y}')

# window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# widgets 
text = tk.Text(window)
text.pack()


# exercise : 
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

# run 
window.mainloop()
