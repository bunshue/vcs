# -*- coding:utf-8 -*-
# file: pyOpenGLDraw3D.py
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
class OpenGLWindow:
	def __init__(self, width = 640, height = 480, title = 'PyOpenGL'):	# 起始化
		glutInit(sys.argv)						# 傳遞指令行參數
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)	# 設定顯示模式
		glutInitWindowSize(width, height)				# 設定視窗大小
		self.window = glutCreateWindow(title)				# 建立視窗
		glutDisplayFunc(self.Draw)					# 設定場景繪制函數
		self.InitGL(width, height)					# 呼叫OpenGL起始化函數
	def Draw(self):								# 繪制場景
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)		# 清除螢幕
		glLoadIdentity()						# 重設觀察矩陣
		glTranslatef(1.5,0.0,-7.0)					# 搬移位置
		glRotatef(45,1.0,1.0,1.0)					# 分別繞X，Y，Z軸旋轉45度
		glBegin(GL_QUADS)						# 開始繪制立方體
		glColor3f(1.0,0.0,0.0)						# 設定彩色為紅色
		glVertex3f( 1.0, 1.0,-1.0)					# 繪制立方體的頂面
		glVertex3f(-1.0, 1.0,-1.0)
		glVertex3f(-1.0, 1.0, 1.0)
		glVertex3f( 1.0, 1.0, 1.0)
		glColor3f(0.0,1.0,0.0)						# 設定彩色為綠色
		glVertex3f( 1.0,-1.0, 1.0)
		glVertex3f(-1.0,-1.0, 1.0)
		glVertex3f(-1.0,-1.0,-1.0)
		glVertex3f( 1.0,-1.0,-1.0)
		glColor3f(0.0,0.0,1.0)						# 設定彩色為藍色
		glVertex3f( 1.0, 1.0, 1.0)
		glVertex3f(-1.0, 1.0, 1.0)
		glVertex3f(-1.0,-1.0, 1.0)
		glVertex3f( 1.0,-1.0, 1.0)
		glColor3f(1.0,0.0,0.0)
		glVertex3f( 1.0,-1.0,-1.0)
		glVertex3f(-1.0,-1.0,-1.0)
		glVertex3f(-1.0, 1.0,-1.0)
		glVertex3f( 1.0, 1.0,-1.0)
		glColor3f(0.0,1.0,0.0)
		glVertex3f(-1.0, 1.0, 1.0)
		glVertex3f(-1.0, 1.0,-1.0)
		glVertex3f(-1.0,-1.0,-1.0)
		glVertex3f(-1.0,-1.0, 1.0)
		glColor3f(0.0,0.0,1.0)
		glVertex3f( 1.0, 1.0,-1.0)
		glVertex3f( 1.0, 1.0, 1.0)
		glVertex3f( 1.0,-1.0, 1.0)
		glVertex3f( 1.0,-1.0,-1.0)
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
