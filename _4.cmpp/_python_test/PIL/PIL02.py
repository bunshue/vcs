# 各種未歸類的import

from PIL import Image, ImageFilter

filename1 = 'C:/______test_files/orient2_RightTop.jpg'
filename2 = '__temp/orient2_RightTopffff.jpg'

#讀取圖形
im = Image.open(filename1)
#顯示圖形
#im.show()

#對圖形套用過濾器
im_sharp = im.filter(ImageFilter.SHARPEN)

#儲存過濾過的圖形到新檔案
im_sharp.save(filename2, 'JPEG')

print("儲存過濾過的圖形, 檔案 : "+filename2);

#分解圖形顏色 例如RGB的紅綠藍
r,g,b = im_sharp.split()


#檢視圖形內嵌的EXIF資料
exif_data = im._getexif()
print("取得圖片內的EXIF資料");
print(exif_data)

