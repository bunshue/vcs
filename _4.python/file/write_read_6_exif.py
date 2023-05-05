import os
import time
import exifread

def get_year_month(fullpathname):
    fp = open(fullpathname, 'rb')
    exif = exifread.process_file(fp)
    ym = 0
    if 'EXIF DateTimeOriginal' in exif:
        print('有 EXIF 資料')
        ym = exif['EXIF DateTimeOriginal'].values
    else:
        print('無 EXIF 資料, 使用檔案時間')
        ym = time.strftime('%Y:%m:%d', time.localtime(os.stat(fullpathname).st_ctime))
        fp.close()
    return ym[0:4], ym[5:7]

imagefile = 'C:/_git/vcs/_1.data/______test_files1/orient1.jpg'
y, m = get_year_month(imagefile)
print(y)
print(m)

