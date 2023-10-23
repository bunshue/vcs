from PIL import Image
with Image.open("images/view.jpg") as im:
  new_im = im.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
  new_im.save( "images/view30.jpg")

