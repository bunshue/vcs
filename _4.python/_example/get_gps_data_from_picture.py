#浅析python中获取图片中exif中的gps方法

from PIL import Image
from PIL.ExifTags import TAGS
def get_exif_data(fname): #定义获取图片exif的方法
    """Get embedded EXIF data from image file."""
    ret = {}     #创建一个字典对象存储exif的条目如相机品牌：相应品牌这样的数据
    try:
        img = Image.open(fname)      #创建图像对象
        if hasattr(img, '_getexif'):      #检查图像对象有无_getexif属性，发现也有getexif属性，内容好像差不多
            exifinfo = img._getexif()   #取出img的_getexif属性，这是一个字典对象
            if exifinfo != None:  #判断检查
                for tag, value in exifinfo.items(): #取出字典的项，值
                    decoded = TAGS.get(tag, tag) #TAGS实际是一字典对象，记录着类型001：相机品牌，002：光圈这样的条目，_getexif的项全是数字，并不是具体项目，所以需在TAGS里检索对应的实际项目
                    ret[decoded] = value
    except IOError:
        print ('IOERROR ' + fname)
    return ret



#定义了方法后我们可以取出exif里的gps信息

fileName = 'C:/dddddddddd/__手機來的圖片1/20230113_103319.jpg'
if __name__ == '__main__':
    #fileName = r'' #有GPS的照片位置
    Img_exif = get_exif_data(fileName) #用自定函数取得exif信息
    if Gps_Info:=Img_exif.get('GPSInfo'): #简单做个判定有无gps信息，这里用了海象运算符
        print(Gps_Info.get(1)) #1项对应是N还是S，也就是南北
        NS_point=(Gps_Info.get(2)) #2项对应是纬度信息，是多元元组，每组是度，分，秒，里面数值是当前值及精度，NS_point[0][0] / NS_point[0][1]这个就是度了，以此类推，所以后面两组分别除60，3600，换算为度，并相加他们就组成以小数表示的纬度
        print(NS_point[0][0] / NS_point[0][1] + NS_point[1][0] / NS_point[1][1] / 60 + NS_point[2][0] / NS_point[2][1] / 3600)
        print(Gps_Info.get(3)) #3项对应是EW也就是东西
        EW_point=Gps_Info.get(4) #如上处理经度信息
        print(EW_point[0][0] / EW_point[0][1] + EW_point[1][0] / EW_point[1][1] / 60 + EW_point[2][0] / EW_point[2][1] / 3600)
        #得出这些信息大家可具体灵活运用，比如有些在线地图可直接在地址处提交经纬度定位到GPS具体位置的
    else:
        print('no gps data')



