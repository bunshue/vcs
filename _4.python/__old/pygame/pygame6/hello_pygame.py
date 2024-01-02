import pygame #滙入PyGame套件
import sys
pygame.init() #將PyGame初始化

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((300,300), 1)

#視窗標題列顯示文字
pygame.display.set_caption('我的第一支Pygame程式')

#依據事件做偵測，使用者是否按了右上角的X鈕
running = True
while running:
    for event in pygame.event.get():   #依據事件
        #判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
            pygame.quit() #quit()方法結束Pygame程序
            sys.exit()
