import tkinter as tk

def convert():
    # Get the value entered by the user into the
    # kilo_entry widget.
    kilo = float(kilo_entry.get())

    # Convert kilometers to miles.
    miles = kilo * 0.6214

    print(kilo_entry.get())

    print('Results : ', str(kilo) + ' kilometers is equal to ' + str(miles) + ' miles.')
        

window = tk.Tk()

# Create two frames to group widgets.
top_frame = tk.Frame()
bottom_frame = tk.Frame()

# Create the widgets for the top frame.
prompt_label = tk.Label(top_frame, text='Enter a distance in kilometers:')
kilo_entry = tk.Entry(top_frame, width=10)

# Pack the top frame's widgets.
prompt_label.pack(side='left')
kilo_entry.pack(side='left')

# Create the button widgets for the bottom frame.
calc_button = tk.Button(bottom_frame, text='Convert', command=convert)
calc_button.pack(side='left')

# Pack the frames.
top_frame.pack()
bottom_frame.pack()

window.mainloop()
