print("------------------------------------------------------------")  # 60個
print("PyAutoGUI，鍵盤滑鼠自動化, 自動控制滑鼠與鍵盤 ST")
print("------------------------------------------------------------")  # 60個

import sys
import time
import pyautogui


def sleep(second):
    for i in range(second):
        # print("等", i + 1, "秒")
        time.sleep(1)  # 等1秒


print(time.ctime())
print("------------------------------------------------------------")  # 60個

"""
# 移動滑鼠鼠標
x, y = 200, 200
pyautogui.moveTo(x, y, duration=2)  # 移動滑鼠位置
pyautogui.PAUSE = 1  # pyautogui等待

x, y = 500, 500
pyautogui.moveTo(x, y, duration=0.5)  # 左上角
pyautogui.PAUSE = 1  # pyautogui等待

x, y = 200, 200
pyautogui.moveTo(x, y, duration=3)  # 移動滑鼠位置
pyautogui.PAUSE = 1  # pyautogui等待
"""
print("基本 pyautogui 功能")

print("測試 pixelMatchesColor")

# 取得目前所有視窗程式的ID
screens = pyautogui.getAllWindows()
# print("screens :", screens)

x, y = 200, 200
trueFalse = pyautogui.pixelMatchesColor(x, y, (255, 255, 255))
print(trueFalse)

trueFalse = pyautogui.pixelMatchesColor(x, y, (0, 0, 255))
print(trueFalse)

width, height = pyautogui.size()  # 取得螢幕寬度和高度, 分辨率
print("螢幕寬度和高度 :", width, height)  # 列印螢幕寬度和高度

# 全螢幕截圖
screenImage = pyautogui.screenshot()  # 全螢幕截圖
screenImage.save("tmp_screen_full.png")  # 全螢幕存圖

# 部分截圖
cropPict = screenImage.crop((960, 210, 1900, 480))
cropPict.save("tmp_screen_part3.jpg")

x, y = 200, 200
print("取得像素值 :", screenImage.getpixel((x, y)))  # 取得該點之像素值

# 部分截圖
x_st, y_st, w, h = 1920 // 2, 1080 // 2, 1920 // 2, 1080 // 2
screenImage = pyautogui.screenshot(region=(x_st, y_st, w, h))  # x, y, 寬度, 高度
screenImage.save("tmp_screen_part1.png")  # 存圖

screenImage = pyautogui.screenshot("tmp_screen_part2a.jpg")  # 方法1
screenImage.save("tmp_screen_part2b.png")  # 存圖

print("------------------------------")  # 30個

# print("時時顯示滑鼠位置座標, 按 Ctrl+C 離開")
# pyautogui.displayMousePosition()

print("------------------------------")  # 30個

print("獲得滑鼠游標位置")

for i in range(5):
    x, y = pyautogui.position()  # 獲得滑鼠游標位置
    print(x, y)  # 列印滑鼠游標位置
    xylocStr = "x= " + str(x).rjust(4) + " y= " + str(y).rjust(4)
    print(xylocStr, end="\r", flush=True)  # 設定同一行最左邊輸出

    position = pyautogui.position()  # 獲得滑鼠游標位置
    print(position)

    sleep(1)  # 等N秒

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import subprocess

subprocess.Popen("data/vcs_test_pyautogui.exe")  # 打開應用程式

sleep(5)  # 等N秒

print("------------------------------------------------------------")  # 60個

# 滑鼠走到 richTextBox1 位置點一下
pyautogui.click(x=500, y=120, button="left")

for i in range(10):
    # 滑鼠滾輪往下捲動
    pyautogui.scroll(-300)  # 往下捲動(負數)
    sleep(1)  # 等N秒

for i in range(10):
    # 滑鼠滾輪往上捲動
    pyautogui.scroll(300)  # 往上捲動(正數)
    sleep(1)  # 等N秒

print("------------------------------")  # 30個

# 滑鼠走到 richTextBox1 位置點一下
pyautogui.click(x=500, y=120, button="left")

