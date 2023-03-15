# Python 新進測試 14 讀取並使用圖片檔案

from PIL import Image

filename0 = 'C:/_git/vcs/_4.cmpp/_python_test/data/flower.jpg'
filename1 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/rgb_to_bgr.jpg'
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/b_and_w.jpg'
filename3 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/gray_image.jpg'
filename4 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/rotate_90.jpg'

im = Image.open(filename0)
r, g, b = im.split()
convert_image = im.merge('RGB', (b, g, r))
#convert_image.show()   #顯示圖片
convert_image.save(filename1)

from PIL import Image
im = Image.open(filename0)
black_and_white = im.convert('1')
#black_and_white.show() #顯示圖片
black_and_white.save(filename2)

from PIL import Image
im = Image.open(filename0)
gray_iamge = im.convert('L')
#gray_iamge.show()  #顯示圖片
gray_iamge.save(filename3) 

from PIL import Image
im = Image.open(filename0)
#im.transpose(Image.ROTATE_90).show()
#儲存90度旋轉的圖片#顯示圖片
im.transpose(Image.ROTATE_90).save(filename4)

print("作業完成")
