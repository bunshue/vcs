from PIL import Image, ImageDraw, ImageFont

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/ubuntu.ttf'

font_size=30

mesg = 'this is a lion mouse'

font = ImageFont.truetype(selected_font, font_size)
font_size = font.getsize(mesg)
print(font_size)

width = font_size[0]
height = font_size[1]

img = Image.new('RGBA', (width, height), (255, 255, 255, 0))

draw = ImageDraw.Draw(img)

#寫字
draw.text((0,0), mesg, (0,0,0), font)

filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/pil_test01.png'
img.save(filename)
print('已寫入檔案：' + filename)


