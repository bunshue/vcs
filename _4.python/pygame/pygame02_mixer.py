"""
Python 聲音處理 pygame

mixer	用來播放聲音

用 pygame 播放 mp3 檔案
用 pygame 播放 wav 檔案
用 pygame 播放 midi 檔案
"""

import sys
import time
import math
import random
import pygame


# 播放mp3
def play_audio_file(filename):
    from pygame import mixer

    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():
        continue

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():#讀取播放狀態, True:正在播放, False:不在播放中
    pygame.time.delay(10)  # msec
    print('.')

print('結束播放')

"""


"""

#要能夠順利讀取各種奇怪的檔名中日文字

print("測試寫檔")
mp3_foldername1 = 'D:/_git/vcs/_1.data/______test_files1/_mp3/'
mp3_foldername2 = 'D:/vcs/astro/_DATA2/_mp3/陳一郎_台語精選集6CD/disc2/'
mp3_foldername3 = 'D:/vcs/astro/_DATA2/_mp3/japanese/昭和の歌--演歌系列9/'
mp3_foldername4 = 'D:/vcs/astro/_DATA2/_________整理_mp3/_mp3_日本_new/(アルバム)演歌 八代亜紀 -[全曲集(Disc1-2)](全24曲)/渕_辙 - [葢轿瘅(Disc1)]'
mp3_foldername5 = 'D:/vcs/astro/_DATA2/_mp3/japanese/美空ひばり(美空云雀).-.[美空ひばり全曲集1].专辑.(MP3)/'

mp3_foldernames = [mp3_foldername1, mp3_foldername2, mp3_foldername3, mp3_foldername4, mp3_foldername5]

print(mp3_foldernames)

filename = "tk_ex_MusicPlayer1.txt"

print("檔名 :", filename)
with open(filename, "w", encoding="utf-8") as f:
    for _ in mp3_foldernames:
        f.write(_)
        f.write("\n")

print("測試讀檔")
filename = "tk_ex_MusicPlayer1.txt"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

"""

import pygame
import time

pygame.init()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption("my mp3 player")

filename = "D:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"

pygame.mixer.music.load(filename)  # 載入音樂
# 音樂可以是ogg、mp3、wav等格式
# 載入的音樂不會全部放到內容中，而是以流的形式播放的，即在播放的時候才會一點點從文件中讀取

pygame.mixer.music.play()  # 播放載入的音樂
# 該函數立即返回，音樂播放在后臺進行。play方法還可以使用兩個參數
# 如果音樂已經播放，它就會重新啟動
# play(loops=0, start=0.0) -> None
# 參數1:控制音樂播放的次數。播放(5)將使音樂播放一次，然后重復5次，總共是6次。如果循環是-1，那么音樂就會無限重復
# 起始位置的參數控制著歌曲開始播放的地方。起始位置取決于音樂演奏的格式。MP3和OGG以時間為單位(以秒為單位)。MOD音樂是模式的序號。如果不能設置起始位置，通過一個startpos將會拋出一個NotImplementedError


time.sleep(5)

pygame.mixer.music.load(filename)  # 如果一個音樂流已經播放，它就會被停止。這并不是音樂的開始
pygame.mixer.music.play()  # 播放載入的音樂


pygame.mixer.music.set_endevent(pygame.KEYDOWN)  # 當播放停止時，音樂會發送一個事件
# 參數：事件
# 每次音樂結束時，這個事件都會被排隊，而不僅僅是第一次[只要不在播放狀態，會一直發送]。為了防止事件被排隊，請調用這個方法，沒有參數

b = pygame.mixer.music.get_endevent()  # 當播放停止時，獲取set_endevent發送的事件--int
# pygame.KEYDOWN=2
# 如果沒有endevent，函數將返回pygame.NOEVENT

print("xxxxxxx", b)

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        print("aaaaa")
        exit()
        print("bbbbb")
    # print('aaaaaa',event)
    pygame.display.update()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
if not mixer.music.get_busy():
    mixer.music.load(playsong)
    mixer.music.play(loops=-1)
else:
    mixer.music.unpause()

mixer.music.load(playsong)
mixer.music.play(loops=-1)

msg.set("\n停止播放")
msg.set("\n正在播放：{}".format(playsong))


win.destroy()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import pygame
import time

# 播放音樂

# pygame.init()

filename = "data/hit.wav"
filename = "D:/_git/vcs/_1.data/______test_files1/_wav/harumi99.wav"

pygame.mixer.init()

# 用 mixer.Sound
# soundhit = pygame.mixer.Sound(filename)
# soundhit.play()

# 用 music.load
pygame.mixer.music.load(filename)

# print("設定音量 0.5")
pygame.mixer.music.set_volume(0.5)  # 設定音量 0.0~1.0

pygame.mixer.music.play()  # 單次播放

# pygame.mixer.music.play(-1)  # 循環播放
# pygame.mixer.music.play(-1, 0.0)  # 循環播放

a = 0
running = True
while running:
    # print(a)
    time.sleep(1)  # 1秒
    status = pygame.mixer.music.get_busy()  # 檢查音樂流是否在播放
    if status == False:
        print("播放完畢")
        running = False
    volume = pygame.mixer.music.get_volume()  # 返回當前音量 0.0~1.0
    # print(volume)
    a += 1
    if a >= 20:
        a = 0


"""
pygame.mixer.music.rewind()  # 重新啟動音樂 # 將當前音樂的播放重新設置為一開始
pygame.mixer.music.stop()  # 停止播放
pygame.mixer.music.pause()  # 暫停播放
pygame.mixer.music.unpause()  # 恢復暫停音樂

status = pygame.mixer.music.get_busy()  # 檢查音樂流是否在播放
# 當音樂流在積極播放時，就會返回True。當音樂空閑時，返回False
# 暫停相當于在播放，返回True

