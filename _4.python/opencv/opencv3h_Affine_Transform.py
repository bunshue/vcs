"""
AffineTransform

PerspectiveTransform

"""

from opencv_common import *

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 08")
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image = cv2.imread(filename)

H, W, D = image.shape

x = 50
y = 50
M = np.float32([[1, 0, x], [0, 1, y]])
move = cv2.warpAffine(image, M, (W, H))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(move, cv2.COLOR_BGR2RGB))
plt.title("影像移動")

plt.suptitle("影像移動")
show()

print("------------------------------------------------------------")  # 60個

print("opencv 09")
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

image = cv2.imread(filename)

H, W, D = image.shape

p1 = np.float32([[0, 0], [W - 1, 0], [0, H - 1]])
p2 = np.float32([[0, H * 0.33], [W * 0.85, H * 0.25], [W * 0.15, H * 0.7]])
M = cv2.getAffineTransform(p1, p2)
dst = cv2.warpAffine(image, M, (W, H))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("Affine(仿射的)Transform")

plt.suptitle("Affine(仿射的)Transform")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 10")
filename = r"data/PerspectiveTransform/PerspectiveTransform.jpg"

image = cv2.imread(filename)

H, W, D = image.shape

pts1 = np.float32([[150, 50], [400, 50], [60, 450], [310, 450]])
pts2 = np.float32([[50, 50], [H - 50, 50], [50, W - 50], [H - 50, W - 50]])

pts1 = np.float32([[200, 0], [300, 0], [100, 600], [200, 600]])
pts2 = np.float32([[100, 0], [200, 0], [100, 600], [200, 600]])


pts1 = np.float32([[100, 0], [600, 0], [0, 600], [500, 600]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])


M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(image, M, (W, H))

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖是歪圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("把歪圖拉正")

plt.suptitle("PerspectiveTransform")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 98")

# 圖形變換
# 幾何變換

# 對圖形進行仿射變換
img = cv2.imread("data/lena.jpg")
h, w = img.shape[:2]
src = np.array([[0, 0], [w - 1, 0], [0, h - 1]], dtype=np.float32)
dst = np.array([[300, 300], [873, 78], [161, 923]], dtype=np.float32)

m = cv2.getAffineTransform(src, dst)
result = cv2.warpAffine(img, m, (2 * w, 2 * h), borderValue=(255, 255, 255, 255))

fig, ax = plt.subplots(figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(-5, w * 2 + 5)
ax.set_ylim(h * 2 + 5, -5)
ax.axis("off")
ax.imshow(result[:, :, ::-1])
ax.imshow(img[:, :, ::-1], alpha=0.4)
p = np.vstack((src, src[:1]))
ax.plot(p[:, 0], p[:, 1], "-o", alpha=0.5)

from matplotlib.patches import FancyArrowPatch

for p1, p2 in zip(src, dst):
    arrow = FancyArrowPatch(
        p1, p2, transform=ax.transData, color="gray", mutation_scale=10
    )
    ax.add_artist(arrow)

show()


print("------------------------------")  # 30個

print("opencv 99")

# 對圖形進行透視變換
src = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
dst = np.array([[300, 350], [800, 300], [900, 923], [161, 923]], dtype=np.float32)

m = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, m, (2 * w, 2 * h), borderValue=(255, 255, 255, 255))

fig, ax = plt.subplots(figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(-5, w * 2 + 5)
ax.set_ylim(h * 2 + 5, -5)
ax.axis("off")
ax.imshow(result[:, :, ::-1])
ax.imshow(img[:, :, ::-1], alpha=0.4)
p = np.vstack((src, src[:1]))
ax.plot(p[:, 0], p[:, 1], "-o", alpha=0.5)

from matplotlib.patches import FancyArrowPatch

for p1, p2 in zip(src, dst):
    arrow = FancyArrowPatch(
        p1, p2, transform=ax.transData, color="gray", mutation_scale=10
    )
    ax.add_artist(arrow)

show()


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


print("------------------------------------------------------------")  # 60個
