def menu(status):
    os.system("cls")
    print("wav 播放器  {}".format(status))
    print("--------------------------------------")
    print("1. 播  放")
    print("2. 上一首")
    print("3. 下一首")
    print("4. 停止播放")
    print("0. 結束程式")
    print("--------------------------------------")
    
def playwav(song):
    global status,sound
    sound = mixer.Sound(wavfiles[index])
    sound.play(loops = 0)    
    status="正在播放 {}".format(wavfiles[index])            
    
def playNewwav(song):
    global status,sound
    sound.stop()
    sound = mixer.Sound(wavfiles[index])
    sound.play(loops = 0)      
    status="正在播放 {}".format(wavfiles[index])   
    
### 主程式從這裡開始 ###
    
from pygame import mixer
import glob,os
mixer.init()

source_dir = "wav/"
wavfiles = glob.glob(source_dir+"*.wav")
index=0
status=""
sound = mixer.Sound(wavfiles[index])

while True:
    menu(status)
    choice = int(input("請輸入您的選擇："))
    if choice==1:
         playwav(wavfiles[index])
    elif choice==2:
        index +=1
        if index==len(wavfiles):
            index=0 
        playNewwav(wavfiles[index])            
    elif choice==3:
        index -=1
        if index<0:
            index=len(wavfiles)-1  
        playNewwav(wavfiles[index])            
    elif choice==4:
        sound.stop()
        status="停止播放" 
    else:
        break
    
sound.stop()    
print("程式執行完畢！")