# ch9_33.py
song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
#mydict = {}                         # 省略,空字典未來儲存單字計數結果
print("原始歌曲")
print(song)

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()            # 歌曲改為小寫
print("小寫歌曲")
print(songLower)

# 將歌曲的標點符號用空字元取代
for ch in songLower:                
    if ch in ".,?":
        songLower = songLower.replace(ch,'')
print("不再有標點符號的歌曲")    
print(songLower)

# 將歌曲字串轉成串列
songList = songLower.split()        
print("以下是歌曲串列")
print(songList)                     # 列印歌曲串列

# 將歌曲串列處理成字典 
mydict = {wd:songList.count(wd) for wd in songList}
print("以下是最後執行結果")
print(mydict)                       # 列印字典









