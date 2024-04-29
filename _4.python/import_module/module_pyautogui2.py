import pyautogui

import random
import time
import math

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
