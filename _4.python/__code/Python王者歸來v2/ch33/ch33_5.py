# ch33_5.py
import pygame
pygame.mixer.init()

pygame.time.delay(1000)                         # 先給聲音初始化工作
pygame.mixer.music.load('house_lo.mp3')         # 下載mp3音樂檔案
pygame.mixer.music.play(-1)                     # 永遠播放mp3音樂檔案
pygame.time.delay(3000)                         # 暫停3秒,mp3音樂繼續撥放
if pygame.mixer.music.get_busy():    
    pygame.mixer.music.pause()                  # 暫停播放             
    pygame.time.delay(3000)                     # 暫停3秒
    soundObj = pygame.mixer.Sound('punch.wav')  # 建立Sound物件
    soundObj.play()                             # 撥放Sound物件    
    pygame.time.delay(3000)                     # 暫停3秒
    pygame.mixer.music.unpause()                # 恢復播放

