# -*- coding:utf-8 -*-
# file: pyOpenGLTexture.py
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import Image
class OpenGLWindow:
	def __init__(self, width = 640, height = 480, title = 'PyOpenGL'):	# 起始化
		glutInit(sys.argv)						# 傳遞指令行參數
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)	# 設定顯示模式
		glutInitWindowSize(width, height)				# 設定視窗大小
		self.window = glutCreateWindow(title)				# 建立視窗
		glutDisplayFunc(self.Draw)					# 設定場景繪制函數
		glutIdleFunc(self.Draw)						# 設定閒置時場景繪制函數
		self.InitGL(width, height)					# 呼叫OpenGL起始化函數
		self.x = 0.2							# 旋轉角度增量
		self.y = 0.2
		self.z = 0.2
	def Draw(self):								# 繪制場景
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)		# 清除螢幕
		glLoadIdentity()						# 重設觀察矩陣
		glTranslatef(0.0,0.0,-5.0)					# 搬移位置
		glRotatef(self.x,1.0,0.0,0.0)					# 繞X軸旋轉
		glRotatef(self.y,0.0,1.0,0.0)					# 繞Y軸旋轉
		glRotatef(self.z,0.0,0.0,1.0)					# 繞Z軸旋轉
		glBegin(GL_QUADS)			    			# 繪制立方體
		glTexCoord2f(0.0, 0.0) 						# 對前面進行貼圖
		glVertex3f(-1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 
		glVertex3f( 1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f( 1.0,  1.0,  1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f(-1.0,  1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 						# 對後面進行貼圖
		glVertex3f(-1.0, -1.0, -1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f(-1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f( 1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 0.0)
		glVertex3f( 1.0, -1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 						# 對頂面進行貼圖 
		glVertex3f(-1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 0.0) 
		glVertex3f(-1.0,  1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 
		glVertex3f( 1.0,  1.0,  1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f( 1.0,  1.0, -1.0)
		glTexCoord2f(1.0, 1.0) 						# 對底面進行貼圖
		glVertex3f(-1.0, -1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f( 1.0, -1.0, -1.0)
		glTexCoord2f(0.0, 0.0) 
		glVertex3f( 1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 0.0)
		glVertex3f(-1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 						# 對右側面進行貼圖
		glVertex3f( 1.0, -1.0, -1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f( 1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f( 1.0,  1.0,  1.0)
		glTexCoord2f(0.0, 0.0) 
		glVertex3f( 1.0, -1.0,  1.0)
		glTexCoord2f(0.0, 0.0) 						# 對左側面進行貼圖
		glVertex3f(-1.0, -1.0, -1.0)
		glTexCoord2f(1.0, 0.0) 
		glVertex3f(-1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f(-1.0,  1.0,  1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f(-1.0,  1.0, -1.0)
		glEnd()			
		glutSwapBuffers()						# 交換快取
		self.x = self.x + 0.2						# 旋轉角度增加
		self.y = self.y + 0.2
		self.z = self.z + 0.2
	def InitGL(self, width, height):					# OpenGL起始化函數
    		self.LoadTextures()						# 載入紋理
    		glEnable(GL_TEXTURE_2D)						# 容許紋理映射
		glClearColor(0.0, 0.0, 0.0, 0.0)				# 設為黑色背景 
		glClearDepth(1.0)						# 設定深度快取
		glDepthFunc(GL_LESS)						# 設定深度測試型態
		glEnable(GL_DEPTH_TEST)						# 容許深度測試
		glShadeModel(GL_SMOOTH)						# 啟動平順陰影
		glMatrixMode(GL_PROJECTION)					# 設定觀察矩陣
		glLoadIdentity()						# 重設觀察矩陣
		gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)	# 計算螢幕高寬比
		glMatrixMode(GL_MODELVIEW)					# 設定觀察矩陣
	def LoadTextures(self):							# 載入紋理圖片
		image = Image.open('python.bmp')				# 開啟圖片
		width = image.size[0]						# 圖形寬度
		height = image.size[1]						# 圖形高度
		image = image.tostring('raw', 'RGBX', 0, -1)			# 轉換圖形
		glBindTexture(GL_TEXTURE_2D, glGenTextures(1))   		# 建立紋理
		glPixelStorei(GL_UNPACK_ALIGNMENT,1)
		glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 
				0, GL_RGBA, GL_UNSIGNED_BYTE, image)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
	def MainLoop(self):							# 進入訊息循環
		glutMainLoop()
window = OpenGLWindow()								# 建立視窗
window.MainLoop()								# 進入訊息循環
