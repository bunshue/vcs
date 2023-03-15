from PIL import Image, ImageFilter

#讀取圖形
filename = 'C:/______test_files/orient2_RightTop.jpg'
im = Image.open(filename)
#顯示圖形
#im.show()

#對圖形套用過濾器
im_sharp = im.filter(ImageFilter.SHARPEN)

#儲存過濾過的圖形到新檔案
filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/orient2_RightTopffff.jpg'
im_sharp.save(filename, 'JPEG')
print("儲存過濾過的圖形, 檔案 : "+filename);

#分解圖形顏色 例如RGB的紅綠藍
r,g,b = im_sharp.split()

#檢視圖形內嵌的EXIF資料
exif_data = im._getexif()
print("取得圖片內的EXIF資料");
print(exif_data)

