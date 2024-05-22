# coding:utf-8
#
#file PlantsVsZombies.py

import pygame, random, sys, time
from pygame.locals import *

UI_Width = 1024  #游戲視窗寬度
UI_Height = 600  #游戲視窗高度
FPS = 60	#框頻

MAX_Into = 10 #最大僵屍透過數(超過此數，游戲結束)
Zombie_Width = 50 #僵屍寬度
Zombie_Height = 90 #僵屍高度

Zombie_Total = 50 #僵屍總數

Zombie_Add_Rate = 30  #僵屍增加頻率

Zombie_Speed = 2  #僵屍1向左搬移的速度
Zombie2_Speed = Zombie_Speed / 2  #僵屍2向左搬移的速度

Emitter_Move_Dist = 10  #發射器每次搬移距離
Bullet_Speed = 10	#子彈的速度
Bullet_Add_Rate = 15 #子彈清單中加入子彈的頻率

Zombies_List = []   #儲存僵屍1的清單
Zombies2_List = []  #儲存僵屍2的清單
Bullets_List = []	#子彈清單

Into_Base_Zombies = 0  #透過的僵屍數量
Score = 0				#積分

Add_Zombie_Total = 0 #加入的僵屍總數

Zombie_Rate_Counter = 0	#僵屍1頻率計數器
Zombie2_Rate_Counter = 0  #僵屍2頻率計數器
Bullet_Rate_Counter = 40		#子彈計數器

TEXTCOLOR = (255, 255, 255) #文字彩色

#上下左右搬移標志
To_Left = False
To_Right = False	
To_Up = False
To_Down = False
#射擊標志
Shoot = False


# 離開游戲 
def quit():
    pygame.quit()
    sys.exit()

def init():
    global Zombies_List,Zombies2_List,Bullets_List,Into_Base_Zombies,Score,Add_Zombie_Total
    global To_Left,To_Right,To_Up,To_Down,Shoot
    Zombies_List = []   #儲存僵屍的清單
    Zombies2_List = []  #儲存新僵屍的清單
    Bullets_List = []	#子彈清單
    Into_Base_Zombies = 0  #進入基地的僵屍數量
    Score = 0				#積分
    Add_Zombie_Total = 0 #加入的僵屍總數
    To_Left = To_Right = To_Up = To_Down = Shoot = False

#開始界面時等待游戲者按鍵
def waitPressKey():
    global Zombies_List,Zombies2_List,Bullets_List,Into_Base_Zombies,Score,Add_Zombie_Total
    while True:			#無窮迴圈
        for event in pygame.event.get():	#取得事件
            if event.type == QUIT:			#事件型態為離開
                quit()					#離開游戲
            if event.type == KEYDOWN:		#按鍵事件
                if event.key == K_ESCAPE:	#按下ESC鍵
                    quit()				#離開游戲
                if event.key == K_RETURN:	#按下換行
                    init()
                    return					#離開無窮迴圈

