

mp3_filename = 'C:/_git/vcs/_1.data/______test_files1/_mp3/16.監獄風雲.mp3'

print("------------------------------------------------------------")  # 60個

print('用tk.Scale控制聲音大小')

import pygame
import tkinter as tk

window = tk.Tk()

pygame.init()

pygame.mixer.music.load(mp3_filename)

started = False
playing = False

def buttonClick():
    global playing, started
    if not playing:
        if not started:
            pygame.mixer.music.play(-1)
            started = True
        else:
            pygame.mixer.music.unpause()
        button.config(text="Pause")
    else:
        pygame.mixer.music.pause()
        button.config(text="Play")
    playing = not playing


def setVolume(val):
    volume = float(slider.get())
    pygame.mixer.music.set_volume(volume / 100)

slider = tk.Scale(window, from_=100, to=0, command=setVolume)
button = tk.Button(window, text="Play", command=buttonClick)
slider.pack()
slider.set(100)
button.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個
