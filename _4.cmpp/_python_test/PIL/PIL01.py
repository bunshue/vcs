# PIL 測試 1

from PIL import Image

filename0 = 'C:/_git/vcs/_4.cmpp/_python_test/data/flower.jpg'
filename1 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/rgb_to_bgr.jpg'
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/b_and_w.jpg'
filename3 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/gray_image.jpg'
filename4 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/rotate_90.jpg'

image_file = Image.open(filename0)
image_file = image_file.convert('1') #轉換成二值化圖像
image_file.save('result.png')

'''
image_file = Image.open(filename0)
r, g, b = image_file.split()
convert_image = image_file.merge('RGB', (b, g, r))
#convert_image.show()   #顯示圖片
convert_image.save(filename1)
'''

image_file = Image.open(filename0)
black_and_white = image_file.convert('1')	#轉換成二值化圖像
#black_and_white.show() #顯示圖片
black_and_white.save(filename2)

image_file = Image.open(filename0)
gray_iamge = image_file.convert('L')	#轉換成灰階圖像
#gray_iamge.show()  #顯示圖片
gray_iamge.save(filename3) 

image_file = Image.open(filename0)
#image_file.transpose(Image.ROTATE_90).show()
#儲存90度旋轉的圖片#顯示圖片
image_file.transpose(Image.ROTATE_90).save(filename4)


from PIL import Image, ImageFilter

filename1 = 'C:/______test_files/orient2_RightTop.jpg'
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/orient2_RightTopffff.jpg'

#讀取圖形
image_file = Image.open(filename1)
#image_file.show()  #顯示圖片

#對圖形套用過濾器
im_sharp = image_file.filter(ImageFilter.SHARPEN)

#儲存過濾過的圖形到新檔案
im_sharp.save(filename2, 'JPEG')
print("儲存過濾過的圖形, 檔案 : "+filename2);

#分解圖形顏色 例如RGB的紅綠藍
r,g,b = im_sharp.split()

#檢視圖形內嵌的EXIF資料
exif_data = image_file._getexif()
print("取得圖片內的EXIF資料");
print(exif_data)

from PIL.ExifTags import TAGS

image_file = Image.open(filename1)
exif_data = image_file._getexif()

if exif_data is not None:
    for (tag, value) in exif_data.items():
	    key = TAGS.get(tag, tag)
	    print(key + ' = ' + str(value))

from PIL import Image, ExifTags
image_file = Image.open(filename1)
exif_data = image_file.getexif()
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