#顯示字串
def DisplayStr(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#判斷僵屍是否擊中發射器
def EmitterWasHit(EmitterRect, z):
    for z in Zombies_List:
        if EmitterRect.colliderect(z['rect']):
            gameHit1Sound.play()
            return True
    return False

#判斷子彈是否擊中了僵屍1
def ZombieWasHit(Bullets_List, z):
    for b in Bullets_List:
        if b['rect'].colliderect(z['rect']):
            Bullets_List.remove(b) #移除子彈
            gameHit2Sound.play()
            return True
    return False
#判斷子彈是否擊中了僵屍2
def Zombie2WasHit(Bullets_List, c):
    for b in Bullets_List:
        if b['rect'].colliderect(c['rect']):
            Bullets_List.remove(b)
            return True
    return False

#處理各類別事件
def ProcEvent():
    global To_Up,To_Down,Shoot

    for event in pygame.event.get():  #取得事件
        if event.type == QUIT:			#離開事件
            quit()					#離開游戲

        if event.type == KEYDOWN:		#鍵碟按下事件
            if event.key == K_UP or event.key == ord('w'):	#按了向上鍵或字母w
                To_Down = False	#設定向下為False
                To_Up = True		#設定向上為True
            if event.key == K_DOWN or event.key == ord('s'):	#按了向上鍵或字母s
                To_Up = False
                To_Down = True

            if event.key == K_SPACE:	#按了空白鍵
                Shoot = True		#設定發射子彈

        if event.type == KEYUP:		#鍵碟放開事件
            if event.key == K_ESCAPE:	#松開ESC鍵
                quit()			#離開游戲

            if event.key == K_UP or event.key == ord('w'): #松開向上鍵或字母w
                To_Up = False
            if event.key == K_DOWN or event.key == ord('s'):
                To_Down = False

            if event.key == K_SPACE:	#松開空白鍵
                Shoot = False

        if event.type == MOUSEBUTTONDOWN: #滑鼠按下
            Shoot = True

        if event.type == MOUSEBUTTONUP:		#滑鼠松開
            Shoot = False

#向游戲中增加角色
def AddRoles():
    # 增加僵屍
    global Add_Zombie_Total,Zombie_Rate_Counter,Zombie_Rate_Counter,Zombie2_Rate_Counter,Bullet_Rate_Counter,Bullet_Rate_Counter
    if Add_Zombie_Total < Zombie_Total : #若果僵屍數量少於總數
        Zombie_Rate_Counter += 1
        if Zombie_Rate_Counter == Zombie_Add_Rate:
            Zombie_Rate_Counter = 0		#計數器清0
            zombieSize_X = Zombie_Width
            zombieSize_Y = Zombie_Height
            newZombie = {'rect': pygame.Rect(UI_Width, random.randint(10,UI_Height-zombieSize_Y-10), zombieSize_X, zombieSize_Y),
                    'surface':pygame.transform.scale(zombieImage, (zombieSize_X, zombieSize_Y)),
                    }

            Zombies_List.append(newZombie) #新增到僵屍清單中
            Add_Zombie_Total += 1

        # 增加僵屍2
        Zombie2_Rate_Counter += 1 #計數器加1
        if Zombie2_Rate_Counter == Zombie_Add_Rate:
            Zombie2_Rate_Counter = 0		#計數器清0

            zombie2Size_X = Zombie_Width
            zombie2Size_Y = Zombie_Height
            newZombie2 = {'rect': pygame.Rect(UI_Width, random.randint(10,UI_Height-zombie2Size_Y-10), zombie2Size_X, zombie2Size_Y),
                    'surface':pygame.transform.scale(Zombie2Image, (zombie2Size_X, zombie2Size_Y)),
                }
            Zombies2_List.append(newZombie2) #新增到僵屍2清單中
            Add_Zombie_Total += 1

    # 加入子彈
    Bullet_Rate_Counter += 1  #子彈計數器加1
    if Bullet_Rate_Counter >= Bullet_Add_Rate and Shoot == True:
        Bullet_Rate_Counter = 0 #計數器清0
        #產生新的子彈
        newBullet = {'rect':pygame.Rect(EmitterRect.centerx+10, EmitterRect.centery-25, bulletRect.width, bulletRect.height),
                 'surface':pygame.transform.scale(bulletImage, (bulletRect.width, bulletRect.height)),
                }
        Bullets_List.append(newBullet) #新增到子彈清單

#更新角色狀態
def RolesStatus():
    global Score, Into_Base_Zombies
    # 搬移子彈發射器
    if To_Up and EmitterRect.top > 30:  #向上且有向上的空間
        EmitterRect.move_ip(0,-1 * Emitter_Move_Dist)
    if To_Down and EmitterRect.bottom < UI_Height-10: #向下搬移
        EmitterRect.move_ip(0,Emitter_Move_Dist)

    # 僵屍1搬移
    for z in Zombies_List:
        z['rect'].move_ip(-1*Zombie_Speed, 0)

    # 僵屍2搬移
    for c in Zombies2_List:
        c['rect'].move_ip(-1*Zombie2_Speed,0)

    # 搬移子彈
    for b in Bullets_List:
        b['rect'].move_ip(1 * Bullet_Speed, 0)

    # 移除已搬移到左側的僵屍1(檢查判斷)
    for z in Zombies_List[:]:
        if z['rect'].left < 0:
            Zombies_List.remove(z)  #從清單中移除
            Into_Base_Zombies += 1  #增加進入基地的僵屍數量

    # 移除已搬移到左側的僵屍2(檢查判斷)
    for c in Zombies2_List[:]:
        if c['rect'].left <0:
            Zombies2_List.remove(c)
            Into_Base_Zombies += 1

    #移除已到右邊界的子彈
    for b in Bullets_List[:]:
        if b['rect'].right>UI_Width:
            Bullets_List.remove(b)

    # 檢查子彈是否擊中了僵屍
    for z in Zombies_List: #循環檢查每一個僵屍
        if ZombieWasHit(Bullets_List, z):
            Score += 1	#積分加1
            Zombies_List.remove(z)  #移除僵屍

    for c in Zombies2_List:
        if Zombie2WasHit(Bullets_List, c):
            Score += 1
            Zombies2_List.remove(c)

#在場景中重畫角色
def ReDraw():
    GameWin.blit(rescaledBackground, (0, 0))

    # 繪制發射器
    GameWin.blit(EmitterImage, EmitterRect)

    # 繪制每一個僵屍
    for z in Zombies_List:
        GameWin.blit(z['surface'], z['rect'])

    for c in Zombies2_List:
        GameWin.blit(c['surface'], c['rect'])

    # 繪制每一枚子彈
    for b in Bullets_List:
        GameWin.blit(b['surface'], b['rect'])

    # 顯示得分和透過左邊僵屍的數量
    DisplayStr('透過僵屍: %s' % (Into_Base_Zombies), font, GameWin, 10, 20)
    DisplayStr('擊斃僵屍: %s' % (Score), font, GameWin, 10, 50)

    pygame.display.update()# 更新畫面

#檢查勝負
def CheckWinOrLose():
    pygame.mixer.music.stop()	#停止音樂
    gameOverSound.play()	#播放游戲結束音樂
    time.sleep(4)	#延時
    gameOverSound.stop()
    GameWin.blit(rescaledBackground, (0, 0))  #繪制背景
    GameWin.blit(EmitterImage, (UI_Width / 2, UI_Height - 70))  #繪制發射器
    DisplayStr('擊斃僵屍: %s' % (Score), font, GameWin, 10, 30)
    DisplayStr('GAME OVER', font, GameWin, UI_Width / 2 - 75, UI_Height / 3)
    DisplayStr('按確認鍵重玩，或按ESC離開', font, GameWin, UI_Width / 2 - 200, UI_Height / 3 + 150)
    if Into_Base_Zombies >= MAX_Into:  #僵屍透過數量超過最大數
        DisplayStr('僵屍已搶占了你的基地', font, GameWin, UI_Width / 2- 165, UI_Height / 3 + 100)
        gameLoseSound.play()
    if EmitterWasHit(EmitterRect, Zombies_List): #僵屍擊中發射器
        DisplayStr('你被僵屍擊中了', font, GameWin, UI_Width / 2 - 110, UI_Height / 3 +100)
        gameLoseSound.play()
    if Score + Into_Base_Zombies >= Zombie_Total:
        DisplayStr('你擊敗了僵屍的進攻', font, GameWin, UI_Width / 2 - 160, UI_Height / 3 +100)	
        gameWinSound.play()


pygame.init()	#起始化pygame模組
mainClock = pygame.time.Clock()
GameWin = pygame.display.set_mode((UI_Width, UI_Height))#設定游戲場地的大小
pygame.display.set_caption('植物大戰僵屍')  #設定視窗標題
pygame.mouse.set_visible(True) #顯示滑鼠指標
font = pygame.font.SysFont("simsunnsimsun", 32)	#設定字型

gameOverSound = pygame.mixer.Sound('gameover.wav')  #游戲結束音效
gameWinSound = pygame.mixer.Sound('winmusic.wav')  #游戲勝利音效
gameLoseSound = pygame.mixer.Sound('losemusic.wav')  #游戲失敗音效
gameHit1Sound = pygame.mixer.Sound('hit1.wav')  #僵屍擊中發射器音效
gameHit2Sound = pygame.mixer.Sound('hit2.wav')  #子彈擊中僵屍音效
pygame.mixer.music.load('background.mp3')

EmitterImage= pygame.image.load('Emitter.gif')# 設定游戲者發射圖片
EmitterRect = EmitterImage.get_rect()

bulletImage = pygame.image.load('Bullet.gif')# 設定子彈圖片
bulletRect = bulletImage.get_rect()

zombieImage = pygame.image.load('Zombie1.png')#僵屍1圖片
Zombie2Image = pygame.image.load('Zombie2.png') #僵屍2圖片
backgroundImage = pygame.image.load('background.jpg')#設定背景圖片
logoImage = pygame.image.load('PvZ_Logo.png') #設定Logo圖片
rescaledBackground = pygame.transform.scale(backgroundImage, (UI_Width, UI_Height)) #將背景圖縮放到游戲視窗大小

GameWin.blit(rescaledBackground, (0, 0)) #把背景畫到游戲視窗
GameWin.blit(logoImage,(UI_Width / 2 - 275, 150))
GameWin.blit(EmitterImage, (UI_Width / 2, UI_Height - 70)) #把游戲者的子彈發射器畫到螢幕對應位置

DisplayStr('按確認鍵開始', font, GameWin, UI_Width / 2 - 95, 300)
pygame.display.update() #更新螢幕
waitPressKey() #等待使用者按確認鍵，開始游戲


#進入游戲
while True:
    EmitterRect.topleft = (30, UI_Height /2) #將發射器放置距左側30，垂直位置置中的地方

    pygame.mixer.music.play(-1) #循環播放音樂

    while True:  
        ProcEvent()
        AddRoles()	#加入角色到游戲
        RolesStatus() #更新角色狀態（搬移、移除、檢查邊界）
        ReDraw()  #重繪畫面

        # 檢查僵屍是否擊中發射器，若擊中，則游戲結束
        if EmitterWasHit(EmitterRect, Zombies_List):
            break
        if EmitterWasHit(EmitterRect, Zombies2_List):
           break
        
        # 檢查透過的僵屍數量是否達到最大值，若是，則游戲結束
        if Into_Base_Zombies >= MAX_Into:
            break

        if Score + Into_Base_Zombies >= Zombie_Total:
            break

        mainClock.tick(FPS) #設定最大框率

    # 跳出循環，則停止游戲
    CheckWinOrLose() #檢查勝負
    pygame.display.update() #更新畫面
    waitPressKey()#等待按鍵




