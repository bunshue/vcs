from PIL import Image
with Image.open("pic/3.jpg") as im:
  new_im = im.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')
  new_im.save( "pic/3_rotate0.jpg")
  
