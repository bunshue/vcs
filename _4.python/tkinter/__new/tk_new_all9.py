
"""
pLabel1= tk.Label(win, text="難度計算過程", fg="black", bg="silver", font=("新細明體",12),padx=20,pady=10 )

import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
ptext = tk.Text(win)
ptext.insert(tk.INSERT, "床前明月光\n")
ptext.insert(tk.INSERT, "疑是地上霜\n")
ptext.insert(tk.INSERT, "舉頭望明月\n")
ptext.insert(tk.INSERT, "低頭思故鄉\n")
ptext.pack()
ptext.config(state=tk.DISABLED)
win.mainloop()


text1 = tk.StringVar(value='GUI1')
ent1 = tk.Entry(win, textvariable=text1, width=15, justify=tk.CENTER)
ent1.grid(row=0, column=0, padx=5, pady=5)
text2 = tk.StringVar(value='GUI2')
ent2 = tk.Entry(win, textvariable=text2, width=15, justify=tk.CENTER)
ent2.grid(row=0, column=2, padx=5, pady=5, sticky=tk.N)
text3 = tk.StringVar(value='GUI3')
ent3 = tk.Entry(win, textvariable=text3, width=15, justify=tk.CENTER)
ent3.grid(row=1, column=1, padx=5, pady=5)

print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.font as tkfont
def radbut_click():
    selected_item = area.get()
    lab_result.config(text=AREA_OPTIONS[selected_item][0])
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
AREA_OPTIONS=(('屏東縣',0),('高雄市',1),('台南市',2),('台東縣',3))
area = tk.IntVar()
area.set(0)
for item, value in AREA_OPTIONS:
    radbut = tk.Radiobutton(win, text=item, variable=area, value=value, command=radbut_click, font=default_font)
    radbut.pack()
lab_result = tk.Label(win, font=default_font, fg='black')
lab_result.pack(padx=10, pady=(5,10))       
win.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
def combox_select(event):
    selected_area = event.widget.get()
    lab_result.config(text=selected_area)
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
AREA_OPTIONS=('屏東縣','高雄市','台南市','台東縣')
area = tk.StringVar()
combox = ttk.Combobox(win, value=AREA_OPTIONS, textvariable=area, font=default_font)
combox.bind('<<ComboboxSelected>>', combox_select)
combox.current(0)
combox.pack(padx=10, pady=10)
lab_result = tk.Label(win, font=default_font, fg='black', width=18)
lab_result.pack(padx=10, pady=(5,10))       
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_12.py

# Filename: ex09_12.py
import tkinter as tk
import tkinter.font as tkfont
def spinbox_select():
    selected_month = month.get()
    lab_result.config(text=selected_month)    
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
month = tk.IntVar()
month.set(1)
spinbox = tk.Spinbox(win, from_=1, to=12, textvariable=month, command=spinbox_select, font=default_font)
spinbox.pack(padx=10, pady=10)
lab_result = tk.Label(win, font=default_font, fg='black')
lab_result.pack(padx=10, pady=(5,10))    
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\ch09\ex09_13.py

# Filename: ex09_13.py
import tkinter as tk
import tkinter.font as tkfont
def but_click():
    selected_options = ''
    if asia.get():
        selected_options += chkbut_asia.cget('text')
    if america.get():
        selected_options += chkbut_america.cget('text')
    if europe.get():
        selected_options += chkbut_europe.cget('text')
    if aferica.get():
        selected_options += chkbut_aferica.cget('text')
    lab_result.config(text=selected_options)   
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
asia = tk.IntVar()
chkbut_asia = tk.Checkbutton(win, text='亞洲',variable=asia,anchor=tk.W)
chkbut_asia.pack(padx=90, pady=5, fill=tk.X)
america = tk.IntVar()
chkbut_america = tk.Checkbutton(win, text='美洲',variable=america,anchor=tk.W)
chkbut_america.pack(padx=90, pady=5, fill=tk.X)
europe = tk.IntVar()
chkbut_europe = tk.Checkbutton(win, text='歐洲',variable=europe,anchor=tk.W)
chkbut_europe.pack(padx=90, pady=5, fill=tk.X)
aferica = tk.IntVar()
chkbut_aferica = tk.Checkbutton(win, text='非洲',variable=aferica,anchor=tk.W)
chkbut_aferica.pack(padx=90, pady=5, fill=tk.X)
but = tk.Button(win, text='確定', command=but_click, font=default_font, padx=15)
but.pack(padx=10, pady=5)
lab_result = tk.Label(win, font=default_font, fg='black', width=20)
lab_result.pack(padx=10, pady=(5,10))
win.mainloop()

"""

