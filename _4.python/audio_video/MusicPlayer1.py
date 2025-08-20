"""
可播放 mp3
"""

import tkinter
import tkinter.filedialog

from win32com.client import Dispatch


class Window:
    def __init__(self):
        self.root = root = tkinter.Tk()  # 建立視窗
        buttonAdd = tkinter.Button(root, text="Add", command=self.add)
        buttonAdd.place(x=150, y=15)
        buttonPlay = tkinter.Button(root, text="Play", command=self.play)
        buttonPlay.place(x=200, y=15)
        buttonPause = tkinter.Button(root, text="Pause", command=self.pause)
        buttonPause.place(x=250, y=15)
        buttonStop = tkinter.Button(root, text="Stop", command=self.stop)
        buttonStop.place(x=300, y=15)
        buttonNext = tkinter.Button(root, text="Next", command=self.next)
        buttonNext.place(x=350, y=15)
        frame = tkinter.Frame(root, bd=2)
        self.playList = tkinter.Text(frame)
        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.config(command=self.playList.yview)
        self.playList.pack(side=tkinter.LEFT)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        frame.place(y=50)
        self.wmp = Dispatch("WMPlayer.OCX")  # 綁定WMPlayer.OCX

    def MainLoop(self):  # 進入訊息循環
        self.root.minsize(510, 380)
        self.root.maxsize(510, 380)
        self.root.mainloop()

    def add(self):  # 加入播放檔案
        file = tkinter.filedialog.askopenfilename(
            title="Python Music Player",
            filetypes=[("MP3", "*.mp3"), ("WMA", "*.wma"), ("WAV", "*.wav")],
        )
        if file:
            media = self.wmp.newMedia(file)
            self.wmp.currentPlaylist.appendItem(media)
            self.playList.insert(tkinter.END, file + "\n")

    def play(self):
        self.wmp.controls.play()  # 播放檔案

    def pause(self):
        self.wmp.controls.pause()  # 暫停

    def next(self):
        self.wmp.controls.next()  # 下一首

    def stop(self):
        self.wmp.controls.stop()  # 停止


window = Window()
window.MainLoop()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立 midi 檔案")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from midiutil.MidiFile import MIDIFile

# Create the MIDIFile Object
MyMIDI = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.
track = 0
time = 0

# Add track name and tempo.
MyMIDI.addTrackName(track, time, "Sample Track")
MyMIDI.addTempo(track, time, 120)

# C major scale
scale = [60, 62, 64, 65, 67, 69, 71, 72]

# Add a note. addNote expects the following information:
track = 0
channel = 0
pitch = scale[0]
time = 0
duration = 1
volume = 100

# Then add the scale notes
for i, pitch in enumerate(scale):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

# Write the MIDI file to disk
with open("tmp_create_midi.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 pygame 播放 midi 檔案")

import pygame

pygame.mixer.init()
pygame.mixer.music.load("data/HotelCalifornia.mid")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

pygame.mixer.quit()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
