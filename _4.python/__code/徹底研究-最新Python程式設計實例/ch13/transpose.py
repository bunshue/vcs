from PIL import Image
with Image.open("images/building.jpg") as im:
  new_im = im.transpose(Image.ROTATE_90)
  new_im.save( "images/building_90.jpg")
  new_im = im.transpose(Image.FLIP_LEFT_RIGHT)
  new_im.save( "images/building_flip.jpg")