print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.messagebox as tkmessagebox
import tkinter.font as tkfont
def Cal():
    tkmessagebox.showinfo(title="計算", message="計算資料中的試題難度")
def View():
    tkmessagebox.showinfo(title="檢視", message="檢視計算的結果")    
def About():
    tkmessagebox.showinfo(title="關於我們", message="程式設計者:屏東大學教育學系陳新豐")
def Exit():
    win.destroy() 
def main():
    global win
    win = tk.Tk()
    win.geometry("800x600")
    win.title("試題與測驗分析程式")
    default_font = tkfont.nametofont('TkDefaultFont')
    default_font.configure(size=15)
    menubar = tk.Menu(win)
    win.config(menu=menubar)
    menu_file = tk.Menu(menubar, tearoff = 0)
    menu_cal  = tk.Menu(menubar, tearoff = 0)
    menu_help = tk.Menu(menubar, tearoff = 0)    
    menubar.add_cascade(label='檔案', menu=menu_file)
    menubar.add_cascade(label='計算', menu=menu_cal)
    menubar.add_cascade(label='Help', menu=menu_help)
    menu_file.add_command(label='結束', command=Exit)
    menu_cal.add_command(label='計算', command=Cal)
    menu_cal.add_command(label='檢視', command=View)
    menu_help.add_command(label='關於', command=About)
    win.mainloop()
main()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

import tkinter as tk
import tkinter.font as tkfont
win = tk.Tk()
win.geometry("400x300")
win.title("圖形顯示")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
photo = tk.PhotoImage(file=filename)
gs = tk.Canvas(win)
gs.create_image(60,120,image=photo)
gs.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.font as tkfont
win = tk.Tk()
win.geometry("400x300")
win.title("幾何圖形")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
photo = tk.PhotoImage(file=filename)
gs = tk.Canvas(win,width=400,height=300)
gs.pack()
gs.create_rectangle(50,20,150,80)
gs.create_rectangle(80,60,200,100,fill='#FF0000')
gs.create_line(200,200,220,200)
gs.create_line(200,160,320,160,fill='#FF0000')                     
win.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
""" some wrong

from __future__ import unicode_literals
from pytube import YouTube
import tkinter as tk
import youtube_dl
import os

def Downmp4():
    yt = YouTube()
    yt.url = purl.get()
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    fvideo = yt.get("mp4", "360p")    
    fvideo.download(fpath)

def Downmp3():
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    os.chdir(fpath)    
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([purl.get()])

#main program
#製作2個視窗
win=tk.Tk()
win.geometry("600x400")
win.title("MP4與MP3下載")

frame1 = tk.Frame(win, width=600)
frame1.pack()

label1 = tk.Label(frame1, text="網址:")
label1.grid(row=0, column=0)
#label1.pack()
label2 = tk.Label(frame1, text="路徑:")
label2.grid(row=1, column=0)
#label2.pack()
#網址
purl  = tk.StringVar()
#路徑
ppath = tk.StringVar()

entry1 = tk.Entry(frame1, textvariable = purl, width=60)
entry1.grid(row=0, column=1)
#entry1.pack()
entry2 = tk.Entry(frame1, textvariable = ppath, width=60)
ppath.set("d:\music")
entry2.grid(row=1, column=1)
#entry2.pack()

btn1 = tk.Button(frame1, text="mp4", command=Downmp4)
#btn1.pack()
btn1.grid(row=2, column=1)
btn2 = tk.Button(frame1, text="mp3", command=Downmp3)
#btn2.pack()
btn2.grid(row=3, column=1)
#注意事項
label3 = tk.Label(frame1, text="本程式使用時請注意時間，保護眼睛。")
label3.grid(row=4, column=1)

win.mainloop()
"""

print("------------------------------------------------------------")  # 60個


#MP3播放器
def choose():
    global playsong
    message.set("\n播放歌曲：" + choice.get())
    playsong=choice.get()
