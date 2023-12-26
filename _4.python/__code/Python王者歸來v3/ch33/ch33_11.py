# ch33_11.py
from gtts import gTTS
import pygame

text = "我愛明志科技大學!"
tts = gTTS(text=text, lang='zh-tw')
tts.save("hello.mp3")

pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()





