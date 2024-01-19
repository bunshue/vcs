import sys

from moviepy.editor import VideoFileClip
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

print("------------------------------------------------------------")  # 60個

if __name__=='__main__':
	#用一位老同学写的短诗的中英文作为TextClip显示内容，由于内容过长需要滚动显示
    text = """致敬奋战在一线的巾帼女英雄  

    你也是孩子的妈妈，

    你也是爸妈的孩子。

    但你说只要穿上白大褂，

    我就是一名医护人员，

    这就是我的职责。

    我看不清你的长相，

    在层层的防护服里，

    都是一颗颗金子般的心。

    “青山一道同云雨，明月何曾是两乡”

    引用自王昌龄的《送柴侍御》，

    为在抗击疫情一线的女性“逆行者”致敬。

    中国加油！武汉加油！

    武汉人民感谢所有白衣天使！

    Pay tribute to the heroine fighting in the front line
            Yao Junfeng, Wuhan University
    
    You are also the mother of the child,
    You're also a parent's child.
    But you said just put on the white coat,
    I'm a healthcare worker,
    This is my duty.
    I can't see what you look like,
    In layers of protective clothing,
    Every heart is like gold.
    "The green mountains are the same as the clouds and the rain. How could the bright moon be the two villages?"
    It is quoted from Wang Changling's "See  Mr. Chai Off",

    To pay tribute to the female "reverse" in the front line of fighting the epidemic.

    Go China! Come on, Wuhan!

    Wuhan people thank all angels in white!

    """
    clip = VideoFileClip("kkkk.mp4", audio=False).crop(0, 300, 540, 840).subclip(0, 0.05)
    txtclip = TextClip(text, font='仿宋_GB2312', fontsize=18, color='blue', bg_color='white', transparent=True).set_duration(30).resize((clip.size[0], clip.size[1] * 2)).set_fps(clip.fps).set_start(clip.end)

    w = None
    h = clip.size[1]
    x_speed = x_start = y_start = 0
    y_speed = 20
    txtclip = txtclip.fx(vfx.scroll, w, h, x_speed, y_speed, x_start, y_start)  # .set_start(clip.end)

    newclip = CompositeVideoClip([txtclip, clip], bg_color=(255, 255, 255), ismask=False)
    newclip.write_videofile(r"F:\video\WinBasedWorkHard_scroll.mp4", threads=8)
print("------------------------------------------------------------")  # 60個



import os

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

if os.path.exists(filename):
    print(filename, ":", os.path.getsize(filename))
else:
    print(filename,"檔案不存在")
    
print("------------------------------------------------------------")  # 60個

import shutil

srcfilename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
dstfilename = "tmp_pic.jpg"

shutil.copy(srcfilename, dstfilename)       # 檔案複製

print("------------------------------------------------------------")  # 60個
"""
srcfilename = input("請輸入來源檔案 : ")
dstfilename = input("請輸入目的檔案 : ")        
with open(srcfilename) as src_Obj:        # 用預設mode=r開啟檔案,傳回檔案物件src_Obj
    data = src_Obj.read()           # 讀取檔案到變數data

with open(dstfilename, 'w') as dst_Obj:   # 開啟檔案mode=w
    dst_Obj.write(data)             # 將data輸出到檔案

"""

print("------------------------------------------------------------")  # 60個
"""
import zipfile
import glob, os
zipdir = input("請輸入欲壓縮的目錄 : ")
zipdir = zipdir + '/*'
zipfilename = input("請輸入保存壓縮檔案的名稱 : ")

fileZip = zipfile.ZipFile(zipfilename, 'w')
for name in glob.glob(zipdir):        # 遍歷zipdir目錄
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
fileZip.close()
"""
print("------------------------------------------------------------")  # 60個

"""
def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    global mydict
    songList = songCount.split()    # 將歌曲字串轉成串列
    mydict = {wd:songList.count(wd) for wd in set(songList)}

filename = "AreYouSleeping.txt"
with open(filename) as file_Obj:          # 開啟歌曲檔案
    data = file_Obj.read()          # 讀取歌曲檔案

mydict = {}                         # 空字典未來儲存單字計數結果
song = modifySong(data.lower())

wordCount(song)                     # 執行歌曲單字計數

dictList = sorted(mydict.items(), key=lambda item:item[1], reverse=True)
for key, val in dictList:
    print(key,':',val)
"""

print("------------------------------------------------------------")  # 60個

import os

files = ['c1.py', 'c2.py', 'c3.py']
for file in files:
    print(os.path.join('D:\\test', file))   

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

  




