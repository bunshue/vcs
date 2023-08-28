import cv2
try:
	cam=cv2.VideoCapture(0)
except:
	print('请连接摄像头')


#从摄像头读取图片
sucess,img=cam.read()
#保存图片，并退出
cv2.imwrite('file/test.jpg')
#加载图像
image=pygame.image.load('file/test.jpg')
#设置图片大小
image=pygame.transform.scale(image,(640,480))
#绘制视频画面
screen.blit(image,(2,2))

