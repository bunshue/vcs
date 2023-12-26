# ex14_14.py
def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    global mydict
    songList = songCount.split()    # 將歌曲字串轉成串列
    mydict = {wd:songList.count(wd) for wd in set(songList)}

fn = "ch14_51.txt"
with open(fn) as file_Obj:          # 開啟歌曲檔案
    data = file_Obj.read()          # 讀取歌曲檔案

mydict = {}                         # 空字典未來儲存單字計數結果
song = modifySong(data.lower())

wordCount(song)                     # 執行歌曲單字計數

dictList = sorted(mydict.items(), key=lambda item:item[1], reverse=True)
for key, val in dictList:
    print(key,':',val)









