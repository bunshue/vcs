"""

圖像邊緣檢測


"""

import cv2
import numpy as np

ESC = 27
SPACE = 32

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

print("------------------------------------------------------------")  # 60個

# 1、Robers算法

import numpy as np
import cv2
from scipy import signal


def roberts(I, _boundary="fill", _fillvalue=0):
    H1, W1 = I.shape[0:2]
    H2, W2 = 2, 2
    R1 = np.array([[1, 0], [0, -1]], np.float32)
    kr1, kc1 = 0, 0
    IconR1 = signal.convolve2d(
        I, R1, mode="full", boundary=_boundary, fillvalue=_fillvalue
    )
    IconR1 = IconR1[H2 - kr1 - 1 : H1 + H2 - kr1 - 1, W2 - kc1 - 1 : W1 + W2 - kc1 - 1]
    R2 = np.array([[0, 1], [-1, 0]], np.float32)
    IconR2 = signal.convolve2d(
        I, R2, mode="full", boundary=_boundary, fillvalue=_fillvalue
    )
    kr2, kc2 = 0, 1
    IconR2 = IconR2[H2 - kr2 - 1 : H1 + H2 - kr2 - 1, W2 - kc2 - 1 : W1 + W2 - kc2 - 1]
    return (IconR1, IconR2)


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)
IconR1, IconR2 = roberts(image, "symm")
IconR1 = np.abs(IconR1)
edge_45 = IconR1.astype(np.uint8)
cv2.imshow("edge_45", edge_45)
IconR2 = np.abs(IconR2)
edge_135 = IconR2.astype(np.uint8)
cv2.imshow("edge_135", edge_135)
edge = np.sqrt(np.power(IconR1, 2.0) + np.power(IconR2, 2.0))
edge = np.round(edge)
edge[edge > 255] = 255
edge = edge.astype(np.uint8)
cv2.imshow("edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 2、Prewitt算法

import numpy as np
import cv2
from scipy import signal


def prewitt(
    I,
    _boundary="symm",
):
    ones_y = np.array([[1], [1], [1]], np.float32)
    i_conv_pre_x = signal.convolve2d(I, ones_y, mode="same", boundary=_boundary)
    diff_x = np.array([[1, 0, -1]], np.float32)
    i_conv_pre_x = signal.convolve2d(
        i_conv_pre_x, diff_x, mode="same", boundary=_boundary
    )
    ones_x = np.array([[1, 1, 1]], np.float32)
    i_conv_pre_y = signal.convolve2d(I, ones_x, mode="same", boundary=_boundary)
    diff_y = np.array([[1], [0], [-1]], np.float32)
    i_conv_pre_y = signal.convolve2d(
        i_conv_pre_y, diff_y, mode="same", boundary=_boundary
    )
    return (i_conv_pre_x, i_conv_pre_y)


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
i_conv_pre_x, i_conv_pre_y = prewitt(image)
abs_i_conv_pre_x = np.abs(i_conv_pre_x)
abs_i_conv_pre_y = np.abs(i_conv_pre_y)
edge_x = abs_i_conv_pre_x.copy()
edge_y = abs_i_conv_pre_y.copy()
edge_x[edge_x > 255] = 255
edge_y[edge_y > 255] = 255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)
cv2.imshow("edge_x", edge_x)
cv2.imshow("edge_y", edge_y)
edge = 0.5 * abs_i_conv_pre_x + 0.5 * abs_i_conv_pre_y
edge[edge > 255] = 255
edge = edge.astype(np.uint8)
cv2.imshow("edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 3、Sobel算法
import cv2
import numpy as np
from scipy import signal
import math


def pascalSmooth(n):
    pascalSmooth = np.zeros([1, n], np.float32)
    for i in range(n):
        pascalSmooth[0][i] = math.factorial(n - 1) / (
            math.factorial(i) * math.factorial(n - 1 - i)
        )
        return pascalSmooth


def pascalDiff(n):
    pascalDiff = np.zeros([1, n], np.float32)
    pascalSmooth_previous = pascalSmooth(n - 1)
    for i in range(n):
        if i == 0:
            pascalDiff[0][i] = pascalSmooth_previous[0][i]
        elif i == n - 1:
            pascalDiff[0][i] = -pascalSmooth_previous[0][i - 1]
        else:
            pascalDiff[0][i] = (
                pascalSmooth_previous[0][i] - pascalSmooth_previous[0][i - 1]
            )
    return pascalDiff


def sobel(image, n):
    rows, cols = image.shape
    pascalSmoothKernel = pascalSmooth(n)
    pascalDiffKernel = pascalDiff(n)
    image_sobel_x = signal.convolve2d(
        image, pascalSmoothKernel.transpose(), mode="same"
    )
    image_sobel_x = signal.convolve2d(image_sobel_x, pascalDiffKernel, mode="same")
    image_sobel_y = signal.convolve2d(image, pascalSmoothKernel, mode="same")
    image_sobel_y = signal.convolve2d(
        image_sobel_y, pascalDiffKernel.transpose(), mode="same"
    )
    return (image_sobel_x, image_sobel_y)


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
image_sobel_x, image_sobel_y = sobel(image, 7)
edge = np.sqrt(np.power(image_sobel_x, 2.0) + np.power(image_sobel_y, 2.0))
edge = edge / np.max(edge)
edge = np.power(edge, 1)
edge *= 255
edge = edge.astype(np.uint8)
cv2.imshow("image", image)
cv2.imshow("edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
# 4、Scharr算法

import cv2
import numpy as np
from scipy import signal
import math


def scharr(I, _boundary="symm"):
    # I 與 scharr_x 的 same 卷積
    scharr_x = np.array([[3, 0, -3], [10, 0, -10], [3, 0, -3]], np.float32)
    I_x = signal.convolve2d(I, scharr_x, mode="same", boundary="symm")
    # I 與 scharr_y 的same 卷積
    scharr_y = np.array([[3, 10, 3], [0, 0, 0], [-3, -10, -3]], np.float32)
    I_y = signal.convolve2d(I, scharr_y, mode="same", boundary="symm")
    return (I_x, I_y)


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

i_conv_pre_x, i_conv_pre_y = scharr(image)

abs_i_conv_pre_x = np.abs(i_conv_pre_x)
abs_i_conv_pre_y = np.abs(i_conv_pre_y)
edge_x = abs_i_conv_pre_x.copy()
edge_y = abs_i_conv_pre_y.copy()
edge_x[edge_x > 255] = 255
edge_y[edge_y > 255] = 255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)
cv2.imshow("edge_x", edge_x)
cv2.imshow("edge_y", edge_y)
edge = 0.5 * abs_i_conv_pre_x + 0.5 * abs_i_conv_pre_y
edge[edge > 255] = 255
edge = edge.astype(np.uint8)
cv2.imshow("edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 5、Kirsch算法

import cv2
import numpy as np
from scipy import signal
import math


def kirsch(image, _boundary="fill", _fillvalue=0):
    list_edge = []
    k1 = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]])
    image_k1 = signal.convolve2d(
        image, k1, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k1))
    k2 = np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]])
    image_k2 = signal.convolve2d(
        image, k2, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k2))
    k3 = np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]])
    image_k3 = signal.convolve2d(
        image, k3, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k3))
    k4 = np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]])
    image_k4 = signal.convolve2d(
        image, k4, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k4))
    k5 = np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]])
    image_k5 = signal.convolve2d(
        image, k5, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k5))
    k6 = np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]])
    image_k6 = signal.convolve2d(
        image, k6, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k6))
    k7 = np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])
    image_k7 = signal.convolve2d(
        image, k7, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k7))
    k8 = np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]])
    image_k8 = signal.convolve2d(
        image, k8, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    list_edge.append(np.abs(image_k8))
    edge = list_edge[0]
    for i in range(len(list_edge)):
        edge = edge * (edge >= list_edge[i]) + list_edge[i] * (edge < list_edge[i])
    return edge


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
edge = kirsch(image, _boundary="symm")
edge[edge > 255] = 255
edge = edge.astype(np.uint8)
cv2.imshow("edge", edge)
pencilSketch = 255 - edge
cv2.imshow("pencilSketch", pencilSketch)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
# 6、Canny算法
import cv2
import numpy as np
from scipy import signal
import math


def non_maximum_suppression_default(dx, dy):
    edgeMag = np.sqrt(np.power(dx, 2.0) + np.power(dy, 2.0))
    rows, cols = dx.shape
    gradientDirection = np.zeros(dx.shape)
    edgeMag_nonMaxSup = np.zeros(dx.shape)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            angle = math.atan2(dy[r][c], dx[r][c]) / math.pi * 180
            gradientDirection[r][c] = angle
            if abs(angle) < 22.5 or abs(angle) > 157.5:
                if (
                    edgeMag[r][c] > edgeMag[r][c - 1]
                    and edgeMag[r][c] > edgeMag[r][c + 1]
                ):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            if (angle >= 22.5 and angle < 67.5) or (-angle > 112.5 and -angle <= 157.5):
                if (
                    edgeMag[r][c] > edgeMag[r - 1][c - 1]
                    and edgeMag[r][c] > edgeMag[r + 1][c + 1]
                ):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            if abs(angle) >= 67.5 and abs(angle) <= 112.5:
                if (
                    edgeMag[r][c] > edgeMag[r - 1][c]
                    and edgeMag[r][c] > edgeMag[r + 1][c]
                ):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            if (angle >= 112.5 and angle <= 157.5) or (
                -angle >= 22.5 and -angle < 67.5
            ):
                if (
                    edgeMag[r][c] > edgeMag[r - 1][c + 1]
                    and edgeMag[r][c] > edgeMag[r + 1][c - 1]
                ):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
    return edgeMag_nonMaxSup


def nom_maximum_suppression_Inter(dx, dy):
    edgeMag = np.sqrt(np.power(dx, 2.0) + np.power(dy, 2.0))
    rows, cols = dx.shape
    gradientDirection = np.zeros(dx.shape)
    edgeMag_nonMaxSup = np.zeros(dx.shape)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if dy[r][c] == 0 and dx[r][c] == 0:
                continue
            angle = math.atan2(dy[r][c], dx[r][c]) / math.pi * 180
            gradientDirection[r][c] = angle
            if (angle > 45 and angle <= 90) or (angle > -135 and angle <= -90):
                ratio = dx[r][c] / dy[r][c]
                leftTop_top = (
                    ratio * edgeMag[r - 1][c - 1] + (1 - ratio) * edgeMag[r - 1][c]
                )
                rightBottom_bottom = (1 - ratio) * edgeMag[r + 1][c] + ratio * edgeMag[
                    r + 1
                ][c + 1]
                if edgeMag[r][c] > leftTop_top and edgeMag[r][c] > rightBottom_bottom:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            if (angle > 90 and angle <= 135) or (angle > -90 and angle <= -45):
                ratio = abs(dx[r][c] / dy[r][c])
                rightTop_top = (
                    ratio * edgeMag[r - 1][c + 1] + (1 - ratio) * edgeMag[r - 1][c]
                )
                leftBottom_bottom = (
                    ratio * edgeMag[r + 1][c - 1] + (1 - ratio) * edgeMag[r + 1][c]
                )
                if edgeMag[r][c] > rightTop_top and edgeMag[r][c] > leftBottom_bottom:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            if (angle >= 0 and angle <= 45) or (angle > -180 and angle <= -135):
                ratio = dy[r][c] / dx[r][c]
                rightBottom_right = (
                    ratio * edgeMag[r + 1][c + 1] + (1 - ratio) * edgeMag[r][c + 1]
                )
                leftTop_left = (
                    ratio * edgeMag[r - 1][c - 1] + (1 - ratio) * edgeMag[r][c - 1]
                )
                if edgeMag[r][c] > rightBottom_right and edgeMag[r][c] > leftTop_left:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            if (angle > 135 and angle <= 180) or (angle > -45 and angle <= 0):
                ratio = abs(dy[r][c] / dx[r][c])
                rightTop_right = (
                    ratio * edgeMag[r - 1][c + 1] + (1 - ratio) * edgeMag[r][c + 1]
                )
                leftBottom_left = (
                    ratio * edgeMag[r + 1][c - 1] + (1 - ratio) * edgeMag[r][c - 1]
                )
                if edgeMag[r][c] > rightTop_right and edgeMag[r][c] > leftBottom_left:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
    return edgeMag_nonMaxSup


def checkInRange(r, c, rows, cols):
    if r > 0 and r < rows and c >= 0 and c < cols:
        return True
    else:
        return False


def trace(edgeMag_nonMaxSup, edge, lowerThresh, r, c, rows, cols):
    if edge[r][c] == 0:
        edge[r][c] = 255
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    checkInRange(r + i, c + j, rows, cols)
                    and edgeMag_nonMaxSup[r + i][c + j] >= lowerThresh
                ):
                    trace(
                        edgeMag_nonMaxSup, edge, lowerThresh, r + i, c + j, rows, cols
                    )


