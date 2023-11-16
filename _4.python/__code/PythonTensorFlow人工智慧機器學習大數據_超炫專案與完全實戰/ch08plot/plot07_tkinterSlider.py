#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"

try:
  import Tkinter as tk
except ImportError:
  import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

win = tk.Tk()
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, win)
canvas.get_tk_widget().pack()
ax=fig.add_subplot(111)
fig.subplots_adjust(bottom=0.25)

x = [5,6,7,8]
ax.plot(x,x)
ax.axis([0,10, 0, 10])

ax_time = fig.add_axes([0.12, 0.1, 0.78, 0.03])
Slider1 = Slider(ax_time, 'Time', 0, 30, valinit=0)

def update(val):
    pos = Slider1.val
    ax.axis([pos, pos+10, 0, 10])
    fig.canvas.draw_idle()
Slider1.on_changed(update)

tk.mainloop()