# ch19_9.py
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下以圓形為基礎
canvas.create_arc(10, 10, 110, 110, extent=180, style=ARC)
canvas.create_arc(210, 10, 310, 110, extent=180, style=CHORD)
canvas.create_arc(410, 10, 510, 110, start=30, extent=120, style=PIESLICE)










