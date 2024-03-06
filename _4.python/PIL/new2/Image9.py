from PIL import Image
img = Image.open("img01.jpg")
imgcopy=img.copy()
imgcopy.save("imgcopy.png")