'''
文字轉語音

'''

import pyttsx3

text = 'Welcome to the United Stated and have a nice day.'

tts = pyttsx3.init()
tts.say(text)
tts.runAndWait()
