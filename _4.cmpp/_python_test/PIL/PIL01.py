# Python 新進測試 14 讀取並使用圖片檔案

from PIL import Image

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/flower.jpg'
image = Image.open(filename)
r, g, b = image.split()
convert_image = Image.merge('RGB', (b, g, r))
#convert_image.show()   #顯示圖片
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/rgb_to_bgr.jpg'
convert_image.save(filename2)

from PIL import Image
image = Image.open(filename)
black_and_white = image.convert('1')
#black_and_white.show() #顯示圖片
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/b_and_w.jpg'
black_and_white.save(filename2)

from PIL import Image
image = Image.open(filename)
gray_iamge = image.convert('L')
#gray_iamge.show()  #顯示圖片
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/gray_image.jpg'
gray_iamge.save(filename2) 

from PIL import Image
image = Image.open(filename)
#image.transpose(Image.ROTATE_90).show()
#儲存90度旋轉的圖片#顯示圖片
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/rotate_90.jpg'
image.transpose(Image.ROTATE_90).save(filename2)

print("作業完成")