b = pygame.mixer.get_init()  # 測試混音器是否初始化
# 如果混音器已初始化，則返回正在使用的播放參數。如果混音器尚未初始化，則返回None
# get_init() -> (frequency, format, channels)
# (22050, -16, 2)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Load music and sound
coinSound = pygame.mixer.Sound("data/coin.wav")
coinSound.play()

pygame.mixer.music.load("data/music.mp3")
pygame.mixer.music.play(-1)  # 循環播放
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------")  # 30個


'''

# ------------------------------------------------------------  # 60個

Pygame | 1 - 窗口的显示

前言
对于开发一个游戏来说，窗口的显示肯定是前提中的前提，对于pygame来说，只需要一小段代码就可以初始化窗口。

例如：

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

即完成窗口的初始化。

我们这里调用了一个set_mode函数，set_mode：返回一个Surface对象，代表了桌面上出现的窗口。第一个参数代表分辨率；第二个参数是标志位，如果不需要使用任何特性，则指定为0；第三个为色深。

关于标志位的说明如下：

标志位	功能
FULLSCREEN	创建一个全屏窗口 （create a fullscreen display）
DOUBLEBUF	创建一个“双缓冲”窗口，建议在HWSURFACE或者OPENGL时使用（recommended for HWSURFACE or OPENGL）
HWSURFACE	创建一个硬件加速的窗口，必须和FULLSCREEN同时使用（hardware accelerated, only in FULLSCREEN）
OPENGL	创建一个OPENGL渲染的窗口 （create an OpenGL-renderable display）
RESIZABLE	创建一个可以改变大小的窗口 （display window should be sizeable）
NOFRAME	创建一个没有边框的窗口 （display window will have no border or controls）

改变窗口尺寸的代码实现
pygame的默认显示窗口是不支持拖动边框改变大小的，改变set_mode函数的参数后可以实现。以下展示一个可运行实例：

import pygame
# 下面这个是导入所有的key参数
from pygame.locals import *
from sys import exit

background_image = '../image/sushiplate.jpg'
SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

background = pygame.image.load(background_image).convert()

while True:
	event = pygame.event.wait()
	if event.type == QUIT:
		exit()
	if event.type == VIDEORESIZE:
		SCREEN_SIZE = event.size
		screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
		pygame.display.set_caption("Window resized to " + str(event.size))

    # 这里需要重新填满窗口
	screen_width, screen_height = SCREEN_SIZE
	for y in range(0, screen_height, background.get_height()):
		for x in range(0, screen_width, background.get_width()):
			screen.blit(background, (x, y))

pygame.display.update()

VIDEORESIZE 事件，它包含如下内容：
size — 一个二维元组，值为更改后的窗口尺寸，size[0]为宽，size[1]为高
w — 宽
h — 高

其他
如果想使用复合模式，可以加一个“|”

比如：screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | FULLSCREEN, 32)

当使用OPENGL时，不能使用pygame.display.update()来更新窗口，而是pygame.display.flip()。

如果要更深刻地进行学习该部分的话可以去官网查询相关词条。

# ------------------------------------------------------------  # 60個

Pygame | 2 - 事件

定义
Pygame会接受用户的各种操作（比如按键盘，移动鼠标等）产生事件。事件随时可能发生，而且量也可能会很大，Pygame的做法是把一系列的事件存放一个队列里，逐个的处理。

处理事件
pygame.event.get()
pygame.event.wait() —— pygame会等到发生一个时间才继续下去
pygame.event.poll() —— 一旦调用，它会根据现在的情形返回一个真实的事件，或者一个“什么都没有”

事件集
事件	产生途径	参数	详细描述
QUIT	用户按下关闭按钮	none	 
ATIVEEVENT	Pygame被激活或者隐藏	gain, state	 
KEYDOWN	键盘被按下	unicode, key, mod	key – 按下或者放开的键值，是一个数字，Pygame中可以使用K_xxx来表示，比如字母a就是K_a，还有K_SPACE和K_RETURN等。 mod – 包含了组合键信息，如果mod & KMOD_CTRL是真的话，表示用户同时按下了Ctrl键。类似的还有KMOD_SHIFT，KMOD_ALT。 unicode – 代表了按下键的Unicode值
KEYUP	键盘被放开	key, mod	 
MOUSEMOTION	鼠标移动	pos, rel, buttons	buttons – 一个含有三个数字的元组，三个值分别代表左键、中键和右键，1就是按下了 pos – 位置 rel – 代表了现在距离上次产生鼠标事件时的距离
MOUSEBUTTONDOWN	鼠标按下	pos, button	button – 这个值代表了哪个按键被操作 pos – 位置
MOUSEBUTTONUP	鼠标放开	pos, button	button – 这个值代表了哪个按键被操作 pos – 位置
JOYAXISMOTION	游戏手柄(Joystick or pad)移动	joy, axis, value	 
JOYBALLMOTION	游戏球(Joy ball)?移动	joy, axis, value	 
JOYHATMOTION	游戏手柄(Joystick)?移动	joy, axis, value	 
JOYBUTTONDOWN	游戏手柄按下	joy, button	 
JOYBUTTONUP	游戏手柄放开	joy, button	 
VIDEORESIZE	Pygame窗口缩放	size, w, h	 
VIDEOEXPOSE	Pygame窗口部分公开(expose)?	none	 
USEREVENT	触发了一个用户事件	code	 

事件过滤
并不是所有的事件都需要处理。我们使用**pygame.event.set_blocked(type )来完成。如果有好多事件需要过滤，可以传递一个列表，比如pygame.event.set_blocked([KEYDOWN, KEYUP])，如果你设置参数None，那么所有的事件有被打开了。与之相对的，我们使用pygame.event.set_allowed()**来设定允许的事件。

产生事件
通常玩家做什么，Pygame就产生对应的事件就可以了，不过有的时候我们需要模拟出一些事件来，比如录像回放的时候，我们就要把用户的操作再现一遍。

为了产生事件，必须先造一个出来，然后再传递它

y_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=' ')

你也可以像下面这样写

my_event = pygame.event.Event(KEYDOWN, {"key":K_SPACE, "mod":0, "unicode":' '})
pygame.event.post(my_event)

tips：
Event():Event(type, dict) 或者 Event(type, **attributes)。
post(): 把新的事件放在事件队列的最后。

# ------------------------------------------------------------  # 60個

Pygame | 3 - 字体

创建font对象
Pygame可以直接调用系统字体，或者也可以使用TTF字体。

函数：SysFont(name, size, bold=False, italic=False)
my_font = pygame.font.SysFont("arial ", 16)

第一个参数是字体名，第二个是大小。该函数返回一个系统字体，这个字体与“bold”和“italic”两个flag相匹配。如果找不到，就会使用pygame的默认字体。可以使用**pygame.font.get_fonts()**来获得当前系统所有可用字体。

函数：Font(filename, size) 或者 Font(object, size)
my_font = pygame.font.Font("simsun.ttf", 16)

使用这个方法，需要把字体文件 随同游戏一起发送，这样可以避免使用者机器上没有所需的字体（TTF字体集），注意最后要将字体的名称改为英文，也就是说路径中不能有中文。

使用字体
函数：render(text , antialias, color, background=None)
text_surface = my_font.render("Pygame is cool!", True, (0,0,0), (255, 255, 255))

第一个参数文字；第二个参数是个布尔值，表示是否开启抗锯齿，如果为True，字体会比较平滑，不过相应的速度有一点点影响；第三个参数是字体的颜色；第四个是背景色，如果你想没有背景色（也就是透明），就不加这第四个参数。

案例
import pygame
om pygame.locals import *
from sys import exit

if name == "main":
pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
# font = pygame.font.Font('./ttf/font.ttf',16) #*.ttf是自己命名的TTF文件
font_height = font.get_linesize()
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))
    #获得时间的名称
    event_text = event_text[int(-SCREEN_SIZE[1]/font_height):]
    #这个切片操作保证了event_text里面只保留一个屏幕的文字

    if event.type == QUIT:
        exit()

    screen.fill((255, 255, 255))

    y = SCREEN_SIZE[1]-font_height
    #找一个合适的起笔位置，最下面开始但是要留一行的空
    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y))
        #以后会讲
        y-=font_height
        #把笔提一行

    pygame.display.update()

原文链接 ：https://blog.csdn.net/Hubz131/article/details/86740969

# ------------------------------------------------------------  # 60個


Pygame | 4 - 图像

图像数据在Pygame需要被导入，并转化成一个对象储存，想要处理或者调用，就直接调用该对象即可

convert: 将图像转化为Surface对象，每次加载完图像后就要使用这个函数.
例如：

background = pygame.image.load(background_image).convert()
screen.blit(background, (0, 0))  # 画上背景图

convert_alpha：相比convert，保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状。可以试试不用convert_alpha()生成的效果。
例如：

x, y = pygame.mouse.get_pos()  # 获得鼠标位置
# 计算光标左上角位置
x -= mouse_cursor.get_width()/2
y -= mouse_cursor.get_height()/2
# 画上光标
screen.blit(mouse_cursor, (x, y))

blit方法
之前我们一直有调用一个blit方法，效果即在屏幕上加载我们的surface

blit(source, dest, area=None, special_flags = 0)

第一个参数为一个Surface对象，第二个为左上角位置。画完以后得用update更新，否则画面一片漆黑。
dest可以为一个点，也可以是一个矩形，但只有矩形的左上角会被使用，矩形的大小不会造成影响。
area参数可以指定源图像中的一部分被画到目标位置。
图像的管理方法
除了上面说的pygame.image.load外，还可以指定尺寸创建一个空的surface。

>>> a = pygame.Surface((256,256))

这个Surface对象是全黑的。除了大小外，Surface函数还有flags和depth两个参数。

HWSURFACE – creates the image in video memory
SRCALPHA – the pixel format will include a per-pixel alpha。（创建有Alpha通道的surface，选择这个选项需要depth为32。）
alpha_surface = pygame.Surface((256,256), flags=SRCALPHA, depth=32)

矩形对象(Rectangle  Objects)
pygame中有Rect类 ，用来存储和处理矩形对象（包含在pygame.locals）中。这是一个很重要的类，rect对象和surface对象构成了pygame基本的游戏设计要素，之后的一系列游戏效果一般都要通过这两个类来实现。

Rect(left, top, width, height)
Rect((left, top), (width, height))
有了Rect对象之后，可以对其做很多操作，例如调整大小、位置，判断一个点是否在其中等。

剪裁（Clipping）
surface中有裁剪区域（clip area），是一个矩形，定义了哪部分会被绘制，即若定义了这个区域，只有这个区域内的像素会被修改。

set_clip(screen_rect=None): 设定区域，当参数为None时，重置。一个surface对象默认的剪裁区域为这个surface。
get_clip() : 得到剪裁区域，返回一个Rect对象。
子表面（Subsurfaces）
Subsurfaces是在一个surface中再提取出一个surface。当在subsurface上操作时，同时也向父表面上操作。这可以用来绘制图形文字，比如把文字变成多种颜色。把整张图读入后，用subsurface将每个字分隔开。

my_font_image = Pygame.load("font.png")
letters = []
letters["a"] = my_font_image.subsurface((0,0), (80,80))
letters["b"] = my_font_image.subsurface((80,0), (80,80))

填充
fill(color, rect=None, special_flags=0)

当rect参数为默认参数时，整个surface都会被填充。color参数可以为RGB或者RGBA。如果使用RGBA，除非surface有alpha通道（使用了SRCALPHA flag），否则RGBA的Alpha会被忽略。

设置Surface的像素
set_at((x, y), Color) : 设置单个像素的颜色
get_at((x, y)) : 得到单个像素的颜色
下面是对像素进行操作的一个代码实例：

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))

    # screen.lock)()
    for _ in range(100):
        rand_pos = (randint(0, 639), randint(0, 479))
        screen.set_at(rand_pos, rand_col)
    # screen.unlock()
    pygame.display.update()

图像的缩放
def scale(surface: Surface, size: Union[Tuple[int, int], List[int]], dest_surface: Optional [Surface]=None)

scale(Surface, (width, height), DestSurface = None) -> Surface resize to new resolution

将Surface属性的self.image转化为30×30的大小

self.image = pygame.transform .scale(self.image, (30, 30))

锁定Surface
当对像素进行读或写操作时，surface会被锁定。一个锁定的surface，经常不能被显示或被pygame操作。所以除非必要，在手动lock之后不要忘了unlock。

所有pygame的函数如过需要锁定和解锁，这些操作时自动发生的。如果不想发生自动的lock和unlock（有些时候为了提高效率），可以在一些会造成自动锁定和解锁的语句前后注释掉这两句。

# ------------------------------------------------------------  # 60個

Pygame | 5 - 绘制图形

有时候我们没必要为了一些关卡的小障碍额外再去做一张贴图，这个时候进行内部图像的绘制就是一个性价比很高的选择。

pygame使用pygame.draw来绘制图形。其包含以下几种函数。

函数	作用	用法
rect	绘制矩形	rect(Surface, color, Rect, width=0)
polygon	绘制多边形	polygon(Surface, color, pointlist, width=0)
circle	绘制圆	circle(Surface, color, pos, radius, width=0)
ellipse	绘制椭圆	ellipse(Surface, color, Rect, width=0)
arc	绘制圆弧	arc(Surface, color, Rect, start_angle, stop_angle, width=1)
line	绘制线	line(Surface, color, start_pos, end_pos, width=1)
lines	绘制一系列的线	lines(Surface, color, closed, pointlist, width=1)
aaline	绘制一根平滑的线	aaline(Surface, color, startpos, endpos, blend=1)
aalines	绘制一系列平滑的线	aalines(Surface, color, closed, pointlist, blend=1)

width参数：width参数为0或省略，1则填充。
画填充的矩形，有另一个方法Surface.fill()，事实上，这种方法速度更快。
lines函数的closed为一个布尔变量，如果closed为真，则会画一条连接第一个和最后一个点的线，是整个图形闭合
pygame.draw
Pygame 中绘制图形的模块。

该模块用于在 Surface 对象上绘制一些简单的形状。这些函数将渲染到任何格式的 Surface 对象上。硬件渲染会比普通的软件渲染更耗时。

大部分函数用 width 参数指定图形边框的大小，如果 width = 0 则表示填充整个图形。

所有的绘图函数仅能在 Surface 对象的剪切区域生效。这些函数返回一个 Rect，表示包含实际绘制图形的矩形区域。

大部分函数都有一个 color 参数，传入一个表示 RGB 颜色值的三元组，当然也支持 RGBA 四元组。其中的 A 是 Alpha 的意思，用于控制透明度。不过该模块的函数并不会绘制透明度，而是直接传入到对应 Surface  对象的 pixel alphas 中。color 参数也可以是已经映射到 Surface  对象的像素格式中的整型像素值。

当这些函数在绘制时，必须暂时锁定 Surface  对象。许多连续绘制的函数可以通过一次性锁定直到画完再解锁来提高效率。

函数详解
pygame.draw.rect()
绘制矩形 。

rect(Surface, color, Rect, width=0) -> Rect

在 Surface  对象上绘制一个矩形。Rect 参数指定矩形的位置和尺寸。width 参数指定边框的宽度，如果设置为 0 则表示填充该矩形。

pygame.draw.polygon()
绘制多边形。

polygon(Surface, color, pointlist, width=0) -> Rect

在 Surface  对象上绘制一个多边形。pointlist 参数指定多边形的各个顶点。width 参数指定边框的宽度，如果设置为 0 则表示填充该矩形。

绘制一个抗锯齿的多边形，只需要将 aalines() 的 closed 参数设置为 True 即可。

pygame.draw.circle()
根据圆心和半径绘制圆形。

circle(Surface, color, pos, radius, width=0) -> Rect

在 Surface  对象上绘制一个圆形。pos 参数指定圆心的位置，radius 参数指定圆的半径。width 参数指定边框的宽度，如果设置为 0 则表示填充该矩形。

pygame.draw.ellipse()
根据限定矩形绘制一个椭圆形。

ellipse(Surface, color, Rect, width=0) -> Rect

在 Surface  对象上绘制一个椭圆形。Rect 参数指定椭圆外围的限定矩形。width 参数指定边框的宽度，如果设置为 0 则表示填充该矩形。

pygame.draw.arc()
绘制弧线。

arc(Surface, color, Rect, start_angle, stop_angle, width=1) -> Rect

在 Surface  对象上绘制一条弧线。Rect 参数指定弧线所在的椭圆外围的限定矩形。两个 angle 参数指定弧线的开始和结束位置。width 参数指定边框的宽度。

pygame.draw.line()
绘制线段。

line(Surface, color, start_pos, end_pos, width=1) -> Rect

在 Surface  对象上绘制一条线段。两端以方形结束。

pygame.draw.lines()
绘制多条连续的线段。

lines(Surface, color, closed, pointlist, width=1) -> Rect

在 Surface  对象上绘制一系列连续的线段。pointlist 参数是一系列短点。如果 closed 参数设置为 True，则绘制首尾相连。

pygame.draw.aaline()
绘制抗锯齿的线段。

aaline(Surface, color, startpos, endpos, blend=1) -> Rect

在 Surface  对象上绘制一条抗锯齿的线段。blend 参数指定是否通过绘制混合背景的阴影来实现抗锯齿功能。该函数的结束位置允许使用浮点数。

pygame.draw.aalines()
绘制多条连续的线段（抗锯齿）。

aalines(Surface, color, closed, pointlist, blend=1) -> Rect

在 Surface  对象上绘制一系列连续的线段（抗锯齿）。如果 closed 参数为 True，则首尾相连。blend 参数指定是否通过绘制混合背景的阴影来实现抗锯齿功能。该函数的结束位置允许使用浮点数。

# ------------------------------------------------------------  # 60個

Pygame | 6 - 运动

直线运动
实现方式相当简单，其实就是用bilt函数不停地该变坐标即可，比如

# sprite的起始坐标
x = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))
    x += 1

    if x>640:
        x = 0

    pygame.display.update()

控制帧率
在上面的程序中，帧率是很高的。而且电脑的性能不同，鱼的速度就会不同，如果动画的的元素很多，速度就会下降。

为了解决这个问题，可以使用pygame的时间模块。

clock = pygame.time.Clock()

time_passed = clock.tick()

time_passed = clock.tick(30)

第一行初始化了一个Clock对象。第二行返回了距上一次调用这个函数，过去了多长时间（注意，得到的值是以毫秒为单位的）。第三行，在函数中添加了framerate参数，这个函数会延时使得游戏的帧率不会超过给定值。

给定的值仅仅是最大帧率，当动作复杂或机器性能不足时，实际帧率无法达到这个值，需要一种手段控制动画效果。比如给物体一个恒定的速度，再通过时间，计算出移动的距离。

斜线运动

这个原理也很简单，做一个触边速度变更的逻辑判断即可

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed/1000
    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds

    # 到达边界后速度反向
    if x > 640 - sprite.get_width():
        speed_x = -speed_x
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0

    if y > 480 - sprite.get_height():
        speed_y = -speed_y
        y = 480 - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0

    pygame.display.update()

为了代码优雅，可以使用向量来完成上述目标，不过这可能需要自己码一个模块来完成这个目标。

# ------------------------------------------------------------  # 60個

Pygame | 7 - 键盘输入

在之前的例子中使用过键盘输入，使用pygame.event.get()获取所有事件，当event.type ==KEYDOWN时，再判断event.key的种类。也可以使用pygame.key.get_pressed()来获取所有按下的键值，它会返回一个元组，这个元祖的索引就是键值，对应的值为True就是按下。

但是，如果要处理文本输入，这个函数不是正确的方法。因为我们不知道按键被按下的顺序。

key模块下还有如下的函数：

key.get_focused —— 返回当前的pygame窗口是否激活
key.get_mods —— 按下的组合键（Alt, Ctrl, Shift）
key.set_mods —— 你也可以模拟按下组合键的效果（KMOD_ALT, KMOD_CTRL, KMOD_SHIFT）
例子：if pygame.key.get_mods() & KMOD_SHIFT:

key.set_repeat —— 参数为（delay，interval）。当有参数时，即repeat被激活时，被按住的键会产生多次KEYDOWN事件。第一次发送KEYDOWN事件后，经过delay时间（ms）发送第二次，然后每隔interval时间（ms）发送一次事件。如果没有参数，不产生重复按键事件。当pygame初始化之后，重复按键默认为disabled
key.name —— 接受键值返回键名
该模块包含处理与键盘操作相关的函数。当键盘按键被按下和释放时，事件队列将获得 pygame.KEYDOWN 和 pygame.KEYUP 事件消息。这两个消息均包含 key 属性，是一个整数的 id，代表键盘上具体的某个按键。

pygame.KYEDOWN 事件还有个额外的属性 unicode 和 scancode。unicode 代表一个按键翻译后的 Unicode 编码，这包含 shift 按键和组合键。scancode 是扫描码，不同键盘间该值可能不同。不过这对于特殊按键像多媒体键的选择是有用的。

key 属性的值是一个数字，为了方便使用，Pygame 将这些数字定义为以下这些常量：

KeyASCII	ASCII	描述
K_BACKSPACE	\b	退格键（Backspace）
K_TAB	\t	制表键（Tab）
K_CLEAR	 	清楚键（Clear）
K_RETURN	\r	回车键（Enter）
K_PAUSE	 	暂停键 （Pause）
K_ESCAPE	^[	退出键（Escape）
K_SPACE	空格键	（Space）
K_EXCLAIM	!	感叹号（exclaim）
K_QUOTEDBL	"	双引号（quotedbl）
K_HASH	#	井号（hash）
K_DOLLAR	$	美元符号（dollar）
K_AMPERSAND	& and	符号（ampersand）
K_QUOTE	’	单引号（quote）
K_LEFTPAREN	(	左小括号（left parenthesis）
K_RIGHTPAREN	)	右小括号（right parenthesis）
K_ASTERISK	*	星号（asterisk）
K_PLUS	+	加号（plus sign）
K_COMMA	,	逗号（comma）
K_MINUS	-	减号（minus sign）
K_PERIOD	.	句号（period）
K_SLASH	/	正斜杠（forward slash）
K_0	0	0
K_1	1	1
K_2	2	2
K_3	3	3
K_4	4	4
K_5	5	5
K_6	6	6
K_7	7	7
K_8	8	8
K_9	9	9
K_COLON	:	冒号（colon）
K_SEMICOLON	;	分号（semicolon）
K_LESS	<	小于号（less-than sign）
K_EQUALS	=	等于号（equals sign）
K_GREATER	>	大于号（greater-than sign）
K_QUESTION	?	问号（question mark）
K_AT	@	at 符号（at）
K_LEFTBRACKET	[	左中括号（left bracket）
K_BACKSLASH	\	反斜杠（backslash）
K_RIGHTBRACKET	]	右中括号（right bracket）
K_CARET	^	脱字符（caret）
K_UNDERSCORE	_	下划线（underscore）
K_BACKQUOTE	`	重音符（grave）
K_a	a	a
K_b	b	b
K_c	c	c
K_d	d	d
K_e	e	e
K_f	f	f
K_g	g	g
K_h	h	h
K_i	i	i
K_j	j	j
K_k	k	k
K_l	l	l
K_m	m	m
K_n	n	n
K_o	o	o
K_p	p	p
K_q	q	q
K_r	r	r
K_s	s	s
K_t	t	t
K_u	u	u
K_v	v	v
K_w	w	w
K_x	x	x
K_y	y	y
K_z	z	z
K_DELETE	 	删除键（delete）
K_KP0	 	0（小键盘）
K_KP1	 	1（小键盘）
K_KP2	 	2 （小键盘）
K_KP3	 	3（小键盘）
K_KP4	 	4（小键盘）
K_KP5	 	5 （小键盘）
K_KP6	 	6 （小键盘）
K_KP7	 	7 （小键盘）
K_KP8	 	8 （小键盘）
K_KP9	 	9 （小键盘）
K_KP_PERIOD	.	句号（小键盘）
K_KP_DIVIDE	/	除号（小键盘）
K_KP_MULTIPLY	*	乘号（小键盘）
K_KP_MINUS	-	减号（小键盘）
K_KP_PLUS	+	加号（小键盘）
K_KP_ENTER	\r	回车键（小键盘）
K_KP_EQUALS	=	等于号（小键盘）
K_UP	 	向上箭头（up arrow）
K_DOWN	 	向下箭头（down arrow）
K_RIGHT	 	向右箭头（right arrow）
K_LEFT	 	向左箭头（left arrow）
K_INSERT	 	插入符（insert）
K_HOME	 	Home 键（home）
K_END	 	End 键（end）
K_PAGEUP	 	上一页（page up）
K_PAGEDOWN	 	下一页（page down）
K_F1	 	F1
K_F2	 	F2
K_F3	 	F3
K_F4	 	F4
K_F5	 	F5
K_F6	 	F6
K_F7	 	F7
K_F8	 	F8
K_F9	 	F9
K_F10	 	F10
K_F11	 	F11
K_F12	 	F12
K_F13	 	F13
K_F14	 	F14
K_F15	 	F15
K_NUMLOCK	 	数字键盘锁定键（numlock）
K_CAPSLOCK	 	大写字母锁定键（capslock）
K_SCROLLOCK	 	滚动锁定键（scrollock）
K_RSHIFT	 	右边的 shift 键（right shift）
K_LSHIFT	 	左边的 shift 键（left shift）
K_RCTRL	 	右边的 ctrl 键（right ctrl）
K_LCTRL	 	左边的 ctrl 键（left ctrl）
K_RALT	 	右边的 alt 键（right alt）
K_LALT	 	左边的 alt 键（left alt）
K_RMETA	 	右边的元键（right meta）
K_LMETA	 	左边的元键（left meta）
K_LSUPER	 	左边的 Window 键（left windows key）
K_RSUPER	 	右边的 Window 键（right windows key）
K_MODE	 	模式转换键（mode shift）
K_HELP	 	帮助键（help）
K_PRINT	 	打印屏幕键（print screen）
K_SYSREQ	 	魔术键（sysrq）
K_BREAK	 	中断键（break）
K_MENU	 	菜单键（menu）
K_POWER	 	电源键（power）
K_EURO	 	欧元符号（euro）
以下是组合键的常量定义：

KeyASCII	描述
KMOD_NONE	木有同时按下组合键
KMOD_LSHIFT	同时按下左边的 shift 键
KMOD_RSHIFT	同时按下右边的 shift 键
KMOD_SHIFT	同时按下 shift 键
KMOD_CAPS	同时按下大写字母锁定键
KMOD_LCTRL	同时按下左边的 ctrl 键
KMOD_RCTRL	同时按下右边的 ctrl 键
KMOD_CTRL	同时按下 ctrl 键
KMOD_LALT	同时按下左边的 alt 键
KMOD_RALT	同时按下右边的 alt 键
KMOD_ALT 同时按下	alt 键
KMOD_LMETA	同时按下左边的元键
KMOD_RMETA	同时按下右边的元键
KMOD_META	同时按下元键
KMOD_NUM	同时按下数字键盘锁定键
KMOD_MODE	同时按下模式转换键\
函数详解
pygame.key.get_focused()

当窗口获得键盘的输入焦点时返回 True。

get_focused() -> bool

当窗口获得键盘的输入焦点时返回 True，如果窗口需要确保不失去键盘焦点，可以使用 pygame.event.set_grab(True) 独占所有的输入接口。

pygame.key.get_pressed()

获取键盘上所有按键的状态。

get_pressed() -> bools

返回一个由布尔类 型值组成的序列，表示键盘上所有按键的当前状态。使用 key 常量作为索引，如果该元素是 True，表示该按键被按下。

使用该函数获取一系列按钮被按下的状态，并不能正确的获取用户输入 的文本。因为你无法知道用户按键的被按下的顺序，并且快速的连续按下键盘可能无法完全被捕获（在两次调用 pygame.key.get_pressed() 的过程中被忽略），也无法将这些按下的按键完全转化为字符值。实现此功能可以通过捕获 pygame.KEYDOWN 事件消息来实现。

pygame.key.get_mods()

检测是否有组合键被按下。

get_mods() -> int

返回一个包含所有组合键位掩码的整数。使用位操作符 & 你可以检测某个组合键是否被按下。

pygame.key.set_mods()

临时设置某些组合键为被按下状态。

set_mods(int) -> None

创建一个位掩码整数，包含你需要设置为被按下状态的组合键。

pygame.key.set_repeat()

控制重复响应持续按下按键的时间。

set_repeat() -> None

set_repeat(delay, interval) -> None

当开启重复响应按键，那么用户持续按下某一按键，就会不断产生同一 pygame.KEYDOWN 事件。delay 参数设置多久后（单位是毫秒）开始发送第一个 pygame.KEYDOWN 事件。interval 参数设置发送两个事件之间的间隔。如果不传入任何参数，表示取消重复响应按键。

pygame.key.get_repeat()

获取重复响应按键的参数。

get_repeat() -> (delay, interval)

当开启重复响应按键，那么用户持续按下某一按键，就会不断产生同一 pygame.KEYDOWN 事件。返回值是一个二元组，第一个元素 delay 表示多久后（单位是毫秒）开始发送第一个 pygame.KEYDOWN 事件。第二个元素 interval 表示发送两个事件之间的间隔。

默认情况下重复响应按键是没有开启的。

Pygame 1.8 新增加的。

pygame.key.name()

获取按键标识符对应的名字。

name(key) -> string

获取一个按键标识符对应的字符串 描述。

# ------------------------------------------------------------  # 60個

Pygame | 8 - 播放音乐
pygame.mixer.music Pygame 中控制音频 流的模块。

函数
pygame.mixer.music.load()  ——  载入一个音乐文件用于播放

pygame.mixer.music.play()  ——  开始播放音乐流

pygame.mixer.music.rewind()  ——  重新开始播放音乐

pygame.mixer.music.stop()  ——  结束音乐播放

pygame.mixer.music.pause()  ——  暂停音乐播放

pygame.mixer.music.unpause()  ——  恢复音乐播放

pygame.mixer.music.fadeout()  ——  淡出的效果结束音乐播放

pygame.mixer.music.set_volume()  ——  设置音量

pygame.mixer.music.get_volume()  ——  获取音量

pygame.mixer.music.get_busy()  ——  检查是否正在播放音乐

pygame.mixer.music.set_pos()  ——  设置播放的位置

pygame.mixer.music.get_pos()  ——  获取播放的位置

pygame.mixer.music.queue()  ——  将一个音乐文件放入队列中，并排在当前播放的音乐之后

pygame.mixer.music.set_endevent()  ——  当播放结束时发出一个事件

pygame.mixer.music.get_endevent()  ——  获取播放结束时发送的事件

Pygame 中播放音乐的模块和 pygame.mixer 模块是密切联系的。使用音乐模块去控制在调音器上的音乐播放。

音乐（music）播放和声音（sound）播放的不同之处在于音乐是流式的，并且绝对不会在一开始就把一个音乐文件全部载入。调音系统在工作刚开始时仅支持单音乐流。

注意：对于 MP3 格式的支持是受限制的。在一些系统上，一种不受支持的格式将会是系统崩溃，例如 Debian Linux。为了游戏的稳定性，建议使用 OGG 进行替代。

函数详解
pygame.mixer.music.load()
载入一个音乐文件用于播放。

load(filename) -> None

load(object) -> None

该函数将会载入一个音乐文件名 或者文件对象，并且准备播放。如果已经有音乐流正在播放，该音乐流将被停止。另外，函数不会开始播放音乐。

pygame.mixer.music.play()
开始播放音乐流。

play(loops=0, start=0.0) -> None

该函数用于播放已载入的音乐流。如果音乐已经开始播放，则将会重新开始播放。

loops 参数控制重复播放的次数，例如 play(5) 意味着被载入的音乐将会立即开始播放 1 次并且再重复 5 次，共 6 次。如果 loops = -1，则表示无限重复播放。

start 参数控制音乐从哪里开始播放。开始的位置取决于音乐的格式。MP3 和 OGG 使用时间表示播放位置（以秒为单位）。MOD使用模式顺序编号表示播放位置。如果音乐文件无法设置开始位置，则传递了start参数后会产生一个NotImplementedError 错误。

pygame.mixer.music.rewind()
重新开始播放音乐。

rewind() -> None

从文件开头开始重新播放音乐。

pygame.mixer.music.stop()
结束音乐播放。

stop() -> None

如果音乐正在播放则立即结束播放。

pygame.mixer.music.pause()
暂停音乐流的播放。

pause() -> None

通过调用 pygame.mixer.music.unpause() 函数继续播放音乐。

pygame.mixer.music.unpause()
恢复音乐播放。

unpause() -> None

在播放暂停后使用该函数可以继续音乐流的播放。

pygame.mixer.music.fadeout()
淡出的效果结束音乐播放。

fadeout(time) -> None

该函数将会在音乐淡出（也就是不在有声音放出）一段指定长度的时间（以毫秒为单位）后结束播放。

注意：该函数在调用后会一直处于阻塞状态，直到音乐已经淡出。

pygame.mixer.music.set_volume()
设置音量。

set_volume(value) -> None

设置音乐的播放音量。

value 参数值范围为 0.0~1.0。当新的音乐文件被载入，音量会被重置。

pygame.mixer.music.get_volume()
获取音量。

get_volume() -> value

返回正在播放的音乐的音量（此音量应该是调音器音量，注意与其他音量参数区分）。返回值范围为 0.0~1.0。

pygame.mixer.music.get_busy()
检查是否正在播放音乐。

get_busy() -> bool

如果有音乐流正在播放，此方法返回 True。否则返回 False。

pygame.mixer.music.set_pos()
设置播放的位置。

set_pos(pos) -> None

设置播放的起始位置。pos 参数是一个浮点数（或者一个可以转换为浮点数的数值），其值取决于音乐文件的格式：

对于 MOD 文件，它是模块中的整型模式号；

对于 OGG 文件，它是一个以音频开头为零点的绝对时间值（以秒为单位）；

对于 MP3 文件，它是以当前播放位置为零点的绝对时间值（以秒为单位）。

为了对一个 MP3 文件的进行绝对定位，建议首先调用 rewind() 函数（其他文件格式不受支持）。SDL_mixer 更新的版本提供了更好的定位支持。如果一种特殊的格式不支持定位，将会产生一个 SDLError 错误。

该函数会调用 SDL_mixer 内的 Mix_SetMusicPosition() 函数。

pygame.mixer.music.get_pos()
获取播放的位置。

get_pos() -> time

此函数会获得音乐的播放时长（以毫秒为单数的数值）。返回值仅代表已经音乐已经播放了多久，并不考虑任何起始位置偏移量。

pygame.mixer.music.queue()
将一个音乐文件放入队列中，并排在当前播放的音乐之后。

queue(filename) -> None

此函数将会载入一个音乐文件并将其放入队列中。当前的音乐一旦播放完毕，正在排队的音乐文件就会开始播放。如果当前音乐被人为停止或者切换 到其他音乐，则正在排队的音乐会被丢弃。

下面的示例意思是先播放 6 次 Bach 然后再播放 1 次 Mozart：

pygame.mixer.music.load('bach.ogg')

pygame.mixer.music.play(5)        # Plays six times, not five!

pygame.mixer.music.queue('mozart.ogg')

pygame.mixer.music.set_endevent()

当播放结束时发出一个事件。

set_endevent() -> None

set_endevent(type) -> None

调用此函数会使 Pygame 在音乐结束播放后发出信号（通过事件队列）。

type 参数决定了什么样的事件将被放入事件队列中。

任何时候音乐结束，都会放入指定事件到队列中（不仅仅是第一次）。调用该函数并不带任何参数，表示停止投放事件到队列中。

pygame.mixer.music.get_endevent()
获取播放结束时发送的事件。

get_endevent() -> type

返回音乐结束时被放入队列的事件类型。

如果没有指定 endevent 事件，此方法会返回 pygame.NOEVENT

# ------------------------------------------------------------  # 60個

Pygame | 9 - 精灵的初始化与帧更新

Sprite（精灵类）的作用是派生子类，

子类必须在初始化方法中定义图像（image）和位置（rect）的属性。

也就是说，使用Sprite方法是继承这个类，然后重写各种方法。

可以通过复制以下代码，感受一下精灵类如何运行

精灵的初始化

import pygame
from pygame.locals import QUIT

class Plat(pygame.sprite.Sprite):
    def __init__(self, color, initial_position):
        pygame.sprite.Sprite.__init__(self)

        # 这里直接加载一个图片文件
        self.image = pygame.image.load('background.jpg').convert_alpha()
        # 以下数据会保存为一个元组，前两个是绘制的坐标，后两个是图像长与高
        self.rect = 0, 0, 100, 100

# 这样就算基本完成一个精灵类了，之后把它放到屏幕里

pygame.init()
screen = pygame.display.set_mode([800, 600])

b = pygame.sprite.Group()
a = Plat((255,0,0), (100,100))
# 通过组的办法管理精灵，可以直接进行定位和更新
b.add(a)

while True:

    if pygame.event.poll().type == QUIT:
        pygame.quit()
        exit()

    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()
    b.draw(screen)

    pygame.display.update()

帧的更新
精灵序列图
将要加载的动画帧放在一个精灵序列图里面，然后在程序里面调用它。pygame会自动更新动画帧，这样一个动态的图像就会展现在我们面前了。

下面是一个典型的精灵序列图：行和列的索引都是从0开始的。

值得一提的是这不是列表，而是整张图片就是这样的，通过截取不同的区域来实现图片的变化，这就是比较传统的帧数更新方法，也可以使用一系列图片来实现帧更新，不过这可能让缓存 比较慢


加载精灵图序列：
在加载一个精灵图序列的时候，我们需要告知程序一帧的大小，（传入帧的宽度和高度，文件名 ）。

除此之外，还需要告诉精灵类，精灵序列图里面有多少列。load函数可以加载一个精灵序列图。

def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = 0,0,width,height
        self.columns = columns

更新帧
一个循环动画通常是这样工作的：从第一帧不断的加载直到最后一帧，然后在折返回第一帧，并不断重复这个操作。

self.frame += 1

        if self.frame > self.last_frame:
                self.frame = self.first_frame

        self.last_time = current_time

但是如果只是这样做的话，程序会一股脑地将动画播放完了，我们想让它根据时间间隔一张一张的播放，因此加入定时的代码。

pygame中的time模块有一个get_ticks()方法可以满足定时的需要。

ticks = pygame.time.get_ticks()

然后将ticks变量传递给sprite的update函数，这样就可以轻松让动画按照帧速率来播放了。哦，帧速率还没有设置，咱们现在设置一下帧速率。

启动一个定时器 ，然后调用tick（num）函数就可以让游戏以num帧来运行了。

framerate = pygame.time.Clock()

framerate.tick(60)

绘制帧
sprite.draw()方法是用来绘制帧的，但是这个函数是由精灵来自动调用的，我们没有办法重写它，因此需要在update函数里面做一些工作。

首先需要计算单个帧左上角的x，y位置值（x表示列编号，y表示行编号）：

# 用帧数目除以行数，然后在乘上帧的高度，这就能完成索引了

frame_x = (self.frame % self.columns) * self.frame_width

frame_y = (self.frame // self.columns) * self.frame_height

# 然后将计算好的x，y值传递给位置rect属性。

rect = ( frame_x, frame_y, self.frame_width, self.frame_height )

# subsurface返回surface中的一部分，实现了区域截取的方法

self.image = self.master_image.subsurface(rect)

案例
使用图片


import pygame
from pygame.locals import *

class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.topleft = 0,0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = 0,0,width,height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("精灵类测试")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()


cat = MySprite(screen)
cat.load("sprite.png", 100, 100, 4)
group = pygame.sprite.Group()
group.add(cat)

while True:
    framerate.tick(30)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        exit()
        
    screen.fill((0,0,100))

    group.update(ticks)
    group.draw(screen)
    pygame.display.update()

可以深切体会一下作者的代码改写，我感觉十分精彩
原文地址
https://blog.csdn.net/peng__dada/article/details/79156500?ops_request_misc=&request_id=&biz_id=102&utm_term=pygame%20sprite%E8%BF%90%E5%8A%A8&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-2-79156500.first_rank_v2_pc_rank_v29&spm=1018.2226.3001.4187

# ------------------------------------------------------------  # 60個


# ------------------------------------------------------------  # 60個



# ------------------------------------------------------------  # 60個



# ------------------------------------------------------------  # 60個



'''


