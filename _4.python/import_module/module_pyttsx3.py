'''
文字轉語音

'''

import pyttsx3

print('------------------------------------------------------------')	#60個

text = 'Welcome to the United Stated and have a nice day.'

engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',10)
engine.say(text)
engine.runAndWait()

print('------------------------------------------------------------')	#60個

#Changing Voice , Rate and Volume

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

print('存成mp3檔')
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()


