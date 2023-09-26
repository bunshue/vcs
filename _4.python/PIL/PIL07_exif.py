'''
EXIF
'''

print('------------------------------------------------------------')	#60個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/orient2_RightTop.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/orient2_RightTopffff.jpg'

from PIL import Image
from PIL import Image, ImageFilter

image = Image.open(filename1)    #讀取的是RGB格式的圖片

#檢視圖形內嵌的EXIF資料
exif_data = image._getexif()
print("取得圖片內的EXIF資料");
print(exif_data)

from PIL.ExifTags import TAGS

image = Image.open(filename1)

exif_data = image._getexif()

"""
if exif_data is not None:
    for (tag, value) in exif_data.items():
	    key = TAGS.get(tag, tag)
	    print(key + ' = ' + str(value))

"""
print('------------------------------------------------------------')	#60個

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
           

print('------------------------------------------------------------')	#60個

from PIL import Image, ExifTags

# 1 代表正常
# 8 代表順時針轉90度
# 3 代表旋轉180度
# 6 代表逆時針90度

dic_exif = {
    1: 0,
    8: 90,
    3: 180,
    6: -90
}

filename = 'C:/_git/vcs/_1.data/______test_files1/orient2_RightTop.jpg'

print('Processing img {}......'.format(filename))
img = Image.open(filename)
try:
    exif = {
        ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in ExifTags.TAGS
        }
except:
    exif = {
        'Orientation': 1
    }
print(type(exif))
#print(exif)
print(exif['Orientation'])
orient = exif['Orientation']
if orient == 1:
    print('正常顯示')
elif orient == 8:
    print('順時針轉90度')
elif orient == 3:
    print('順時針轉180度')
elif orient == 6:
    print('逆時針轉90度')
else:
    print('XXXXXXX')
    
degree = dic_exif[exif['Orientation']]
# 圖片選轉 ， expand 要設定 (不然旋轉後會有黑邊)
img_clip = img.rotate(degree, expand = 1)
filename2 = 'cccc.jpg'
img_clip.save(filename2, 'JPEG')


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




