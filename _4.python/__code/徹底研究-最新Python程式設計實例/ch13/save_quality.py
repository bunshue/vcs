from PIL import Image
im = Image.open("images/cute.jpg")
im.save("images/kid_high.jpg", quality=95 )
im.close()
