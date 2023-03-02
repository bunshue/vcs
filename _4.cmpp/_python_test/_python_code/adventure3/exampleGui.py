import Tkinter as tk
window = tk.Tk()

usernameBox = tk.Entry(window)
passwordBox = tk.Entry(window, show="*")
usernameLabel = tk.Label(window, text="Username")
passwordLabel = tk.Label(window, text="Password")
button = tk.Button(window, text="Login")

usernameLabel.grid(row=1, column=1)
usernameBox.grid(row=1, column=2)

passwordLabel.grid(row=2, column=1)
passwordBox.grid(row=2, column=2)

button.grid(row=3, column=2)

window.mainloop()