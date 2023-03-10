# Python 新進測試 14 讀取並使用圖片檔案

from PIL import Image
image = Image.open('data/flower.jpg')
r, g, b = image.split()
convert_image = Image.merge('RGB', (b, g, r))
#convert_image.show()   #顯示圖片
convert_image.save('__temp/rgb_to_bgr.jpg')

from PIL import Image
image = Image.open('data/flower.jpg')
black_and_white = image.convert('1')
#black_and_white.show() #顯示圖片
black_and_white.save('__temp/b_and_w.jpg')

from PIL import Image
image = Image.open('data/flower.jpg')
gray_iamge = image.convert('L')
#gray_iamge.show()  #顯示圖片
gray_iamge.save('__temp/gray_image.jpg') 


from PIL import Image
image = Image.open('data/flower.jpg')
#image.transpose(Image.ROTATE_90).show()
#儲存90度旋轉的圖片#顯示圖片
image.transpose(Image.ROTATE_90).save('__temp/rotate_90.jpg')

print("作業完成")