def hysteresisThreshold(edge_nonMaxSup, lowerThresh, upperThresh):
    rows, cols = edge_nonMaxSup.shape
    edge = np.zeros(edge_nonMaxSup.shape, np.uint8)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if edge_nonMaxSup[r][c] >= upperThresh:
                trace(edge_nonMaxSup, edge, lowerThresh, r, c, rows, cols)
            if edge_nonMaxSup[r][c] < lowerThresh:
                edge[r][c] = 0
    return edge


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
image_sobel_x, image_sobel_y = sobel(image, 3)
edge = np.sqrt(np.power(image_sobel_x, 2.0) + np.power(image_sobel_y, 2.0))
edge[edge > 255] = 255
edge = edge.astype(np.uint8)
edgeMag_nonMaxSup = non_maximum_suppression_default(image_sobel_x, image_sobel_y)
edgeMag_nonMaxSup[edgeMag_nonMaxSup > 255] = 255
edgeMag_nonMaxSup = edgeMag_nonMaxSup.astype(np.uint8)
cv2.imshow("edgeMag_nonMaxSup", edgeMag_nonMaxSup)
edge = hysteresisThreshold(edgeMag_nonMaxSup, 60, 180)
lowerThresh = 40
upperThresh = 150
cv2.imshow("canny", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# 7、Laplacian算法
import cv2
import numpy as np
from scipy import signal
import math


def laplacian(image, _boundary="fill", _fillvalue=0):
    laplacianKernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], np.float32)
    i_conv_lap = signal.convolve2d(
        image, laplacianKernel, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    return i_conv_lap


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)
i_conv_lap = laplacian(image, "symm")
threshEdge = np.copy(i_conv_lap)
threshEdge[threshEdge > 0] = 255
threshEdge[threshEdge <= 0] = 0
threshEdge = threshEdge.astype(np.uint8)
cv2.imshow("threshEdge", threshEdge)
abstraction = np.copy(i_conv_lap)
abstraction = abstraction.astype(np.float32)
abstraction[abstraction >= 0] = 1.0
abstraction[abstraction < 0] = 1.0 + np.tanh(abstraction[abstraction < 0])
cv2.imshow("abstraction", abstraction)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 8、LoG算法
import cv2
import numpy as np
from scipy import signal
import math


