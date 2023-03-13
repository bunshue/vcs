from PIL import Image, ImageDraw, ImageFont

msg = 'lion-mouse'

font_size = 30; #文字大小
font_r = 255;   #紅色值
font_g = 0;     #綠色值
font_b = 0;     #藍色值

fill = (font_r, font_g, font_b)

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)
font = ImageFont.truetype('data/ubuntu.ttf',font_size)
fn_w, fn_h = dw0.textsize(msg, font=font)
im = Image.new('RGBA', (fn_w, fn_h), (255,255,255,0))
dw = ImageDraw.Draw(im)
dw.text((0,0), msg, font=font, fill=fill)

#im.show()
filename = '__temp/tmppic_new'
im.save(filename+'.png', 'PNG')
print('新檔存圖, 已寫入檔案：'+filename+'.png')

