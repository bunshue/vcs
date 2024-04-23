import tkinter as tk
from StillClock import StillClock
   
def setNewTime():
    clock.setHour(hour.get())
    clock.setMinute(minute.get())
    clock.setSecond(second.get())
    
window = tk.Tk()
window.title("Change Clock Time")

clock = StillClock(window)
clock.pack()

frame = tk.Frame(window)
frame.pack()
tk.Label(frame, text = "Hour: ").pack(side = tk.LEFT)
hour = tk.IntVar()
hour.set(clock.getHour())
tk.Entry(frame, textvariable = hour, width = 2).pack(side = tk.LEFT) 
tk.Label(frame, text = "Minute: ").pack(side = tk.LEFT)
minute = tk.IntVar()
minute.set(clock.getMinute())
tk.Entry(frame, textvariable = minute, width = 2).pack(side = tk.LEFT) 
tk.Label(frame, text = "Second: ").pack(side = tk.LEFT)
second = tk.IntVar()
second.set(clock.getMinute())
tk.Entry(frame, textvariable = second, width = 2).pack(side = tk.LEFT) 
tk.Button(frame, text = "設定時間", command = setNewTime).pack(side = tk.LEFT)

window.mainloop()
