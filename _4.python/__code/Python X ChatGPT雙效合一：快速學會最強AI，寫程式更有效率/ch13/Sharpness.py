from PIL import Image,ImageEnhance
with Image.open("pic/1.jpg") as im:
    new_im = ImageEnhance.Contrast(im).enhance(0.3)
    new_im.save( "pic/1_Contrast.jpg") 
