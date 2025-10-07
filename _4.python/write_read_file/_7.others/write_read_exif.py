import os
import sys
import time
import exifread

filename = "D:/_git/vcs/_1.data/______test_files1/orient1.jpg"
filename = 'D:/_git/vcs/_1.data/______test_files1/__pic/_gps/pic_gps2.jpg'

print("------------------------------------------------------------")  # 60個


def get_year_month(fullpathname):
    fp = open(fullpathname, "rb")
    exif = exifread.process_file(fp)
    ym = 0
    if "EXIF DateTimeOriginal" in exif:
        print("有 EXIF 資料")
        ym = exif["EXIF DateTimeOriginal"].values
        print(ym)
    else:
        print("無 EXIF 資料, 使用檔案時間")
        ym = time.strftime("%Y:%m:%d", time.localtime(os.stat(fullpathname).st_ctime))
        fp.close()
        print(ym)
    return ym[0:4], ym[5:7], ym[8:10]


yyyy, mm, dd = get_year_month(filename)
print("年", yyyy)
print("月", mm)
print("日", dd)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from PIL import Image, ExifTags
from datetime import datetime

print(filename)

image_exif = Image.open(filename)._getexif()
if image_exif:
    print("原始資料")
    print(type(image_exif))
    print(image_exif)

    print("搭配標籤")
    exif = {
        ExifTags.TAGS[k]: v
        for k, v in image_exif.items()
        if k in ExifTags.TAGS and type(v) is not bytes
    }
    print(type(exif))
    print(exif)

    print("取得時間")
    date_obj = datetime.strptime(exif["DateTimeOriginal"], "%Y:%m:%d %H:%M:%S")
    print(date_obj)

    print("GPS資訊")
    gps_info = exif["GPSInfo"]
    print(type(gps_info))
    print(gps_info)
    print("南或北 :", gps_info[1])
    print("緯度 :", gps_info[2])
    print("東或西 :", gps_info[3])
    print("經度 :", gps_info[4])
    print("高度參考 :", gps_info[5])
    print("高度 :", gps_info[6])
    print("GPS時間 :", gps_info[7])
    print("GPS時間 :", gps_info[29])