def pausemp3(): 
    mixer.music.pause() 
    message.set("\n暫停播放 {}".format(playsong))   
def increase():
    global volume
    volume +=0.1
    if volume>=1.0:
        volume=1.0
    mixer.music.set_volume(volume) 
def decrease():
    global volume
    volume -=0.1
    if volume<=0.2:
        volume=0.2
    mixer.music.set_volume(volume)  
def playmp3():
    global status,playsong,preplaysong
    if playsong==preplaysong:
        if not mixer.music.get_busy():
            mixer.music.load(playsong)
            mixer.music.play(loops=-1) 
        else:
            mixer.music.unpause() 
        message.set("\n正在播放：{}".format(playsong))
    else:
        playnewmp3()
        preplaysong=playsong 
def playnewmp3():
    global playsong
    mixer.music.stop()
    mixer.music.load(playsong)   
    mixer.music.play(loops=-1)  
    message.set("\n正在播放：{}".format(playsong))
def stopmp3():
    mixer.music.stop()
    message.set("\n停止播放") 
def loadmp3():
    global volume
    global playsong
    global preplaysong
    global choice
    global pdir
    frame1 = tk.Frame(win)
    frame1.pack()
    mp3files = []
    mp3files = glob.glob(pdir.get()+"*.mp3")
    playsong=preplaysong = ""
    index = 0
    volume= 0.8
    choice = tk.StringVar()    
    for mp3 in mp3files:  
        prbutton = tk.Radiobutton(frame1,text=mp3,variable=choice,value=mp3,command=choose)
        if(index==0):     
            prbutton.select()
            playsong=preplaysong=mp3
        prbutton.grid(row=index, column=0, sticky="w")
        index += 1      
    message.set("\n讀取檔案")
def exitmp3():
    mixer.music.stop()
    win.destroy() 

import tkinter as tk
from pygame import mixer
import glob

mixer.init()
win=tk.Tk()
win.geometry("640x380")
win.title("MP3播放程式")
labeltitle = tk.Label(win, text="\nMP3播放程式", fg="blue",font=("標楷體",12))
labeltitle.pack()
frame0 = tk.Frame(win)
frame0.pack()
pdir = tk.StringVar()
plabel1 = tk.Label(frame0, text="請輸入目錄:", width=8)
plabel1.grid(row=0, column=0, padx=5, pady=5)
pentry = tk.Entry(frame0, textvariable=pdir, width=12)
pdir.set('music/')
pentry.grid(row=0, column=1, padx=5, pady=5)   
button1 = tk.Button(frame0, text="播放", width=8,command=playmp3)
button1.grid(row=1, column=0, padx=5, pady=5)
button2 = tk.Button(frame0, text="暫停", width=8,command=pausemp3)
button2.grid(row=1, column=1, padx=5, pady=5)
button3 = tk.Button(frame0, text="調大音量", width=8,command=increase)
button3.grid(row=1, column=2, padx=5, pady=5)
button4 = tk.Button(frame0, text="調小音量", width=8,command=decrease)
button4.grid(row=1, column=3, padx=5, pady=5)
button5 = tk.Button(frame0, text="停止", width=8,command=stopmp3)
button5.grid(row=1, column=4, padx=5, pady=5)
button7 = tk.Button(frame0, text="讀取檔案", width=8,command=loadmp3)
button7.grid(row=1, column=5, padx=5, pady=5)
button6 = tk.Button(frame0, text="結束", width=8,command=exitmp3)
button6.grid(row=1, column=6, padx=5, pady=5)
win.protocol("WM_DELETE_WINDOW", exitmp3)   
message = tk.StringVar()
message.set("\n播放歌曲：")
plabel2 = tk.Label(win, textvariable=message,fg="blue",font=("標楷體",10))
plabel2.pack() 
plabel3 = tk.Label(win, text="\n")
plabel3.pack()   
win.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.messagebox as tkmessagebox
import tkinter.filedialog as tkfiledialog
import tkinter.font as tkfont
def Cal():
    options = {}
    options['filetypes'] = [("allfiles","*"),("text","*.txt")]
    options['initialdir'] = "c:\\"
    options['multiple'] = False
    options['title'] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)    
    if fs:
        f = open(fs.name,'r')
        fc = f.readlines()
        f.close()
        fo = open('output.txt','w')
        fo.write("試題分析結果\n")
        pitem = int(fc[0][0:3])
        fo.write('題數:'+str(pitem)+'\n')
        pmiss = fc[0][4:5]
        fo.write('缺失:'+pmiss+'\n')
        pomit = fc[0][6:7]
        fo.write('遺漏:'+pomit+'\n')
        pid   = int(fc[0][8:10])
        fo.write('ID長度:'+str(pid)+'\n')
        pans  = fc[1]
        fo.write('答案:'+pans)
        pnum  = len(fc)-2
        fo.write('人數:'+str(pnum)+'\n')        
        psitem = []
        for j in range(0, pitem, 1):
            psitem.append(0)
        for i in range(0,pnum, 1):            
            for j in range(0,pitem, 1):                
                if (fc[2+i][pid+j]==pans[j]):                    
                    psitem[j] = psitem[j]+1                
        for j in range(0, pitem):
            fo.write('第'+str(j+1).rjust(2,'0')+'題，難度值p='+str(round(psitem[j]/pnum,2)).ljust(4,'0')+'\n')
        fo.close()
        tkmessagebox.showinfo(title="試題分析", message="分析完成")
    else:   
	     print ("沒有選擇檔案")
