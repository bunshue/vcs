import turtle
import random

#一大堆turtle範例

import sys

import turtle as tu

print('------------------------------------------------------------')	#60個
'''
pos_list = list()
print("請問要畫幾邊形？")
n = 7
tu.color('red')
tu.speed(8)
tu.penup()
tu.goto(0,-200)
for i in range(n):
    tu.left(360//n)
    tu.forward(100)
    pos_list.append(tu.pos())
for i in range(len(pos_list)):
    for point in pos_list:
        tu.penup()
        tu.goto(pos_list[i])
        tu.pendown()
        tu.goto(point)
tu.done()

print('------------------------------------------------------------')	#60個

tu.speed(0)
tu.color('blue')
tu.pensize(3)
for i in range(150):
    tu.left(i//10)
    tu.forward(6)
tu.penup()
tu.home()
tu.pendown()
for i in range(150):
    tu.right(i//10)
    tu.forward(6)
tu.penup()
tu.home()
tu.pendown()
for i in range(150):
    tu.right(i//10)
    tu.backward(6)
tu.penup()
tu.home()
tu.pendown()
for i in range(150):
    tu.left(i//10)
    tu.backward(6)
tu.done()
'''
print('------------------------------------------------------------')	#60個

import math

tu.speed(8)
tu.penup()
tu.goto(-200,0)
tu.pendown()
for d in range(0, 361, 5):
    tu.goto(d-200, 100*math.sin(d*math.pi/180))
tu.done()

print('------------------------------------------------------------')	#60個

import math

tu.speed(8)
tu.pensize(3)
tu.penup()
tu.goto(-200,0)
tu.color('red')
tu.pendown()
for d in range(0, 361, 5):
    tu.goto(d-200, 100*math.sin(d*math.pi/180))
tu.penup()
tu.goto(-200,100)
tu.color('blue')
tu.pendown()
for d in range(0, 361, 5):
    tu.goto(d-200, 100*math.cos(d*math.pi/180))
tu.done()

print('------------------------------------------------------------')	#60個

import math

tu.speed(8)

tu.pensize(3)
tu.penup()
tu.goto(150,0)
tu.color('red')
tu.pendown()
for d in range(0, 361, 2):
    x = 150*math.cos(3*d*math.pi/180)
    y = 150*math.sin(7*d*math.pi/180)
    tu.goto(x, y)
tu.done()

print('------------------------------------------------------------')	#60個

import math

def th(degree):
    return degree*math.pi/180

r = 100
tu.speed(8)
tu.pensize(3)
tu.penup()
tu.color('red')
for d in range(0, 361, 2):
    x = 2*r*(math.cos(th(d)) - 0.5 * math.cos(2*th(d)))
    y = 2*r*(math.sin(th(d)) - 0.5 * math.sin(2*th(d)))
    if d:
        tu.pendown()
    tu.goto(x, y)
tu.done()

print('------------------------------------------------------------')	#60個

import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Richard's pygame!")
bk = pg.Surface(screen.get_size())
bk.fill((255,255,255))
screen.blit(bk, (0,0))
pg.display.update()
quit = False
while not quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit = True
pg.quit()

print('------------------------------------------------------------')	#60個

import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Richard's pygame!")
bk = pg.Surface(screen.get_size())
bk.fill((255,255,255))
pg.draw.rect(bk, (255, 0, 0), (100, 100, 300, 300), 2)
screen.blit(bk, (0,0))
pg.display.update()
quit = False
while not quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit = True
pg.quit()

print('------------------------------------------------------------')	#60個

import random
import pygame as pg
import math

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Richard's pygame!")
bk = pg.Surface(screen.get_size())
bk.fill((255,255,255))
lines = list()
for th in range(0, 361):
    y = 250 - 200 * math.sin(th*math.pi/180)   
    lines.append((th+140, y))
pg.draw.lines(bk, (0, 0, 255), False, lines, 2)
    
screen.blit(bk, (0,0))
pg.display.update()
quit = False
while not quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit = True
pg.quit()

print('------------------------------------------------------------')	#60個

