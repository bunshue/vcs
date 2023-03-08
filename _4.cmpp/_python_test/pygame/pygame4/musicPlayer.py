import pygame
import Tkinter as tk
window = tk.Tk()
pygame.init()

pygame.mixer.music.load("music.mp3")

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
