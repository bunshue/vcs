"""

winsound

"""

import sys

import winsound

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

duration_ms = 500
frqs=[262,294,330,349,392,440,494]

for i in range(7):
    winsound.Beep(frqs[i], duration_ms)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

wav_filename = "D:/_git/vcs/_1.data/______test_files1/_wav/harumi99.wav"

winsound.PlaySound(wav_filename, winsound.SND_FILENAME)

"""
winsound.SND_SYNC	同步播放
winsound.SND_ASYNC	非同步播放, 即背景音樂
winsound.SND_LOOP	循環播放
winsound.SND_ALIAS
winsound.SND_PURGE
winsound.SND_NOSTOP
winsound.SND_NODEFAULT
winsound.SND_MEMORY
"""


"""
winsound.Beep
winsound.Beep(440, 750)

winsound.MessageBeep(5000)#逼一聲
winsound.MessageBeep(winsound.MB_OK)
winsound.MessageBeep(winsound.MB_ICONASTERISK)
winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

winsound.MessageBeep(winsound.MB_ICONQUESTION)
"""

winsound.MessageBeep(winsound.MB_ICONHAND)

"""
winsound.MessageBeep, "bad")
winsound.MessageBeep, 42, 42)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


def fnSound(s):
    winsound.PlaySound("data/" + s + ".wav", winsound.SND_FILENAME)


def speakNumber(n):
    if n > 99:
        return
    n = str(n)
    if len(n) == 1:  # 若字串長度為1表個位數
        fnSound(n)  # 呼叫fnSound播放該數的音檔
    else:  # 兩位數時
        if n[0] != "1":  # 若第一個字不是1
            fnSound(n[0])  # 呼叫fnSound播放十位數的音檔
        fnSound("10")  # 呼叫fnSound播放10.wav
        if n[1] != "0":  # 若第一個字不是0
            fnSound(n[1])  # 呼叫fnSound播放個位數的音檔


print("把數字念出來")

number = 17
speakNumber(number)

number = 58
speakNumber(number)

number = 94
speakNumber(number)

number = 10
speakNumber(number)

number = 6
speakNumber(number)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
