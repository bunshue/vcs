import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

win = tk.Tk()
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, win)
canvas.get_tk_widget().pack()
ax=fig.add_subplot(111)

x = [5,6,7,8]
ax.plot(x)

tk.mainloop()