def View():
    options = {}
    options['filetypes'] = [("allfiles","*")]
    options['initialdir'] = "c:\\"
    options['multiple'] = False
    options['title'] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)    
    if fs:        
        f = open(fs.name,'r')
        fc= f.readlines()
        f.close()
        ptext = tk.Text(win, width=800, height=600)        
        for i in range(0, len(fc), 1):
            ptext.insert(tk.INSERT, fc[i])        
        ptext.pack()
        ptext.config(state=tk.DISABLED)       
    else:   
	     print ("沒有選擇檔案")
def About():
    tkmessagebox.showinfo(title="關於我們", message="程式設計者:屏東大學教育學系陳新豐")
def Exit():
    win.destroy() 
def main():
    global win    
    win = tk.Tk()
    win.geometry("800x600")
    win.title("試題與測驗分析程式")
    default_font = tkfont.nametofont('TkDefaultFont')
    default_font.configure(size=15)
    menubar = tk.Menu(win)
    win.config(menu=menubar)
    menu_file = tk.Menu(menubar, tearoff = 0)
    menu_cal  = tk.Menu(menubar, tearoff = 0)
    menu_help = tk.Menu(menubar, tearoff = 0)    
    menubar.add_cascade(label='檔案', menu=menu_file)
    menubar.add_cascade(label='計算', menu=menu_cal)
    menubar.add_cascade(label='Help', menu=menu_help)
    menu_file.add_command(label='結束', command=Exit)
    menu_cal.add_command(label='計算', command=Cal)
    menu_cal.add_command(label='檢視', command=View)    
    menu_help.add_command(label='關於', command=About)
    win.mainloop()
main()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch09\ex09_91.py

import tkinter as tk
import tkinter.messagebox as tkmessagebox
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")

tkmessagebox.askokcancel(title="對話方塊", message="askokcancel")

win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計入門與應用\二版範例資料\ch09\ex09_92.py

def checknum():
    pmsg.set("Small")

import tkinter as tk
import random as r

# create gui interface
win = tk.Tk()
win.geometry("400x300")
win.title("Guess Number")
ans=r.randint(0,100)
#print(ans)
#input guess number
pL1 = tk.Label(win, text="Please enter number:")
pL1.pack()
while (True):
    pnum = tk.StringVar()
    pE1 = tk.Entry(win, textvariable=pnum)
    pE1.pack()
    pB1 = tk.Button(win, text="OK", command=checknum)
    pB1.pack()

pmsg = tk.StringVar()
pL2 = tk.Label(win, textvariable=pmsg)
pL2.pack()

#num=121
#while (num!=ans):
#    num=int(input("please enter guess number:"))
#    if (num==ans):
#        break
#    if (num>ans):
#        print("bigger")
#    else:
#        print("smaller")   
#print("you are win")    

win.mainloop()


print("------------------------------------------------------------")  # 60個

