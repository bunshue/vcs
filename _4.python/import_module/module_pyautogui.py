"""

PyAutoGUI，自動控制滑鼠跟鍵盤



"""
import sys
import time
import math
import random

import pyautogui

print("------------------------------------------------------------")  # 60個

width, height = pyautogui.size()  # 取得螢幕寬度和高度
print(width, height)  # 列印螢幕寬度和高度

print("------------------------------------------------------------")  # 60個

width, hwight = pyautogui.size()
print(width, hwight)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("螢幕截圖 全螢幕 一張")

myScreenshot = pyautogui.screenshot()  # 截圖
myScreenshot.save("tmp_screenshot_full.png")  # 存圖

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("螢幕截圖 部分 一張")

(x1, y1, x2, y2) = (0, 0, 1920 // 2, 1080 // 2)

myScreenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
myScreenshot.save("tmp_screenshot_crop.png")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests

url = "https://notify-api.line.me/api/notify"
token = "你的權杖"
headers = {"Authorization": "Bearer " + token}  # 設定 LINE Notify 權杖
data = {"message": "測試一下！"}  # 設定 LINE Notify message ( 不可少 )
image = open("./test.png", "rb")  # 以二進位方式開啟圖片
imageFile = {"imageFile": image}  # 設定圖片資訊
data = requests.post(url, headers=headers, data=data, files=imageFile)  # 發送 LINE Notify

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests


# 定義截圖的函式
def screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("./test.png")

    t = time.time()  # 取得到目前為止的秒數
    t1 = time.localtime(t)  # 將秒數轉換為 struct_time 格式的時間
    now = time.strftime("%Y/%m/%d %H:%M:%S", t1)  # 輸出為特定格式的文字
    sendLineNotify(now)  # 執行發送 LINE Notify 的函式，發送的訊息為時間


# 定義發送 LINE Notify 的函式
def sendLineNotify(msg):
    url = "https://notify-api.line.me/api/notify"
    token = "你的權杖"
    headers = {"Authorization": "Bearer " + token}
    data = {"message": msg}
    image = open("./test.png", "rb")
    imageFile = {"imageFile": image}
    data = requests.post(url, headers=headers, data=data, files=imageFile)


# 使用for 迴圈，每隔五秒截圖發送一次
for i in range(5):
    screenshot()
    time.sleep(5)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

while True:
    x, y = pyautogui.position()
    # clear_output()
    print(x, y)
    time.sleep(0.5)
    if x < 10:
        print("太左邊  離開")
        break
    elif x > 1200:
        print("太右邊  離開")
        break
    elif y < 10:
        print("太上面  離開")
        break
    elif y > 900:
        print("太下面  離開")
        break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pyautogui.PAUSE = 1
x, y = 630, 20
print("移動")
pyautogui.moveTo(x, y, 2)
print("點擊")
pyautogui.click()
x, y = 264, 62
print("移動")
pyautogui.moveTo(x, y, 2)
print("點擊")
pyautogui.click()
print("打字")
pyautogui.typewrite("https://hophd.wordpress.com")
time.sleep(2)
print("Enter")
pyautogui.press("enter")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("按Ctrl-C 可以中斷本程式")
try:
    while True:
        xloc, yloc = pyautogui.position()  # 獲得滑鼠游標位置
        xylocStr = "x= " + str(xloc).rjust(4) + " y= " + str(yloc).rjust(4)
        print(xylocStr, end="\r", flush=True)  # 設定同一行最左邊輸出
        time.sleep(1)
except KeyboardInterrupt:
    print("\nBye")

print("------------------------------------------------------------")  # 60個

pyautogui.moveTo(500, 450)
pyautogui.click()

print("------------------------------------------------------------")  # 60個

pyautogui.click(500, 450)

print("------------------------------------------------------------")  # 60個

pyautogui.click(500, 450, button="right")

print("------------------------------------------------------------")  # 60個

pyautogui.mouseDown(button="right")  # 在滑鼠游標位置按住滑鼠右邊建
time.sleep(1)
pyautogui.mouseUp(800, 300, button="right")  # 放開後滑鼠游標在(800, 300)

print("------------------------------------------------------------")  # 60個

print("10秒後開始")
time.sleep(10)  # 這10秒需要繪圖視窗取得焦點,選擇畫筆和選擇顏色
pyautogui.click()  # 按一下設定繪圖起始點
displacement = 10
while displacement < 300:
    pyautogui.dragRel(displacement, 0, duration=0.2)
    pyautogui.dragRel(0, displacement, duration=0.2)
    pyautogui.dragRel(-displacement, 0, duration=0.2)
    pyautogui.dragRel(0, -displacement, duration=0.2)
    displacement += 10

print("------------------------------------------------------------")  # 60個

for i in range(1, 10):
    pyautogui.scroll(30)  # 往上捲動
    time.sleep(1)
    pyautogui.scroll(-30)  # 往下捲動
    time.sleep(1)

print("------------------------------------------------------------")  # 60個

screenImage = pyautogui.screenshot("out28_17_1.jpg")  # 方法1
screenImage.save("out28_17_2.jpg")  # 方法2

print("------------------------------------------------------------")  # 60個

screenImage = pyautogui.screenshot()
cropPict = screenImage.crop((960, 210, 1900, 480))
cropPict.save("out28_18.jpg")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

screenImage = pyautogui.screenshot()
x, y = 200, 200
print(screenImage.getpixel((x, y)))  # 取得該點之像素值

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

xloc, yloc = pyautogui.position()  # 獲得滑鼠游標位置
print(xloc, yloc)  # 列印滑鼠游標位置

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x, y = 200, 200
trueFalse = pyautogui.pixelMatchesColor(x, y, (255, 255, 255))
print(trueFalse)
trueFalse = pyautogui.pixelMatchesColor(x, y, (0, 0, 255))
print(trueFalse)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("請在 5 秒內開啟 Word 並設為焦點視窗")
time.sleep(5)
pyautogui.write("Ming-Chi Institute of Technology")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("請在 5 秒內開啟 Word 並設為焦點視窗")
time.sleep(5)
pyautogui.write("Ming-Chi Institute of Technology", interval=0.2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("請在 5 秒內開啟 Word 並設為焦點視窗")
time.sleep(5)
pyautogui.typewrite("Ming-Chi Institute of Technology", 0.2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("請在 5 秒內開啟 Word 並設為焦點視窗")
time.sleep(5)
pyautogui.typewrite(["M", "i", "n", "g"], 1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("請在 5 秒內開啟 記事本 並設為焦點視窗")
time.sleep(5)
pyautogui.typewrite(["M", "i", "m", "g", "left", "left", "del", "n"], 1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("請在 5 秒內開啟記事本並設為焦點視窗")
time.sleep(5)
pyautogui.typewrite(["M", "i", "n", "k", "enter"], 1)
pyautogui.typewrite(["M", "i", "n", "g", "up", "backspace", "g"], 1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("請在 5 秒內開啟記事本並設為焦點視窗")
time.sleep(5)
# 以下輸出*
pyautogui.keyDown("shift")
pyautogui.press("8")
pyautogui.keyUp("shift")
# 以下開啟檢視功能表
pyautogui.keyDown("alt")
pyautogui.press("V")
pyautogui.keyUp("alt")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("請在 5 秒內開啟記事本並設為焦點視窗")
time.sleep(5)
pyautogui.hotkey("shift", "8")  # 輸出 *
pyautogui.hotkey("alt", "V")  # 開啟檢視功能表

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("請在10秒內開啟記事本並設為焦點視窗")
time.sleep(10)

pyautogui.write("Taiwan\t", 0.3)  # Taiwan
pyautogui.write("Hung\t", 0.3)  # 姓
pyautogui.write("Jiin-Kwei\t", 0.3)  # 名
pyautogui.write("Jiin-Kwei\t", 0.3)  # 名
pyautogui.write("Hung\t", 0.3)  # 姓
pyautogui.write("1975\t", 0.3)  # 出生年
pyautogui.write("01\t", 0.3)  # 月
pyautogui.write("01\t", 0.3)  # 日
pyautogui.write("\t", 0.3)  # 選男生
pyautogui.write("Ming-Chi Inst. of Tech\t", 0.3)  # 學校
pyautogui.write("Department of ME", 0.3)  # 科系

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 給予一些時間來切換到瀏覽器視窗
time.sleep(5)

# 假設的表單填寫
# 移動到名字輸入框的位置並按一下, 需要根據實際位置調整座標
pyautogui.click(x=200, y=300)  # 這裡的 x 和 y 值需要您自己設定
pyautogui.write("John Doe", interval=0.1)

# 移動到郵件欄位輸入框的位置
pyautogui.click(x=200, y=350)  # 這裡的 x 和 y 值需要您自己設定
pyautogui.write("cshung@example.com", interval=0.1)

# 如果有更多欄位, 重複上述步驟

# 最後移動到提交按鈕並按一下
pyautogui.click(x=200, y=400)  # 這裡的 x 和 y 值需要您自己設定

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

xloc = 0
while xloc < 1000:
    xloc, yloc = pyautogui.position()  # 獲得滑鼠游標位置
    print(xloc, yloc)  # 列印滑鼠游標位置

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 截取屏幕的一部分
screenshot = pyautogui.screenshot(region=(0, 0, 300, 400))  # x, y, 寬度, 高度
screenshot.save("screenshot.png")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import subprocess

# 打開記事本（或其他應用）
subprocess.Popen("notepad.exe")
time.sleep(2)

# 輸入文本
pyautogui.write("AI實作 - 明志科技大學!", interval=0.1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("5秒後開始")
time.sleep(5)

# 選擇所有本字, 例如在一個文字編輯器中
pyautogui.hotkey("ctrl", "a")  # Ctrl + A

# 複製
pyautogui.hotkey("ctrl", "c")  # Ctrl + C

# 移動到另一個位置或應用
pyautogui.click(100, 100)  # 移動滑鼠游標並按一下

# 貼上
pyautogui.hotkey("ctrl", "v")  # Ctrl + V

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x, y = 300, 300
for i in range(5):
    pyautogui.moveTo(x, y, duration=0.5)  # 左上角
    pyautogui.moveTo(x + 1200, y, duration=0.5)  # 右上角
    pyautogui.moveTo(x + 1200, y + 400, duration=0.5)  # 右下角
    pyautogui.moveTo(x, y + 400, duration=0.5)  # 左下角

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

for i in range(5):
    pyautogui.moveRel(300, 0, duration=0.5)  # 往右上角移動
    pyautogui.moveRel(0, 300, duration=0.5)  # 往右下角移動
    pyautogui.moveRel(-300, 0, duration=0.5)  # 往左下角移動
    pyautogui.moveRel(0, -300, duration=0.5)  # 往左上角移動

print("------------------------------------------------------------")  # 60個

xloc = 0
print("按Ctrl-C 可以中斷本程式")
try:
    while xloc < 1000:
        xloc, yloc = pyautogui.position()  # 獲得滑鼠游標位置
        print(xloc, yloc)  # 列印滑鼠游標位置
except KeyboardInterrupt:
    print("\nBye")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("按Ctrl-C 可以中斷本程式")
try:
    while True:
        xloc, yloc = pyautogui.position()  # 獲得滑鼠游標位置
        print(xloc, yloc)  # 列印滑鼠游標位置
except KeyboardInterrupt:
    print("\nBye")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("10秒後開始")
time.sleep(10)  # 這10秒需要繪圖視窗取得焦點,選擇畫筆和選擇顏色
pyautogui.click()  # 按一下設定繪圖起始點
displacement = 300
while displacement > 10:
    pyautogui.dragRel(displacement, 0, duration=0.2)
    pyautogui.dragRel(0, displacement, duration=0.2)
    pyautogui.dragRel(-displacement, 0, duration=0.2)
    pyautogui.dragRel(0, -displacement, duration=0.2)
    displacement -= 10

print("------------------------------------------------------------")  # 60個

print("請在10秒內開啟記事本並設為焦點視窗")
time.sleep(10)

pyautogui.typewrite("Ming-Chi Institute of Technology", 0.1)
pyautogui.typewrite(["enter"], 0.1)
pyautogui.typewrite("Department of Artificial Intelligence", 0.1)
pyautogui.typewrite(["enter"], 0.1)
pyautogui.typewrite("Name : Jiin-Kwei Hung", 0.1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
from IPython.display import clear_output  # 用IPython

while True:
    x, y = pyautogui.position()
    clear_output()
    print(x, y)
    time.sleep(0.5)
    if x < 10:
        break
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pyautogui.PAUSE = 1
x, y = 630, 20
pyautogui.moveTo(x, y, 2)
pyautogui.click()
x, y = 264, 62
pyautogui.moveTo(x, y, 2)
pyautogui.click()
pyautogui.typewrite("https://hophd.wordpress.com")
time.sleep(2)
pyautogui.press("enter")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pyautogui.moveTo(x=400, y=100)
pyautogui.moveRel(xOffset=300, yOffset=200, duration=3, tween=pyautogui.linear)
pyautogui.moveRel(xOffset=-600, yOffset=0, duration=3, tween=pyautogui.easeInQuad)
pyautogui.moveRel(xOffset=300, yOffset=-200, duration=3, tween=pyautogui.easeOutQuad)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pyautogui.moveTo(x=400, y=100)
pyautogui.moveTo(x=700, y=300, duration=3, tween=pyautogui.linear)
pyautogui.moveTo(x=100, y=300, duration=3, tween=pyautogui.easeInQuad)
pyautogui.moveTo(x=400, y=100, duration=3, tween=pyautogui.easeOutQuad)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("10秒後開始")
print("請打開 https://canvas.apps.chrome/，並挑選你喜歡的畫筆顏色及粗細")
time.sleep(10)
pyautogui.moveTo(x=570, y=552)
pyautogui.dragTo(x=1152, y=354, duration=3, button="left")
pyautogui.dragTo(x=1114, y=795, duration=3, button="left")
pyautogui.dragTo(x=570, y=552, duration=3, button="left")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("10秒後開始")
print("請打開 https://canvas.apps.chrome/，並挑選你喜歡的畫筆顏色及粗細")
time.sleep(10)
pyautogui.moveTo(x=570, y=552)
pyautogui.dragRel(xOffset=582, yOffset=-198, duration=3, button="left")
pyautogui.dragRel(xOffset=-38, yOffset=441, duration=3, button="left")
pyautogui.dragRel(xOffset=-544, yOffset=-243, duration=3, button="left")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pyautogui.displayMousePosition()
time.sleep(0.5)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

while True:
    position = pyautogui.position()
    print(position)
    time.sleep(0.5)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("5秒後開始")
print("請開啟小算盤")
time.sleep(5)

num = "2021"
for n in num:
    box = pyautogui.locateOnScreen(n + ".png", grayscale=True)
    if box:
        x, y = pyautogui.center(box)
        pyautogui.leftClick(x, y)
    else:
        print("找不到圖片")

screen = pyautogui.screenshot()
screen.save("screenshot.png")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("10秒後開始")
print("以瀏覽器開啟 yahoo 網頁，並將視窗放到最大")
time.sleep(10)
pyautogui.scroll(-1000)
time.sleep(1)
pyautogui.scroll(300)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("10秒後開始")
pyautogui.PAUSE = 1
print("以記事本開啟新檔案，並將輸入線移到其中")
time.sleep(10)
pyautogui.typewrite(message="Welcome to PyAutoGUI!\n")
pyautogui.typewrite(message="Welcome to PyAutoGUI!", interval=0.3)
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
pyautogui.press("down")
pyautogui.hotkey("ctrl", "v")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("10秒後開始")
print("以記事本開啟新檔案，並將輸入線移到其中")
time.sleep(10)
pyautogui.press("g")
pyautogui.press("o", presses=2)
pyautogui.press("d")
pyautogui.press("enter")
time.sleep(1)
pyautogui.keyDown("shift")
pyautogui.press("g")
pyautogui.press("o", presses=2)
pyautogui.press("d")
pyautogui.keyUp("shift")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("2秒後開始")
time.sleep(2)
stime = time.time()
print("Game Start")
while time.time() - stime < 10:
    pyautogui.click(x=1030, y=419, button="left")
    # pyautogui.doubleClick(x=1030, y=419, button='left')
print("Game Over")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("3秒後, 以記事本開啟<selenium.txt>檔案，並將視窗放到最大")
print("視窗大小不合")

time.sleep(3)
pyautogui.click(x=20, y=31, button="left")  # 點選檔案功能表
pyautogui.leftClick(x=400, y=116, duration=2)  # 在空白處點擊滑鼠左鍵
pyautogui.click(x=600, y=130, duration=2, button="right")  # 按滑鼠右鍵
pyautogui.doubleClick(x=755, y=48, duration=2, button="left")  # 雙擊滑鼠左鍵

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x_st = 400
y_st = 400
width = 600
height = 600
sizePosition = (714, 84)
sizeOptions = (166, 211, 254, 297)
canvasOrigin = (x_st, y_st, x_st + width, y_st + height)
print(canvasOrigin)
moveX = 0
moveY = 0
swatchTopLeft = (0, 0)
swatchBottomRight = (0, 0)
swatchOffset = (0, 0)

colors = {
    "black": (1, 3),
    "blue": (1, 9),
    "red": (1, 4),
    "orange": (1, 5),
    "yellow": (1, 6),
    "green": (1, 7),
    "purple": (1, 9),
}

center = (width / 2 + canvasOrigin[0], height / 2 + canvasOrigin[1])
print(center)

pyautogui.moveTo(center)


def colorCoords(color):
    index = colors.get(color)
    x = swatchTopLeft[0] + (index[1] * swatchOffset[0])
    y = swatchTopLeft[1] + (index[0] * swatchOffset[1])
    return (x, y)


def pickSize():
    print("pickSize")
    size = random.choice(sizeOptions)
    print("sizePosition =", sizePosition)
    print("size =", size)

    """
    pyautogui.moveTo(sizePosition)
    pyautogui.click()
    pyautogui.moveTo(sizePosition[0], size)
    time.sleep(0.25)
    pyautogui.click()
    """


def waitLoop(length):
    print("Press Enter to Continue")
    # input()
    count = length
    while count > 0:
        print(str(count) + "...")
        time.sleep(1)
        count -= 1


def pickColor():
    print("pickColor")
    color = random.choice(list(colors.keys()))
    colorPosition = colorCoords(color)
    print(colorPosition)
    """
    pyautogui.moveTo(colorPosition)
    pyautogui.click()
    """


def getDestination():
    global moveX
    global moveY

    pos = pyautogui.position()
    startX = pos[0]
    startY = pos[1]
    strokeRand = random.randint(2, 30)

    moveX = random.randint(
        startX - int((width / strokeRand)), startX + int((width / strokeRand))
    )
    moveY = random.randint(
        startY - int((height / strokeRand)), startY + int((height / strokeRand))
    )
    if moveX > canvasOrigin[0] + width:
        return False
    elif moveX < canvasOrigin[0]:
        return False
    elif moveY > canvasOrigin[1] + height:
        return False
    elif moveY < canvasOrigin[1]:
        return False
    else:
        return True


def curve():
    startX = random.randint(canvasOrigin[0], canvasOrigin[2])
    startY = random.randint(canvasOrigin[1], canvasOrigin[3])
    endX = random.randint(canvasOrigin[0], canvasOrigin[2])
    endY = random.randint(canvasOrigin[1], canvasOrigin[3])

    pyautogui.moveTo(startX, startY)
    dist = abs(endX - startX)
    for j in range(dist):
        current = pyautogui.position()
        currX = current[0]
        currY = current[1]
        if endX > startX:
            newX = currX + 1
        if endX < startX:
            newX = currX - 1
        newY = center[1] + math.tan(newX)  # *(random.randint(2, height/2))
        pyautogui.dragTo(newX, newY)


def run(repeat):
    for x in range(repeat):
        if random.randint(0, 100) > 90:
            pickColor()
        if random.randint(0, 100) > 95:
            pickSize()
        # if random.randint(0,100) > 75:
        #    curve()
        # print(x)
        going = False
        startX = random.randint(0 + canvasOrigin[0], width + canvasOrigin[0])
        startY = random.randint(0 + canvasOrigin[1], height + canvasOrigin[1])
        pyautogui.moveTo(startX, startY)
        while not going:
            if getDestination():
                going = True
        # print('from ' +str(startX)+',' +str(startY)+' to '+str(moveX)+','+str(moveY))
        pyautogui.dragTo(moveX, moveY, button="left")
        going = False
        if x % 100 == 0:
            print(x)
    showMenu()


def rebuildCoords():
    global width
    global height
    global canvasOrigin
    global center
    global sizePosition
    global sizeOptions
    global swatchOffset
    global swatchBottomRight
    global swatchTopLeft

    print("Be sure you can see your print output during this process.")
    print("What is the width of the Canvas in pixels?")
    # pixW = input()
    width = 640
    print("What is the height of the Canvas in pixels?")
    # pixH = input()
    height = 480
    print("K, now to get screen coordinates of certain features in Paint.")
    print("press Enter")
    # input()
    print("How long do you need to get your cursor in place? (seconds)")
    # waitTime = int(input())
    waitTime = 1
    print("Move your cursor to the top left color swatch in Paint")
    waitLoop(waitTime)
    pos1 = pyautogui.position()
    print("Captured 1")
    print("Now move your cursor to the bottom right color swatch in Paint")
    waitLoop(waitTime)
    pos2 = pyautogui.position()
    swatchTopLeft = pos1
    swatchBottomRight = pos2
    print("Captured 2")
    offsetX = (pos2[0] - pos1[0]) / 10
    offsetY = (pos2[1] - pos1[1]) / 3
    swatchOffset = (offsetX, offsetY)
    print("Next, move your cursor to the Brush Size Button")
    print("Epstein Didn't Kill Himself")
    waitLoop(waitTime)
    brushPos = pyautogui.position()
    print("Captured 3")
    sizePosition = brushPos
    print("Move the cursor to the smallest brush size option")
    print("keep in mind you have to click for this one")
    waitLoop(waitTime)
    smallPos = pyautogui.position()
    print("Move the cursor to the largest brush size option")
    waitLoop(waitTime)
    bigPos = pyautogui.position()
    small = smallPos[1]
    big = bigPos[1]
    diff = (big - small) / 4
    sizeOptions = (small, small + diff, small + (diff * 2), big)
    print("Lastly, hold your cursor at the top left corner of the image canvas")
    print("Get it as close as possible")
    waitLoop(waitTime)
    origPos = pyautogui.position()
    canvasOrigin = (origPos[0], origPos[1], origPos[0] + width, origPos[1] + height)
    center = (width / 2 + canvasOrigin[0], height / 2 + canvasOrigin[1])


def getCoords(repeat):
    for x in range(repeat):
        print(pyautogui.position())
        time.sleep(1)


def showMenu():
    print("Type a Number and Press Enter:")
    print("1: Run")
    print("2: Get Cursor Coords")
    print(
        "3: Hol up let me do that stupid coordinate thing again because its confusing"
    )
    result = input()
    if result == "1":
        print("ctrl alt del if this goes crazy")
        print("How many strokes?")
        # ticks = input()
        ticks = 20
        run(int(ticks))
    if result == "2":
        print("For how long? (secs)")
        # secs = input()
        secs = 3
        getCoords(int(secs))
    if result == "3":
        rebuildCoords()


"""        
rebuildCoords()
showMenu()
"""


def my_test():
    print("my_test")

    repeat = 100

    for x in range(repeat):
        print(random.randint(0, 100), end=" ")
    print()

    repeat = 1

    for x in range(repeat):
        print(x)
        if random.randint(0, 100) > 90:
            print("xxxxx 1")
            pickColor()
        if random.randint(0, 100) > 95:
            print("xxxxx 2")
            pickSize()
        # if random.randint(0,100) > 75:
        #    curve()

        print("x =", x)

        going = False
        startX = random.randint(0 + canvasOrigin[0], width + canvasOrigin[0])
        startY = random.randint(0 + canvasOrigin[1], height + canvasOrigin[1])
        print("startX =", startX, ", startY =", startY)
        pyautogui.moveTo(startX, startY)
        while not going:
            if getDestination():
                print("xxxxx 5")
                going = True

        print("moveX =", moveX, ", moveY =", moveY)
        print(
            "from "
            + str(startX)
            + ","
            + str(startY)
            + " to "
            + str(moveX)
            + ","
            + str(moveY)
        )
        pyautogui.dragTo(moveX, moveY, button="left")
        going = False
        if x % 100 == 0:
            print(x)


# my_test()


def test_pickColor_pickSize():
    pickColor()
    pickSize()


test_pickColor_pickSize()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
