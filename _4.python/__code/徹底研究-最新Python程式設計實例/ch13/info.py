from PIL import Image
im = Image.open("images/cute.jpg")
print('圖檔格式: ',im.format)
print('圖檔的色彩模式: ',im.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ',im.size)
print('圖片的寬度，單位像素(pixels): ',im.width)
print('圖片的高度，單位像素(pixels): ',im.height)
