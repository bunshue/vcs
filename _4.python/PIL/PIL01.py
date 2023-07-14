'''

裁剪圖片

'''

from PIL import Image   # Importing Image class from PIL module

filename = r'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

# Opens a image in RGB mode
im = Image.open(filename)
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

print(width)
print(height)

# Setting the points for cropped image
left = 20
top = 20
right = width - 20 *2
bottom = height - 20 * 2
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))

 
# Shows the image in image viewer
im.show()
im1.show()

