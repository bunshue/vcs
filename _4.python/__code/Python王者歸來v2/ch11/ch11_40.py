# ch11_40.py
def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    global mydict
    songList = songCount.split()    # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    mydict = {wd:songList.count(wd) for wd in set(songList)}

data = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""

mydict = {}                         # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)                     # 執行歌曲單字計數
print("以下是最後執行結果")
print(mydict)                       # 列印字典








