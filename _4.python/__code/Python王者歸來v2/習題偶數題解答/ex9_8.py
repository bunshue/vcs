# ex9_8.py
song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()            # 歌曲改為小寫

# 將歌曲的標點符號用空字元取代
for ch in songLower:                
        if ch in ".,?":
            songLower = songLower.replace(ch,'')

# 將歌曲字串轉成串列
songList = songLower.split()        

# 將歌曲串列處理成字典
dict = {wd:songList.count(wd) for wd in songList}
   
maxCount = max(dict.values())       # 出現最多次數
for key, count in dict.items():
    if count == maxCount:
        print(f"字串 {key} 出現最多次共出現 {count} 次")










