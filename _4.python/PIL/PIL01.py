# PIL 測試 1

from PIL import Image

filename = 'C:/______test_files2/flower.jpg'

image = Image.open(filename)    #讀取的是RGB格式的圖片
#image.show()

image = Image.open(filename)
#image.transpose(Image.ROTATE_90).show()
#儲存90度旋轉的圖片#顯示圖片
image.transpose(Image.ROTATE_90)

from PIL import Image, ImageFilter

filename1 = 'C:/______test_files/orient2_RightTop.jpg'
filename2 = 'C:/______test_files3/orient2_RightTopffff.jpg'

#讀取圖形
image = Image.open(filename1)
#image.show()  #顯示圖片

#對圖形套用過濾器
im_sharp = image.filter(ImageFilter.SHARPEN)

#儲存過濾過的圖形到新檔案
im_sharp.save(filename2, 'JPEG')
print("儲存過濾過的圖形, 檔案 : "+filename2);

#分解圖形顏色 例如RGB的紅綠藍
r,g,b = im_sharp.split()

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
            


print("作業完成")


