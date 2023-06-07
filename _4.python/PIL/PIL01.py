# PIL 測試 1

from PIL import Image
from PIL import Image, ImageFilter

filename1 = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/bear_filter.jpg'

image = Image.open(filename1)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
#image.show()  #顯示圖片

#對圖形套用過濾器
im_sharp = image.filter(ImageFilter.SHARPEN)

#儲存過濾過的圖形到新檔案
im_sharp.save(filename2, 'JPEG')
print("儲存過濾過的圖形, 檔案 : "+filename2);

#分解圖形顏色 例如RGB的紅綠藍
#看不出效果
r,g,b = im_sharp.split()


print("作業完成")


