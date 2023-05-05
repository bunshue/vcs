import pygame

pygame.init()

windowSize = [400, 300]
pygame.display.set_mode(windowSize)


filename1 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/16.監獄風雲.mp3'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/_wav/harumi.wav'

'''
file1 = pygame.mixer.Sound(filename1)
file2 = pygame.mixer.Sound(filename2)
file3 = pygame.mixer.Sound(filename3)

done = False
while not done:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        file1.play()
        file2.stop()
        file3.stop()

    if keys[pygame.K_2]:
        file1.stop()
        file2.play()
        file3.stop()

    if keys[pygame.K_3]:
        file1.stop()
        file2.stop()
        file3.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
'''



import pygame


pygame.mixer.init()
pygame.mixer.music.load(filename3)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.delay(200)

