# -*- coding:utf-8 -*-
# file: pyOpenGLDraw2D.py
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
class OpenGLWindow:
	def __init__(self, width = 640, height = 480, title = 'PyOpenGL'):	# 起始化
		glutInit(sys.argv)						# 傳遞指令行參數
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)	# 設定顯示模式
		glutInitWindowSize(width, height)				# 設定視窗大小
		self.window = glutCreateWindow(title)				# 建立視窗
		glutDisplayFunc(self.Draw)					# 設定場景繪制函數
		self.InitGL(width, height)					# 呼叫OpenGL起始化函數
	def Draw(self):								# 繪制場景
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()						# 重設觀察矩陣
		glTranslatef(-2.0, 2.0, -6.0)					# 搬移位置
		glBegin(GL_LINES)						# 繪制直線
		glVertex3f(0.0, 0.0, 0.0)					# 直線第一點座標
		glVertex3f(2.0, 0.0, 0.0)					# 直線第二點座標
		glEnd()								# 結束繪制
		glTranslatef(3.0, 0.0, 0.0)					# 搬移位置
		glBegin(GL_POLYGON)						# 透過繪制多邊形來類比圓
		i = 0
		while( i <= 3.14 *2 ):
			x = 0.5 * math.cos(i)
			y = 0.5 * math.sin(i)
			glVertex3f(x, y, 0.0)
			i = i + 0.01
		glEnd()
		glTranslatef(-2, -3.0, 0.0)					# 搬移位置
		glBegin(GL_POLYGON)                 				# 繪制三角行
		glVertex3f(0.0, 1.0, 0.0)
		glVertex3f(1.0, -1.0, 0.0)
		glVertex3f(-1.0, -1.0, 0.0)
		glEnd()
		glTranslatef(2.5, 0.0, 0.0)					# 搬移位置
		glBegin(GL_QUADS)                   				# 繪制四邊形
		glVertex3f(-1.0, 1.0, 0.0)
		glVertex3f(1.0, 1.0, 0.0)
		glVertex3f(1.0, -1.0, 0.0)
		glVertex3f(-1.0, -1.0, 0.0)
		glEnd()
		glutSwapBuffers()						# 交換快取
	def InitGL(self, width, height):					# OpenGL起始化函數
		glClearColor(0.0, 0.0, 0.0, 0.0)				# 設為黑色背景 
		glClearDepth(1.0)						# 設定深度快取
		glDepthFunc(GL_LESS)						# 設定深度測試型態
		glEnable(GL_DEPTH_TEST)						# 容許深度測試
		glShadeModel(GL_SMOOTH)						# 啟動平順陰影
		glMatrixMode(GL_PROJECTION)					# 設定觀察矩陣
		glLoadIdentity()						# 重設觀察矩陣
		gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)	# 計算螢幕高寬比
		glMatrixMode(GL_MODELVIEW)					# 設定觀察矩陣
	def MainLoop(self):							# 進入訊息循環
		glutMainLoop()
window = OpenGLWindow()								# 建立視窗
window.MainLoop()								# 進入訊息循環
