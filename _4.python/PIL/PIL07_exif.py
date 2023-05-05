'''
EXIF
'''

from PIL import Image
from PIL import Image, ImageFilter

filename1 = 'C:/_git/vcs/_1.data/______test_files1/orient2_RightTop.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/orient2_RightTopffff.jpg'

image = Image.open(filename1)    #讀取的是RGB格式的圖片

#檢視圖形內嵌的EXIF資料
exif_data = image._getexif()
print("取得圖片內的EXIF資料");
print(exif_data)

from PIL.ExifTags import TAGS

image = Image.open(filename1)
exif_data = image._getexif()

if exif_data is not None:
    for (tag, value) in exif_data.items():
	    key = TAGS.get(tag, tag)
	    print(key + ' = ' + str(value))

from PIL import Image, ExifTags
image = Image.open(filename1)
exif_data = image.getexif()
print(type(exif_data))
# <class 'PIL.Image.Exif'>

if exif_data is None:
    print('Sorry, image has no exif data.')
else:
    for key, val in exif_data.items():
        if key in ExifTags.TAGS:
            print(f'{ExifTags.TAGS[key]}:{val}')
            # ExifVersion:b'0230'
            # ...
            # FocalLength:(2300, 100)
            # ColorSpace:1
            # ...
            





