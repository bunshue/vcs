def menu(status):
    os.system("cls")
    print("mp3 播放器  {}".format(status))
    print("--------------------------------------")
    print("1. 播  放")
    print("2. 上一首")
    print("3. 下一首")
    print("4. 暫  停")
    print("5. 停止播放")
    print("0. 結束程式")
    print("--------------------------------------")
    
def playmp3(song):
    global status
    print(mixer.music.get_busy())
    if not mixer.music.get_busy():
        mixer.music.load(mp3files[index])
        mixer.music.play() 
    else:
        mixer.music.unpause() 
    status="正在播放 {}".format(mp3files[index])            
    
def playNewmp3(song):
    global status
    mixer.music.stop()
    mixer.music.load(mp3files[index])   
    mixer.music.play()      
    status="正在播放 {}".format(mp3files[index])   
    
### 主程式從這裡開始 ###
    
# pip install pygame
from pygame import mixer
import glob,os
mixer.init()

source_dir = 'C:/_git/vcs/_1.data/______test_files1/_mp3/'

mp3files = glob.glob(source_dir+"*.mp3")
index=0
status=""

while True:
    menu(status)
    print()
    choice = int(input("請輸入您的選擇："))
    if choice==1:
         playmp3(mp3files[index])
    elif choice==2:
        index +=1
        if index==len(mp3files):
            index=0 
        playNewmp3(mp3files[index])            
    elif choice==3:
        index -=1
        if index<0:
            index=len(mp3files)-1  
        playNewmp3(mp3files[index])            
    elif choice==4:
        mixer.music.pause() 
        status="暫停播放 {}".format(mp3files[index]) 
    elif choice==5:
        mixer.music.stop()
        status="停止播放" 
    else:
        break
    
mixer.music.stop()    
print("程式執行完畢！")
