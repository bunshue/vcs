import numpy as np
import cv2


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


def getGrayDiff(img, currentPoint, tmpPoint):
    return abs(
        int(img[currentPoint.x, currentPoint.y]) - int(img[tmpPoint.x, tmpPoint.y])
    )


def selectConnects(p):
    if p != 0:
        connects = [
            Point(-1, -1),
            Point(0, -1),
            Point(1, -1),
            Point(1, 0),
            Point(1, 1),
            Point(0, 1),
            Point(-1, 1),
            Point(-1, 0),
        ]
    else:
        connects = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]
    return connects


def regionGrow(img, seeds, thresh, p=1):
    height, weight = img.shape
    seedMark = np.zeros(img.shape)
    seedList = []
    for seed in seeds:
        seedList.append(seed)
    label = 1
    connects = selectConnects(p)
    while len(seedList) > 0:
        currentPoint = seedList.pop(0)

        seedMark[currentPoint.x, currentPoint.y] = label
        for i in range(8):
            tmpX = currentPoint.x + connects[i].x
            tmpY = currentPoint.y + connects[i].y
            if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= weight:
                continue
            grayDiff = getGrayDiff(img, currentPoint, Point(tmpX, tmpY))
            if grayDiff < thresh and seedMark[tmpX, tmpY] == 0:
                seedMark[tmpX, tmpY] = label
                seedList.append(Point(tmpX, tmpY))
    return seedMark


filename = "C:/_git/vcs/_1.data/______test_files1/ims03.bmp"

img = cv2.imread(filename, 0)
seeds = [Point(10, 10), Point(82, 150), Point(20, 300)]
binaryImg = regionGrow(img, seeds, 10)

cv2.imshow(" ", binaryImg)
cv2.waitKey(0)