def createLoGKernel(sigma, size):
    H, W = size
    r, c = np.mgrid[0:H:1, 0:W:1]
    r -= (H - 1) // 2
    c -= (W - 1) // 2
    sigma2 = pow(sigma, 2.0)
    norm2 = np.power(r, 2.0) + np.power(c, 2.0)
    LoGKernel = (norm2 / sigma2 - 2) * np.exp(-norm2 / (2 * sigma2))
    return LoGKernel


def LoG(image, sigma, size, _boundary="symm"):
    loGKernel = createLoGKernel(sigma, size)
    img_conv_log = signal.convolve2d(image, loGKernel, "same", boundary=_boundary)
    return img_conv_log


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)
img_conv_log = LoG(image, 6, (37, 37), "symm")
edge_binary = np.copy(img_conv_log)
edge_binary[edge_binary > 0] = 255
edge_binary[edge_binary <= 0] = 0
edge_binary = edge_binary.astype(np.uint8)
cv2.imshow("edge_binary", edge_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 9、DoG算法 一
import cv2
import numpy as np
from scipy import signal
import math


def gaussConv(I, size, sigma):
    H, W = size
    xr, xc = np.mgrid[0:1, 0:W]
    xc -= (W - 1) // 2
    xk = np.exp(-np.power(xc, 2.0))
    I_xk = signal.convolve2d(I, xk, "same", "symm")
    yr, yc = np.mgrid[0:H, 0:1]
    yr -= (H - 1) // 2
    yk = np.exp(-np.power(yr, 2.0))
    I_xk_yk = signal.convolve2d(I_xk, yk, "same", "symm")
    I_xk_yk *= 1.0 / (2 * np.pi * pow(sigma, 2.0))
    return I_xk_yk


def DoG(I, size, sigma, k=1.1):
    Is = gaussConv(I, size, sigma)
    Isk = gaussConv(I, size, k * sigma)
    doG = Isk - Is
    doG /= pow(sigma, 2.0) * (k - 1)
    return doG


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)
sigma = 2
k = 1.1
size = (13, 13)
imageDoG = DoG(image, size, sigma, k)
edge = np.copy(imageDoG)
edge[edge > 0] = 255
edge[edge <= 0] = 0
edge = edge.astype(np.uint8)
cv2.imshow("edge", edge)
abstraction = -np.copy(imageDoG)
abstraction = abstraction.astype(np.float32)
abstraction[abstraction >= 0] = 1.0
abstraction[abstraction < 0] = 1.0 + np.tanh(abstraction[abstraction < 0])
cv2.imshow("abstraction", abstraction)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 9、DoG算法 二

