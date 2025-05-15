"""
文字轉語音
語音引擎 pyttsx3

"""

import sys
import pyttsx3

print("------------------------------------------------------------")  # 60個

# 設定語音引擎
engine = pyttsx3.init()
engine.setProperty("rate", 145)  # 設定語速
engine.setProperty("volume", 1.0)  # 設定音量 (1.0 為最大值)

# 向使用者解釋程序
engine.say(
    "當螢幕提示時，請輸入你的訊息。\
           直到聽到提示喊停為止。"
)
engine.runAndWait()

engine.stop()  # 停止 pyttsx3 引擎

print("------------------------------------------------------------")  # 60個

engine = pyttsx3.init()

test_txt="I am a good student 新手一定要玩的MNIST手寫數字辨識"

voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)                                                     #you can change the rate here
for voice in voices:
    print(voice)
    engine.setProperty('voice',voice.id)
    engine.say(test_txt)       
    engine.runAndWait()

print("------------------------------------------------------------")  # 60個

text = "Welcome to the United Stated and have a nice day."

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 10)
engine.say(text)
engine.runAndWait()

print("------------------------------------------------------------")  # 60個

# Changing Voice , Rate and Volume

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty("rate")  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty("rate", 125)  # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty(
    "volume"
)  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty("volume", 1.0)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty("voices")  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty(
    "voice", voices[1].id
)  # changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say("My current speaking rate is " + str(rate))
engine.runAndWait()
engine.stop()

print("存成mp3檔")
engine.save_to_file("Hello World", "test.mp3")
engine.runAndWait()

print("------------------------------------------------------------")  # 60個

import time

# 設定語音引擎
engine = pyttsx3.init()
engine = pyttsx3.init("sapi5")

engine.setProperty("rate", 145)  # 設定語速
engine.setProperty("volume", 1.0)  # 設定音量 (1.0 為最大值)

engine.say("壬戌之秋，七月既望，蘇子與客泛舟遊於赤壁之下。")
engine.runAndWait()
time.sleep(3)

engine.stop()  # 停止 pyttsx3 引擎

print("------------------------------------------------------------")  # 60個

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(s):
    engine.say(s)
    engine.runAndWait()


text = "語言技術：Python 資料科學"
speak(text)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



print("------------------------------------------------------------")  # 60個



