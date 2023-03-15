#在圖上寫字 OK, 只能英文字

from PIL import Image, ImageDraw, ImageFont

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/ubuntu.ttf'
filename1 = 'C:/_git/vcs/_4.cmpp/_python_test/data/sample_s.jpg'
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/tmppic_old.png'
filename3 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/tmppic_new.png'


im = Image.open(filename1)
im.save(filename2+'.png', 'PNG')
print('舊檔存圖, 已寫入檔案：'+filename2+'.png')

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

#im.show()  #顯示圖片
im.save(filename3, 'PNG')
print('新檔存圖, 已寫入檔案：'+filename3)