# 只能寫英數, 不能寫中文
pyautogui.write("ABCDEFG", interval=0.1)
pyautogui.write("ABCDEFG")
pyautogui.write("Column1", 0.3)

pyautogui.typewrite("https://www.google.com")  # 打字, 只能英數, 看起來只適合在網址列輸入資料

pyautogui.typewrite(["enter"], 0.1)  # 打字, 換行

pyautogui.typewrite("AAAA", 0.1)  # 打字
pyautogui.typewrite(["enter"], 0.1)  # 打字, 換行

pyautogui.typewrite(["M", "i", "n", "g"], 0.5)  # 打字

pyautogui.typewrite(["enter"], 0.1)  # 打字, 換行

pyautogui.typewrite(["M", "i", "m", "g", "left", "left", "del", "n"], 0.5)  # 打字

pyautogui.typewrite(["enter"], 0.1)  # 打字, 換行

pyautogui.typewrite(["M", "i", "n", "k", "enter"], 0.5)  # 打字

pyautogui.typewrite(["M", "i", "n", "g", "up", "backspace", "g"], 0.5)  # 打字

pyautogui.typewrite(["enter"], 0.1)  # 打字, 換行

print("------------------------------")  # 30個

pyautogui.click(x=200, y=200, button="left")

# pyautogui.hotkey()

# Ctrl + A 全選
pyautogui.hotkey("ctrl", "a")  # Ctrl + A

sleep(1)  # 等N秒

# Ctrl + C 複製
pyautogui.hotkey("ctrl", "c")  # Ctrl + C

sleep(1)  # 等N秒

# 移動到另一個位置或應用
pyautogui.click(500, 400)  # 移動滑鼠游標並按一下

sleep(1)  # 等N秒

# Ctrl + V 貼上
pyautogui.hotkey("ctrl", "v")  # Ctrl + V

print("------------------------------")  # 30個

# 按 Shift + 8 = *
pyautogui.hotkey("shift", "8")  # 輸出星號 *

# pyautogui.hotkey("alt", "V")  # Alt + V : 開啟檢視功能表

# 按 Shift + 7 = &
pyautogui.keyDown("shift")
pyautogui.press("7")
pyautogui.keyUp("shift")

# 以下開啟檢視功能表 # Alt + V : 開啟檢視功能表
# pyautogui.keyDown("alt")
pyautogui.press("V")
# pyautogui.keyUp("alt")

# pyautogui.keyDown("down")
# pyautogui.keyUp("down")
# pyautogui.keyDown("up")

pyautogui.keyDown("shift")  # 按下 SHIFT
pyautogui.press("g")
pyautogui.press("o", presses=10)  # 按一個字鍵 O, 按10次
pyautogui.press("d")
pyautogui.keyUp("shift")  # 放開 SHIFT

print("------------------------------")  # 30個

# 滑鼠點幾個點
for i in range(10):
    pyautogui.moveTo(60 + 35 * i, 65)  # 移動滑鼠位置
    pyautogui.click()  # 滑鼠點擊

# 滑鼠拖曳到絕對座標 + 左鍵, duration時間完成
pyautogui.moveTo(x=100, y=100)  # 移動滑鼠位置  # 先移動到定點
pyautogui.dragTo(x=150, y=200, duration=3, button="left")  # 滑鼠左鍵拖曳, 3秒完成
pyautogui.dragTo(x=50, y=200, duration=3, button="left")  # 滑鼠左鍵拖曳, 3秒完成
pyautogui.dragTo(x=100, y=100, duration=3, button="left")  # 滑鼠左鍵拖曳, 3秒完成

# 滑鼠移動到相對座標 + 左鍵, duration時間完成
pyautogui.moveTo(200, 100)  # 移動滑鼠位置
pyautogui.moveRel(-50, 100, duration=0.5)  # 往右下
pyautogui.moveRel(50, -100, duration=0.5)  # 往右上
pyautogui.moveRel(50, 100, duration=0.5)  # 往右下
pyautogui.moveRel(-84, -35, duration=0.5)  # 往左上
pyautogui.moveRel(66, 0, duration=0.5)  # 往右

