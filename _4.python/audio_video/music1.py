import sys
import pygame

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/16.監獄風雲.mp3'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/_wav/harumi99.wav'


filename4 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/mario.mp3'

pygame.mixer.init()
pygame.mixer.music.load(filename3)
pygame.mixer.music.play()

'''
pygame.mixer.init()
sound = pygame.mixer.Sound(filename3)
sound.play()
'''

print("------------------------------------------------------------")  # 60個


filename = 'C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3'


from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load(filename)
#mixer.music.play()



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


