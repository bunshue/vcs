from PIL import Image
im = Image.open("images/食物1.jpg")
pic=im.convert("1")
pic.show()
