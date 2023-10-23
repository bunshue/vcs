from PIL import Image

def blue_to_red(image_path):
    img = Image.open(image_path)
    r, g, b = img.split() # 分離三個通道
    img = Image.merge("RGB",(b,g,r))# 將藍色通道和通道互換
    img.show()

blue_to_red("blue_image.jpg")












