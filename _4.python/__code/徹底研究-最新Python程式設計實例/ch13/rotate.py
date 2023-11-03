from PIL import Image
with Image.open("images/building.jpg") as im:
  new_im = im.rotate(180)
  new_im.save( "images/building_rotate.jpg")
