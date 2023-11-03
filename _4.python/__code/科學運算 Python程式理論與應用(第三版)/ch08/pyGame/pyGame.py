# -*- coding:utf-8 -*-
# file: pyGame.py
#
import sys 
import pygame
import threading
import random
class Game:										# 建立游戲類別
	def __init__(self):
		pygame.init()								# pygame起始化
		self.screen = pygame.display.set_mode((800,600))			# 設定顯示模式
		pygame.display.set_caption('Python Game')				# 設定視窗標題
		self.image = []								# 圖片清單
		self.imagerect = []							# 圖片大小清單
		self.vs = pygame.image.load('image/vs.gif')				# 載入圖片
		self.o = pygame.image.load('image/o.gif')
		self.p = pygame.image.load('image/p.gif')
		self.u = pygame.image.load('image/u.gif')
		self.title = pygame.image.load('image/title.gif')
		self.start = pygame.image.load('image/start.gif')
		self.exit = pygame.image.load('image/exit.gif')
		for i in range(3):
			gif = pygame.image.load('image/' + str(i) + '.gif')
			self.image.append(gif)
		for i in range(3):							# 處理圖片繪制區域
			image = self.image[i]
			rect = image.get_rect()
			rect.left = 200 * (i+1) + rect.left
			rect.top = 400
			self.imagerect.append(rect)
	def Start(self):								# 繪制游戲起始界面
		self.screen.blit(self.title, (200,100,400,140))				# 繪制游戲名稱
		self.screen.blit(self.start, (350,300,100,50))				# 繪制開始按鈕
		self.screen.blit(self.exit, (350, 400,100,50))				# 繪制離開按鈕
		pygame.display.flip()							# 更新螢幕
		start = 1
		while start:								# 進入訊息循環
			for event in pygame.event.get():				# 處理訊息
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:		# 處理滑鼠點擊訊息
					if self.isStart() == 0:
						start = 0
					elif self.isStart() == 1:
						sys.exit()
					else:
						pass
				else:
					pass
		self.run()								# 開始游戲
	def run(self):									# 開始游戲
		self.screen.fill((0,0,0))
		for i in range(3):							# 繪制圖片
			self.screen.blit(self.image[i], self.imagerect[i])
		pygame.display.flip()							# 更新螢幕進入訊息循環
		while True:
			for event in pygame.event.get():				# 處理訊息
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:		# 處理滑鼠點擊訊息
					self.OnMouseButDown()
				else:
					pass
	def isStart(self):								# 判斷滑鼠點擊的按鈕
		pos = pygame.mouse.get_pos()
		if pos[0] > 350 and pos[0] < 450:
			if pos[1] > 300 and pos[1] < 350:
				return 0
			elif pos[1] > 400 and pos[1] < 450:
				return 1
			else:
				return 2
		else:
			return 2
	def OnMouseButDown(self):							# 處理滑鼠點擊訊息
		self.screen.blit(self.vs, (300, 150, 140, 140))				# 繪制圖片
		pos = pygame.mouse.get_pos()						# 取得滑鼠位置
		if pos[1] > 400 and pos[1] < 540:					# 判斷滑鼠位置繪制對應圖片
			if pos[0] > 200 and pos[0] < 340:
				self.screen.blit(self.image[0], 
						(150 ,150, 140,140))
				self.isWin(0)
			elif pos[0] > 400 and pos[0] < 540:
				self.screen.blit(self.image[1], 
						(150 ,150, 140,140))
				self.isWin(1)
			elif pos[0] > 600 and pos[0] < 740:
				self.screen.blit(self.image[2], 
						(150 ,150, 140,140))
				self.isWin(2)
			else:
				pass
	def isWin(self, value):								# 判斷誰贏
		num = random.randint(0, 2)						# 產生隨機數
		self.screen.blit(self.image[num], 					# 繪制對應圖片
				(450 ,150, 590,240))
		pygame.display.flip()							# 更新螢幕
		if num == value:							# 判斷誰贏
			self.screen.blit(self.o, 
					(220, 10, 140, 70))
			pygame.display.flip()
		elif num < value:
			if num == 0:
				if value == 2:
					self.screen.blit(self.u, 
						(220, 10, 140, 70))
				else:
					self.screen.blit(self.p, 
						(220, 10, 140, 70))
				pygame.display.flip()
			else:
				self.screen.blit(self.u, 
						(220, 10, 140, 70))
				pygame.display.flip()
		else:
			if num == 2:
				if value == 1:
					self.screen.blit(self.u, 
						(220, 10, 140, 70))
				else:
					self.screen.blit(self.p, 
						(220, 10, 140, 70))
				pygame.display.flip()
			else:
				self.screen.blit(self.u, 
						(220, 10, 140, 70))
				pygame.display.flip()
game = Game()
game.Start()
