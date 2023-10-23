from PIL import Image,ImageEnhance
with Image.open("images/tailand.jpg") as im:
   new_im = ImageEnhance.Brightness(im).enhance(2.5)
   new_im.save( "images/tailand_Brightness.jpg")
