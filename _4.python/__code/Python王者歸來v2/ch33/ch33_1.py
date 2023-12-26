# ch33_1.py
import pygame
pygame.mixer.init()

soundObj = pygame.mixer.Sound('punch.wav')  # 建立Sound物件
soundObj.play()                             # 撥放一次
pygame.time.delay(3000)                     # 休息3秒
soundObj.play(2)                            # 播放3次







