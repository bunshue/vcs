from PIL import Image
im = Image.open("images/cute.jpg")
im.save( "images/kid.jpg" )
im.close()
