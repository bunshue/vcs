# 在圖上作畫

from PIL import Image, ImageDraw

filename1 = 'C:/_git/vcs/_4.cmpp/_python_test/data/sample_s.jpg'
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/tmppic_old.png'
filename3 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/tmppic_new.png'


im = Image.open(filename1)

im.save(filename2, 'PNG')
print('舊檔存圖, 已寫入檔案：'+filename2)

w, h = im.size
print("W = " + str(w)+", H = " + str(h))

print("在圖上作畫")

dw = ImageDraw.Draw(im)

#畫一個外框
dw.rectangle((0,0,w,h), fill=None, outline=(255,0,0), width=10)
#畫線
dw.line((0,0,w,h),width=20, fill=(255,0,0))
dw.line((w,0,0,h),width=20, fill=(255,0,0))
#畫圓
dw.ellipse((0,0,w,h),outline=(255,255,0))
#寫字
mesg = 'This is a lion-mouse'
dw.text((100,100), mesg)

#im.show()  #顯示圖片

im.save(filename3, 'PNG')
print('新檔存圖, 已寫入檔案：'+filename3)
