import tkinter as tk

window = tk.Tk() # Create a window
window.title('左鍵變大 右鍵變小')

# 設定主視窗大小
w = 400
h = 400
size = str(w)+'x'+str(h)
window.geometry(size)

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(window, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
#msg.bind('<Motion>',motion)
msg.pack()

window.mainloop() # Create an event loop

