# ch33_2.py
import pygame
pygame.mixer.init()

pygame.time.delay(1000)                     # 先給聲音初始化工作

soundObj = pygame.mixer.Sound('punch.wav')  # 建立Sound物件
soundObj.play()                             # 撥放一次
pygame.time.delay(3000)                     # 休息3秒
soundObj.set_volume(0.1)                    # 聲音變小
soundObj.play(2)                            # 播放3次