# 拖曳到相對座標 + 左鍵, duration時間完成
pyautogui.moveTo(200, 100)  # 移動滑鼠位置
pyautogui.dragRel(xOffset=-50, yOffset=100, duration=1, button="left")  # 往左下
pyautogui.moveRel(50, -100, duration=0.5)  # 往右上
pyautogui.dragRel(xOffset=50, yOffset=100, duration=1, button="left")  # 往右下
pyautogui.moveRel(-84, -35, duration=0.5)  # 往左上
pyautogui.dragRel(xOffset=66, yOffset=0, duration=1, button="left")  # 往右

print("moveRel() 加參數")
# pyautogui.moveRel(xOffset=200, yOffset=100, duration=3, tween=pyautogui.linear)
# pyautogui.moveRel(xOffset=-200, yOffset=0, duration=3, tween=pyautogui.easeInQuad)
# pyautogui.moveRel(xOffset=200, yOffset=-100, duration=3, tween=pyautogui.easeOutQuad)

print("moveTo() 加參數 移動滑鼠位置")
# pyautogui.moveTo(x=300, y=200)  # 移動滑鼠位置
# pyautogui.moveTo(x=400, y=400, duration=3, tween=pyautogui.linear)
# pyautogui.moveTo(x=100, y=400, duration=3, tween=pyautogui.easeInQuad)
# pyautogui.moveTo(x=300, y=200, duration=3, tween=pyautogui.easeOutQuad)

print("------------------------------")  # 30個

pyautogui.PAUSE = 1

pyautogui.moveTo(500, 100)  # 移動滑鼠位置
pyautogui.click()  # 滑鼠點擊

print("輸入字串, 只能輸入英數")
pyautogui.typewrite(message="Welcome to the United States 1\n")  # 打字
pyautogui.typewrite(
    message="Welcome to the United States 2\n", interval=0.1
)  # 打字, 加每字間隔

print("鍵盤按鍵")  # pyautogui.press() 是按鍵盤的一個鍵

pyautogui.press("enter")  # 按Enter

pyautogui.press("down")  # 按方向鍵 下
pyautogui.press("A")  # 按一個字鍵 D
pyautogui.press("down")  # 按方向鍵 下
pyautogui.press("b")  # 按一個字鍵 D
pyautogui.press("down")  # 按方向鍵 下
pyautogui.press("C")  # 按一個字鍵 D
pyautogui.press("down")  # 按方向鍵 下
pyautogui.press("d")  # 按一個字鍵 D

pyautogui.press("enter")  # 按Enter

pyautogui.press("g")  # 按一個字鍵 G
pyautogui.press("o", presses=10)  # 按一個字鍵 O, 按10次
pyautogui.press("d")  # 按一個字鍵 D

pyautogui.press("enter")  # 按Enter

print("------------------------------")  # 30個

# 滑鼠走到 richTextBox1 位置點一下
pyautogui.click(x=500, y=120, button="left")

# 各種滑鼠按鍵
pyautogui.click(500, 250)  # 滑鼠點擊某一點
pyautogui.click(500, 250, button="right")

sleep(1)  # 等N秒

pyautogui.click(500, 250)  # 滑鼠點擊某一點
pyautogui.mouseDown(button="right")  # 在滑鼠游標位置按住滑鼠右邊建

sleep(1)  # 等N秒

pyautogui.mouseUp(600, 200, button="right")  # 放開後滑鼠游標在(800, 300)

print("------------------------------")  # 30個

# 各種滑鼠按鍵方法
print("滑鼠單擊 左鍵")
# 滑鼠走到 richTextBox1 位置點一下
pyautogui.click(x=500, y=120, button="left")
print("滑鼠雙擊")
pyautogui.doubleClick(x=500, y=120, button="left")
pyautogui.doubleClick(x=500, y=120, duration=2, button="left")  # 雙擊滑鼠左鍵

