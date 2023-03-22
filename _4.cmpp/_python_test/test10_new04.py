import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

#image_path = "street.jpg"  #本機圖片檔路徑
image_path = "C:/______test_files/picture1.jpg"

image_data = open(image_path, "rb").read()  #讀取圖片檔

image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
plt.title('AAAA', size="x-large", y=-0.1)

plt.show()