else:
    print("Unable to get date from exif for %s" % filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from PIL import Image
import piexif

img = Image.open(filename)  # 使用 PIL Image 開啟圖片
exif = piexif.load(img.info["exif"])  # 使用 piexif 讀取圖片 Exif 資訊
print(exif)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from PIL import Image
import piexif

img = Image.open(filename)
exif = piexif.load(img.info["exif"])
# 建立字典對照表
info = {
    "0th": [271, 272, 282, 283, 305, 306, 316],
    "Exif": [
        33434,
        33437,
        34855,
        36867,
        36868,
        36880,
        36881,
        36882,
        40962,
        40963,
        42035,
        42036,
    ],
    "1st": [282, 283],
    "GPS": [2, 4, 5, 17, 24, 31],
}
# 根據對照表，印出照片 exif 裡的資訊 ( 有就印出，沒有就略過 )
for i in info:
    for j in info[i]:
        if j in exif[i]:
            print(j, ":", exif[i][j])


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from PIL import Image
import piexif

img = Image.open(filename)
exif = piexif.load(img.info["exif"])

exif["0th"][305] = b"OXXO.STUDIO"  # 修改編輯軟體
exif["0th"][306] = b"2020:01:01 00:00:00"  # 修改編輯時間
exif["Exif"][36867] = b"2020:01:01 00:00:00"  # 加入檔案建立時間
exif["Exif"][36868] = b"2020:01:01 00:00:00"  # 加入檔案建立時間
exif_new = piexif.dump(exif)  # 更新 Exif
img.save("./tmp_iphone-edit.jpg", exif=exif_new)  # 另存新檔並加入 Exif

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename1 = "D:/_git/vcs/_1.data/______test_files1/orient2_RightTop.jpg"

from PIL import Image
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

image = Image.open(filename1)  # 讀取的是RGB格式的圖片

# 檢視圖形內嵌的EXIF資料
exif_data = image._getexif()
print("取得圖片內的EXIF資料")
print(exif_data)

from PIL.ExifTags import TAGS

image = Image.open(filename1)

exif_data = image._getexif()

"""
if exif_data is not None:
    for (tag, value) in exif_data.items():
	    key = TAGS.get(tag, tag)
	    print(key + ' = ' + str(value))

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from PIL import Image, ExifTags

image = Image.open(filename1)
exif_data = image.getexif()
print(type(exif_data))
# <class 'PIL.Image.Exif'>

if exif_data is None:
    print("Sorry, image has no exif data.")
else:
    for key, val in exif_data.items():
        if key in ExifTags.TAGS:
            print(f"{ExifTags.TAGS[key]}:{val}")
            # ExifVersion:b'0230'
            # ...
            # FocalLength:(2300, 100)
            # ColorSpace:1
            # ...


print("------------------------------------------------------------")  # 60個

from PIL import Image, ExifTags

# 1 代表正常
# 8 代表順時針轉90度
# 3 代表旋轉180度
# 6 代表逆時針90度

dic_exif = {1: 0, 8: 90, 3: 180, 6: -90}

filename = "D:/_git/vcs/_1.data/______test_files1/orient2_RightTop.jpg"

print("Processing image {}......".format(filename))
image = Image.open(filename)

plt.imshow(image)
plt.show()

try:
    exif = {
        ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS
    }
except:
    exif = {"Orientation": 1}
print(type(exif))
# print(exif)
print(exif["Orientation"])
orient = exif["Orientation"]
if orient == 1:
    print("正常顯示")
elif orient == 8:
    print("順時針轉90度")
elif orient == 3:
    print("順時針轉180度")
elif orient == 6:
    print("逆時針轉90度")
else:
    print("XXXXXXX")

degree = dic_exif[exif["Orientation"]]
# 圖片選轉 ， expand 要設定 (不然旋轉後會有黑邊)
image_rotated = image.rotate(degree, expand=1)
filename2 = "tmp_cccc.jpg"
# image_rotated.save(filename2, 'JPEG')

plt.imshow(image_rotated)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('修改 Exif 資料')

import piexif
from PIL import Image

# https://pypi.org/project/piexif/
# https://bit.ly/2RwbD2y

filename = 'D:/_git/vcs/_1.data/______test_files1/__pic/_gps/pic_gps1.jpg'

im = Image.open(filename)
exif_dict = piexif.load(im.info["exif"])
# process im and exif_dict...
print("EXIF")
print(exif_dict["0th"])
exif_dict["0th"][270] = b""  # 影像描述 ImageDescription
exif_dict["0th"][271] = b"DAVID WANG"  # 製作 Make
exif_dict["0th"][272] = b"Samsung Note 9"  # 機型 Model
exif_dict["0th"][305] = b"Python"  # 軟體 Software
print("")

print("EXIF")
print(exif_dict["Exif"])
exif_dict["Exif"][36867] = b"2024:03:11 12:34:56"  # 製作日期 DateTimeOriginal
exif_dict["Exif"][36868] = b"2024:03:11 12:34:56"  # 數位製作日期 DateTimeDigitized

print("EXIF")
print(exif_dict["Exif"])
print("")

print("GPS")
print(exif_dict["GPS"])
print("")

print("lst")
print(exif_dict["1st"])
exif_new = piexif.dump(exif_dict)

# print(exif_new)

filename2 = "tmp_pic_gps_modify.jpg"

im.save(filename2, "JPEG", exif=exif_new)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 浅析python中获取图片中exif中的gps方法

from PIL import Image
from PIL.ExifTags import TAGS


def get_exif_data(fname):  # 定义获取图片exif的方法
    """Get embedded EXIF data from image file."""
    ret = {}  # 创建一个字典对象存储exif的条目如相机品牌：相应品牌这样的数据
    try:
        img = Image.open(fname)  # 创建图像对象
        if hasattr(img, "_getexif"):  # 检查图像对象有无_getexif属性，发现也有getexif属性，内容好像差不多
            exifinfo = img._getexif()  # 取出img的_getexif属性，这是一个字典对象
            if exifinfo != None:  # 判断检查
                for tag, value in exifinfo.items():  # 取出字典的项，值
                    decoded = TAGS.get(
                        tag, tag
                    )  # TAGS实际是一字典对象，记录着类型001：相机品牌，002：光圈这样的条目，_getexif的项全是数字，并不是具体项目，所以需在TAGS里检索对应的实际项目
                    ret[decoded] = value
    except IOError:
        print("IOERROR " + fname)
    return ret


# 定义了方法后我们可以取出exif里的gps信息

filename = "D:/_git/vcs/_1.data/______test_files1/orient1.jpg"
filename = "D:/_git/vcs/_1.data/______test_files1/orient2_RightTop.jpg"

Img_exif = get_exif_data(filename)  # 用自定函数取得exif信息
if Gps_Info := Img_exif.get("GPSInfo"):  # 简单做个判定有无gps信息，这里用了海象运算符
    print("cccccc")
    print(type(Gps_Info))
    print(Gps_Info)
    print("-------------")
    print(Gps_Info.get(1))  # 1项对应是N还是S，也就是南北
    """
    NS_point = Gps_Info.get(
        2
    )  # 2项对应是纬度信息，是多元元组，每组是度，分，秒，里面数值是当前值及精度，NS_point[0][0] / NS_point[0][1]这个就是度了，以此类推，所以后面两组分别除60，3600，换算为度，并相加他们就组成以小数表示的纬度
    print(
        NS_point[0][0] / NS_point[0][1]
        + NS_point[1][0] / NS_point[1][1] / 60
        + NS_point[2][0] / NS_point[2][1] / 3600
    )
    print(Gps_Info.get(3))  # 3项对应是EW也就是东西
    EW_point = Gps_Info.get(4)  # 如上处理经度信息
    print(
        EW_point[0][0] / EW_point[0][1]
        + EW_point[1][0] / EW_point[1][1] / 60
        + EW_point[2][0] / EW_point[2][1] / 3600
    )
    # 得出这些信息大家可具体灵活运用，比如有些在线地图可直接在地址处提交经纬度定位到GPS具体位置的
    """
else:
    print("no gps data")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