import cv2
import numpy as np
from scipy import signal
import math


def gaussConv(I, size, sigma):
    H, W = size
    r, c = np.mgrid[0:H:1, 0:W:1]
    r -= (H - 1) // 2
    c -= (W - 1) // 2
    sigma2 = pow(sigma, 2.0)
    norm2 = np.power(r, 2.0) + np.power(c, 2.0)
    xyk = (norm2 / sigma2 - 2) * np.exp(-norm2 / (2 * sigma2))
    I_xk_yk = signal.convolve2d(I, xyk, "same", "symm")
    return I_xk_yk


def DoG(I, size, sigma, k=1.1):
    Is = gaussConv(I, size, sigma)
    Isk = gaussConv(I, size, k * sigma)
    doG = Isk - Is
    doG /= pow(sigma, 2.0) * (k - 1)
    return doG


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)
sigma = 4
k = 1.1
size = (25, 25)
imageDoG = DoG(image, size, sigma, k)
edge = np.copy(imageDoG)
edge[edge > 0] = 255
edge[edge <= 0] = 0
edge = np.round(edge)
edge = edge.astype(np.uint8)
cv2.imshow("edge", edge)
abstraction = -np.copy(imageDoG)
abstraction = abstraction.astype(np.float32)
abstraction[abstraction >= 0] = 1.0
abstraction[abstraction < 0] = 1.0 + np.tanh(abstraction[abstraction < 0])
cv2.imshow("abstraction", abstraction)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
# 10、Marr-Hildreth算法

