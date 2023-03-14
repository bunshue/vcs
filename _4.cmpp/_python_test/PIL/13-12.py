#在圖上寫字 OK, 只能英文字

from PIL import Image, ImageDraw, ImageFont

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/sample_s.jpg'
selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/ubuntu.ttf'

im = Image.open(filename)
filename = '__temp/tmppic_old'
im.save(filename+'.png', 'PNG')
print('舊檔存圖, 已寫入檔案：'+filename+'.png')

w, h = im.size
print("W = " + str(w)+", H = " + str(h))

print("在圖上作畫")

dw = ImageDraw.Draw(im)

mesg = 'This is a lion-mouse'
font = ImageFont.truetype(selected_font, 80)
#fn_w, fn_h = dw.textsize(unicode(mesg, 'utf-8'), font=font)
fn_w, fn_h = dw.textsize(str(mesg), font=font)

x = w/2-fn_w/2
y = h/2-fn_h/2
dw.text((x+5, y+5), str(mesg), font=font, fill=(25,25,25))
dw.text((x, y), str(mesg), font=font, fill=(128,255,255))

#im.show()
filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/pil_test02.png'
im.save(filename, 'PNG')
print('新檔存圖, 已寫入檔案：'+filename+'.png')



