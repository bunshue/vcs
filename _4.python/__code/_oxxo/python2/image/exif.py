# coding:utf-8
import piexif
from PIL import Image

#https://pypi.org/project/piexif/
#https://bit.ly/2RwbD2y

im = Image.open("test.JPG")
exif_dict = piexif.load(im.info["exif"])
# process im and exif_dict...
print(exif_dict["0th"])
exif_dict["0th"][270] = b''              # 影像描述
exif_dict["0th"][271] = b'OXXO.STUDIO'   # 製作
exif_dict["0th"][272] = b'GoPro Max'     # 機型
exif_dict["0th"][305] = b'Python'        # 軟體
print('')
print(exif_dict["Exif"])
exif_dict["Exif"][36867] = b'2020:01:20 09:52:51'  # 製作日期
exif_dict["Exif"][36868] = b'2020:01:20 09:52:51'  # 數位製作日期
print(exif_dict["Exif"])
print('')
print(exif_dict["GPS"])
print('')
print(exif_dict["1st"])
exif_new = piexif.dump(exif_dict)
#print(exif_new)
im.save("out.jpg", "JPEG", exif = exif_new )
