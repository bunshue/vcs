from PIL import Image

print('圖片裁剪縮放')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'

image = Image.open(filename)    #PIL讀取本機圖片

x = 100
y = 100
w = 100
h = 100

image1 = Image.open(filename)   #PIL讀取本機圖片
image2 = image1.crop((x, y, x + w, y + h))
image3 = image2.resize((100, 300), Image.ANTIALIAS)
image3.save(filename2)

print('完成')