print("滑鼠單擊 左鍵")
pyautogui.leftClick(x=500, y=250, duration=2)  # 在空白處點擊滑鼠左鍵

print("------------------------------")  # 30個

print("操作滑鼠右鍵選單")

print("選右鍵選單 全選")
# 滑鼠走到 richTextBox1 位置點一下
pyautogui.click(x=500, y=120, button="left")

# 按右鍵, 出現右鍵選單
pyautogui.click(x=500, y=130, duration=2, button="right")  # 按滑鼠右鍵

pyautogui.moveTo(x=550, y=260)  # 移動滑鼠位置
sleep(2)
# 點選右鍵選單的內容, 全選
pyautogui.click(x=550, y=260, duration=2, button="left")  # 按滑鼠右鍵

sleep(2)

print("選右鍵選單 複製")
# 按右鍵, 出現右鍵選單, 當時位置
pyautogui.click(button="right")

pyautogui.moveRel(50, 80, duration=0.5)  # 往右下角移動
sleep(2)
pyautogui.click()  # 按滑鼠右鍵, 進行複製

sleep(2)

pyautogui.moveTo(x=550, y=300)  # 移動滑鼠位置

print("選右鍵選單 貼上")
pyautogui.click()
# 按右鍵, 出現右鍵選單
pyautogui.click(button="right")  # 按滑鼠右鍵

pyautogui.moveRel(50, 100, duration=0.5)  # 往右下角移動
sleep(1)
# 點選右鍵選單的內容, 貼上
pyautogui.click()  # 按滑鼠右鍵, 進行貼上

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
print("NG locateOnScreen 請開啟小算盤 5秒後開始")

sleep(5)  # 等N秒

num = "2021"
for n in num:
    box = pyautogui.locateOnScreen(n + ".png", grayscale=True)
    if box:
        x, y = pyautogui.center(box)
        pyautogui.leftClick(x, y)
    else:
        print("找不到圖片")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("PyAutoGUI，鍵盤滑鼠自動化, 自動控制滑鼠與鍵盤 SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

# 6060
print("------------------------------------------------------------")  # 60個
# 3030
print("------------------------------")  # 30個
# 1515
print("---------------")  # 15個


"""
# pyautogui.dragTo() 用來按住滑鼠左鍵並將游標拖曳到指定的螢幕座標位置
pyautogui.dragTo(x, y, duration=0..5, button="left", tween=pyautogui.easeInOutQuad)
• x, y：要拖曳到的目標螢幕座標（X, Y 軸像素位置）。
• duration：拖曳過程所花費的時間（以秒為單位，預設為 0 即瞬間完成）。
• button：按住哪一個滑鼠按鍵，預設為左鍵 ('left')，也可以設為 'middle'（中鍵）或 'right'（右鍵）。
• tween：移動時的速度曲線函數（例如慢慢加速、減速等效果）。

與 dragRel() 的差別：
• dragTo(x, y) 是移動到絕對座標。
• dragRel(xOffset, yOffset) 則是相對於目前游標所在位置來進行位移。

"""


# locateOnScreen() 匹配的基准空间

# L3	图像匹配坐标	pyautogui.locateOnScreen('btn.png') 返回值

# NG cc = pyautogui.locateOnScreen('D:/_git/vcs/_4.python/web_crawler/ggg.png')
# print(cc)


# 截圖找圖
matches = list(pyautogui.locateAllOnScreen("ggg.jpg", confidence=0.9, grayscale=True))
length = len(matches)
print("len = ", length)

for mm in matches:
    print(mm)
    print(mm.index, mm.left, mm.top, mm.width, mm.height)

# print(f"找到{len(matches)}个匹配点，置信度均值：{np.mean([m.confidence for m in matches]):.3f}")
# 若均值0.82但标准差0.15，说明环境噪声大，需降confidence


pyautogui.doubleClick()