import cv2
import numpy as np
from scipy import signal
import math


def gaussConv(I, size, sigma):
    H, W = size
    xr, xc = np.mgrid[0:1, 0:W]
    xc -= (W - 1) // 2
    xk = np.exp(-np.power(xc, 2.0))
    I_xk = signal.convolve2d(I, xk, "same", "symm")
    yr, yc = np.mgrid[0:H, 0:1]
    yr -= (H - 1) // 2
    yk = np.exp(-np.power(yr, 2.0))
    I_xk_yk = signal.convolve2d(I_xk, yk, "same", "symm")
    I_xk_yk *= 1.0 / (2 * np.pi * pow(sigma, 2.0))
    return I_xk_yk


def DoG(I, size, sigma, k=1.1):
    Is = gaussConv(I, size, sigma)
    Isk = gaussConv(I, size, k * sigma)
    doG = Isk - Is
    doG /= pow(sigma, 2.0) * (k - 1)
    return doG


def zero_cross_default(doG):
    zero_cross = np.zeros(doG.shape, np.uint8)
    rows, cols = doG.shape
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if doG[r][c - 1] * doG[r][c + 1] < 0:
                zero_cross[r][c] = 255
                continue
            if doG[r - 1][c] * doG[r + 1][c] < 0:
                zero_cross[r][c] = 255
                continue
            if doG[r - 1][c - 1] * doG[r + 1][c + 1] < 0:
                zero_cross[r][c] = 255
                continue
            if doG[r - 1][c + 1] * doG[r + 1][c - 1] < 0:
                zero_cross[r][c] = 255
                continue
    return zero_cross


def zero_cross_mean(doG):
    zero_cross = np.zeros(doG.shape, np.uint8)
    fourMean = np.zeros(4, np.float32)
    rows, cols = doG.shape
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            leftTopMean = np.mean(doG[r - 1 : r + 1, c - 1 : c + 1])
            fourMean[0] = leftTopMean
            rightTopMean = np.mean(doG[r - 1 : r + 1, c - 1 : c + 2])
            fourMean[1] = rightTopMean
            leftBottomMean = np.mean(doG[r : r + 2, c - 1 : c + 1])
            fourMean[2] = leftBottomMean
            rightBottomMean = np.mean(doG[r : r + 2, c : c + 2])
            fourMean[3] = rightBottomMean
            if np.min(fourMean) * np.max(fourMean) < 0:
                zero_cross[r][c] = 255
    return zero_cross


def Marr_Hildreth(image, size, sigma, k=1.1, crossType="ZERO_CROSS_DEFAULT"):
    doG = DoG(image, size, sigma, k)
    if crossType == "ZERO_CROSS_DEFAULT":
        zero_cross = zero_cross_default(doG)
    elif crossType == "ZERO_CROSS_MEAN":
        zero_cross = zero_cross_mean(doG)
    else:
        print("no crossType")
    return zero_cross


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)
result = Marr_Hildreth(image, (37, 37), 6, 1.1, "ZERO_CROSS_MEAN")
cv2.imshow("Marr_Hildreth", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
