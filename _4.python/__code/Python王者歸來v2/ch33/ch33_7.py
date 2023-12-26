# ch33_7.py
from tkinter import *
import pygame

def playmusic():                                        # 處理按撥放紐
    selection = var.get()                               # 獲得音樂選項
    if selection == '1':
        pygame.mixer.music.load('house_lo.mp3')         # 撥放選項1音樂
        pygame.mixer.music.play(-1)                     # 循環撥放
    if selection == '2':
        pygame.mixer.music.load('NotifyPopup.mp3')      # 撥放選項2音樂
        pygame.mixer.music.play(-1)                     # 循環撥放
    if selection == '3':
        pygame.mixer.music.load('house_lo.mp3')         # 撥放選項3音樂
        pygame.mixer.music.play(-1)                     # 循環撥放 
def stopmusic():                                        # 處理按結束紐
    pygame.mixer.music.stop()                           # 停止撥放此首mp3
    
# 建立mp3音樂選項鈕內容的串列
musics = [('house_lo.mp3', 1),                          # 音樂選單串列
          ('NofityPopup.mp3', 2),
          ('happy.mp3', 3)]

pygame.mixer.init()                                     # 最初化mixer

tk = Tk()
tk.geometry('480x220')                                  # 開啟視窗
tk.title('Mp3 Player')                                  # 建立視窗標題
mp3Label = Label(tk, text='\n我的Mp3 撥放程式')         # 視窗內標題
mp3Label.pack()
# 建立選項紐Radio button
var = StringVar()                                       # 設定以字串表示選單編號
var.set('1')                                            # 預設音樂是1
for music, num in musics:                               # 建立系列選項紐
    radioB = Radiobutton(tk, text=music, variable=var, value=num)
    radioB.pack()
# 建立按鈕Button
button1 = Button(tk, text='撥放', width=10, command=playmusic)    # 撥放mp3音樂
button1.pack()
button2 = Button(tk, text='結束', width=10, command=stopmusic)    # 停止撥放mp3音樂
button2.pack()
mainloop()


