import pygame, sys, random
from pygame.locals import *

#顏色值
White = (255, 255, 255)
Gray = (128, 128, 128)

FPS = 40 #每秒更換的速率

#將圖片切割成3*3的圖塊
Squares = 3
gridNums = Squares * Squares

def main():
   #初始化並設定時間元件
   pygame.init()
   mainClock = pygame.time.Clock()

   #載入圖片並以get_rect()方法取得圖片大小
   gameImage = pygame.image.load('pic\\bg02.jpg')
   gameRect = gameImage.get_rect()
      
   #產生視窗
   screen = pygame.display.set_mode((
      gameRect.width, gameRect.height))
   pygame.display.set_caption('簡易拼圖遊戲')
   
   #圖塊的大小依據圖片的寬和高再除以方塊數所得 width = 640/3
   gridWidth = int(gameRect.width / Squares)
   gridHeight = int(gameRect.height / Squares)
   #函式startGame()遊戲後取得圖塊和空白方格的狀態
   picSlice, waitMoveSqr = startGame()

   #播放音樂
   pygame.mixer.music.load('pic/tetrisb.mid')
   controlMusic = False

   finish = False   #尚未啟動遊戲

   #偵測遊戲的鍵盤和滑鼠
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            finishGame()
      
         #放開鍵盤事件
         if event.type == KEYUP:
            #按鍵盤的m鍵來播放/停止音樂
            if event.key == K_v:
               if controlMusic:
                  pygame.mixer.music.stop()
               else:
                  pygame.mixer.music.play(-1, 0.0)
               controlMusic = not controlMusic #當作切換開關
         
            #按鍵盤的Esc鍵就會離開程式
            if event.key == K_ESCAPE:
               finishGame()
            if finish:
               continue

         #配合左手，按下鍵盤的W、A、S、D來產生和方向鍵向上(W)、左(A)、下(S)、右(D)相同的效果
         if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
               waitMoveSqr = moveLeft(picSlice, waitMoveSqr)
            if event.key == K_RIGHT or event.key == K_d:
               waitMoveSqr = moveRight(picSlice, waitMoveSqr)
            if event.key == K_UP or event.key == K_w:
               waitMoveSqr = moveUp(picSlice, waitMoveSqr)
            if event.key == K_DOWN or event.key == K_s:
               waitMoveSqr = moveDown(picSlice, waitMoveSqr)

         #是否按下滑鼠的按鈕，方法mouse.get_pos()取得位置
         if event.type == MOUSEBUTTONDOWN and \
               event.button == 1:
            x, y = pygame.mouse.get_pos() #取得滑鼠座標
            
            #取得座標值之後，進一步找出滑鼠停留在圖塊的那個位置？
            posX = int(x / gridWidth)
            posY = int(y / gridHeight)
            index = posX + posY * Squares
            if (index == waitMoveSqr-1 or index == waitMoveSqr+1 \
                  or index == waitMoveSqr-Squares or \
                  index == waitMoveSqr+Squares):
               picSlice[waitMoveSqr], picSlice[index] = \
                  picSlice[index], picSlice[waitMoveSqr]
               waitMoveSqr = index
  
      if (isFinished(picSlice, waitMoveSqr)):
         picSlice[waitMoveSqr] = gridNums-1
         finish = True
      
      screen.fill(White)
      
      for k in range(gridNums):
         rowDst = int(k / Squares)
         colDst = int(k % Squares)
         rectDst = pygame.Rect(colDst * gridWidth, 
            rowDst*gridHeight, gridWidth, gridHeight)
  
         if picSlice[k] == -1:
            continue
  
         rowArea = int(picSlice[k] / Squares)
         colArea = int(picSlice[k] % Squares)
         rectArea = pygame.Rect(colArea*gridWidth, 
            rowArea*gridHeight, gridWidth, gridHeight)
         screen.blit(gameImage, rectDst, rectArea)
  
      for k in range(Squares+1):
         pygame.draw.line(screen, Gray, (k*gridWidth, 0),
            (k*gridWidth, gameRect.height))
      for k in range(Squares+1):
         pygame.draw.line(screen, Gray, (0, k*gridHeight),
            (gameRect.width, k*gridHeight))
  
      pygame.display.update()
      mainClock.tick(FPS)

#利用range()隨機產生圖片的分割
def startGame():
   board = [] #空的List存放切割後的圖塊
   #依切割後的圖塊數以append()方法加入board
   for k in range(gridNums):
      board.append(k)
   waitMoveSqr = gridNums - 1   #waitMoveSqr等待被移動的圖塊
   board[waitMoveSqr] = -1 #表示List存放一個元素為-1，讓其他圖片能移動

   #依據隨機值來決定圖片的移動方向並記錄移動圖塊和空白方格
   for k in range(100):
        direction = random.randint(0, 3)
        if (direction == 0):
            waitMoveSqr = moveLeft(board, waitMoveSqr)
        elif (direction == 1):
            waitMoveSqr = moveRight(board, waitMoveSqr)
        elif (direction == 2):
            waitMoveSqr = moveUp(board, waitMoveSqr)
        elif (direction == 3):
            waitMoveSqr = moveDown(board, waitMoveSqr)
   return board, waitMoveSqr

#依傳入圖塊和空白格，將位於空白格左側的圖塊，移入空白格
def moveRight(board, waitMoveSqr):
   #print('1-', board, waitMoveSqr)
   if waitMoveSqr % Squares == 0:
      return waitMoveSqr
   board[waitMoveSqr - 1], board[waitMoveSqr] = \
      board[waitMoveSqr], board[waitMoveSqr-1]
   return waitMoveSqr-1
  
#依傳入圖塊和空白格，將位於空白格右側的圖塊，移入空白格
def moveLeft(board, waitMoveSqr):
    if waitMoveSqr % Squares == Squares - 1:
        return waitMoveSqr
    board[waitMoveSqr+1], board[waitMoveSqr] = \
       board[waitMoveSqr], board[waitMoveSqr+1]
    return waitMoveSqr+1
  
#依傳入圖塊和空白格，將位於空白格上方的圖塊，移入空白格
def moveDown(board, waitMoveSqr):
    if waitMoveSqr < Squares:
        return waitMoveSqr
    board[waitMoveSqr-Squares], board[waitMoveSqr] = \
       board[waitMoveSqr], board[waitMoveSqr-Squares]
    return waitMoveSqr-Squares
      
#依傳入圖塊和空白格，將位於空白格下方的圖塊，移入空白格
def moveUp(board, waitMoveSqr):
    if waitMoveSqr >= gridNums-Squares:
        return waitMoveSqr
    board[waitMoveSqr+Squares], board[waitMoveSqr] = \
       board[waitMoveSqr], board[waitMoveSqr+Squares]
    return waitMoveSqr+Squares
  
#是否完成
def isFinished(board, waitMoveSqr):
    for item in range(gridNums - 1):
        if board[item] != item:
            return False
    return True

#結束應用程式
def finishGame():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
   main()#呼叫main()函式
