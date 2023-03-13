from PIL import Image, ImageDraw

filename = 'data\sample_s.jpg'

im = Image.open(filename)

filename = '__temp/tmppic_old'
im.save(filename+'.png', 'PNG')
print('舊檔存圖, 已寫入檔案：'+filename+'.png')

w, h = im.size
print("W = " + str(w)+", H = " + str(h))

dw = ImageDraw.Draw(im)

print("在圖上作畫")
dw.line((0,0,w,h),width=20, fill=(255,0,0))
dw.line((w,0,0,h),width=20, fill=(255,0,0))
dw.ellipse((50,50,w-50,h-50),outline=(255,255,0))
dw.text((100,100),'This is a test image')

#im.show()
filename = '__temp/tmppic_new'
im.save(filename+'.png', 'PNG')
print('新檔存圖, 已寫入檔案：'+filename+'.png')