""" syntax fail
from __future__ import unicode_literals
from pytube import YouTube

import tkinter as tk
import youtube_dl
import os

def Downmp4():
    #yt = YouTube()
    #yt.url = purl.get()
    yt = YouTube('%s'%purl.get())
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    #fvideo = yt.get("mp4", "360p")    
    fvideo = yt.streams.filter(file_extension='mp4', res='360p').first()
    fvideo.download(fpath)

def Downmp3():
    fpath = ppath.get()
    fpath = fpath.replace("\\","\\\\")
    os.chdir(fpath)    
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([purl.get()])

#main program
#製作2個視窗
win=tk.Tk()
win.geometry("600x400")
win.title("MP4與MP3下載")

frame1 = tk.Frame(win, width=600)
frame1.pack()

label1 = tk.Label(frame1, text="網址:")
label1.grid(row=0, column=0)
#label1.pack()
label2 = tk.Label(frame1, text="路徑:")
label2.grid(row=1, column=0)
#label2.pack()
#網址
purl  = tk.StringVar()
#路徑
ppath = tk.StringVar()

entry1 = tk.Entry(frame1, textvariable = purl, width=60)
entry1.grid(row=0, column=1)
#entry1.pack()
entry2 = tk.Entry(frame1, textvariable = ppath, width=60)
ppath.set("d:\music")
entry2.grid(row=1, column=1)
#entry2.pack()

btn1 = tk.Button(frame1, text="mp4", command=Downmp4)
#btn1.pack()
btn1.grid(row=2, column=1)
btn2 = tk.Button(frame1, text="mp3", command=Downmp3)
#btn2.pack()
btn2.grid(row=3, column=1)
#注意事項
label3 = tk.Label(frame1, text="本程式使用時請注意時間，保護眼睛。")
label3.grid(row=4, column=1)

win.mainloop()
"""
print("------------------------------------------------------------")  # 60個

def checkp():
    p3.set(p2.get()/(p1.get()*p1.get()/10000))
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("計算BMI程式")
frame1 = tk.Frame(win)
frame1.pack(padx=20, pady=10)
p1 = tk.IntVar()
p2 = tk.IntVar()
p3 = tk.DoubleVar()
pLabel = tk.Label(frame1, text="請輸入身高(公分)")
pLabel.pack()
pEn1 = tk.Entry(frame1, textvariable=p1)
pEn1.pack()
pLabe2 = tk.Label(frame1, text="請輸入體重(公斤)")
pLabe2.pack()
pEn2 = tk.Entry(frame1, textvariable=p2)
pEn2.pack()
pButton = tk.Button(frame1, text="計算BMI", command=checkp)
pButton.pack()
pLmsg = tk.Label(frame1, textvariable=p3)
pLmsg.pack()
win.mainloop()





print("------------------------------------------------------------")  # 60個



import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def openFile(): 
    filenameforReading = askopenfilename()
    infile = open(filenameforReading, "r")
    text.insert("end", infile.read()) # Read all from the file
    infile.close()  # Close the input file
    
def saveFile():
    filenameforWriting = asksaveasfilename()
    outfile = open(filenameforWriting, "w")
    # Write to the file
    outfile.write(text.get(1.0, "end")) 
    outfile.close() # Close the output file
    
window = tk.Tk()
window.title("簡易文字編輯器")
        
# Create a menu bar
menubar = tk.Menu(window)
window.config(menu = menubar) # Display the menu bar
        
# create a pulldown menu, and add it to the menu bar
operationMenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = operationMenu)
operationMenu.add_command(label = "Open", command = openFile)
operationMenu.add_command(label = "Save", command = saveFile)
        
# Add a tool bar frame 
frame0 = tk.Frame(window) # Create and add a frame to window
frame0.grid(row = 1, column = 1, sticky = "W")
        
# Create images
opneImage = tk.PhotoImage(file = "open.gif")
saveImage = tk.PhotoImage(file = "save.gif")
        
tk.Button(frame0, image = opneImage, command = openFile).grid(
                row = 1, column = 1, sticky = "W")
tk.Button(frame0, image = saveImage, command = saveFile).grid(
                row = 1, column = 2)
        
frame1 = tk.Frame(window) # Hold editor pane
frame1.grid(row = 2, column = 1)
        
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = "right", fill = "y")
text = tk.Text(frame1, width = 40, height = 20, wrap = "word",
               yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)
        
window.mainloop() # Create an event loop


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


