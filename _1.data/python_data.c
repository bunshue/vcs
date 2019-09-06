
https://www.kancloud.cn/thinkphp/python-guide/39428

http://www.codedata.com.tw/python/python-tutorial-the-1st-class-4-unicode-support-basic-input-output/
http://www.runoob.com/python/python-chinese-encoding.html



pip install numpy	¦w¸ËNumPy

C:\Users\david>pip install pillow
Collecting pillow

#PIL¡GPython Imaging Library
¦w¸ËPillow
>pip install pillow

from PIL import Image, ImageFilter

kitten = Image.open("ABP238.jpg")       #¶}±ÒÀÉ®×
kitten.show()                           #Åã¥ÜÀÉ®×

blurryKitten = kitten.filter(ImageFilter.GaussianBlur)  #¹LÂoªi¾¹
blurryKitten.save("ABP238222.jpg")      #¦sÀÉ
blurryKitten.show()                     #Åã¥ÜÀÉ®×



Python ¶Ç°e email ªº¤TºØ¤è¦¡

https://www.itread01.com/content/1541896623.html

http://pythonscraping.com/pages/page1.html
http://www.pythonscraping.com/pages/page3.html

Web Scraping with Python - Collecting Data from the Modern Web
https://github.com/REMitchell/python-scraping/tree/master/v1/chapter5
https://github.com/REMitchell/python-scraping/tree/master/v1/chapter6
https://github.com/REMitchell/python-scraping/tree/master/v1


ºô¯¸Â^¨ú¡G¨Ï¥ÎPython¡]¤Gª©¡^

¥Ø¿ý
«e¨¥

²Ä¤@³¡ «ØºcÂ^¨úµ{§Ç
²Ä¤@³¹ §Aªº²Ä¤@­ÓÂ^¨úµ{§Ç
²Ä¤G³¹ ¶i¶¥HTML¸ÑªR
²Ä¤T³¹ ¼¶¼gºô¯¸ª¦¦æµ{§Ç
²Ä¥|³¹ ºô¯¸ª¦¦æ¼Ò«¬
²Ä¤­³¹ Scrapy
²Ä¤»³¹ Àx¦s¸ê®Æ

²Ä¤G³¡ Àx¦s¸ê®Æ
²Ä¤C³¹ Åª¨ú¤å¥ó
²Ä¤K³¹ ²M²zÅ¼¸ê®Æ
²Ä¤E³¹ Åª¼g¦ÛµM»y¨¥
²Ä¤Q³¹ ªí³æ»Pµn¤J
²Ä¤Q¤@³¹ »PÂ^¨ú¬ÛÃöªºJavaScript
²Ä¤Q¤G³¹ ³z¹LAPI ª¦¦æ
²Ä¤Q¤T³¹ ¼v¹³³B²z»P¤å¦r¿ëÃÑ
²Ä¤Q¥|³¹ Á×¶}Â^¨ú³´¨À
²Ä¤Q¤­³¹ ¥Hª¦¦æµ{§Ç´ú¸Õ§Aªººô¯¸
²Ä¤Q¤»³¹ ¥­¦æÂ^¨úºô¯¸
²Ä¤Q¤C³¹ »·ºÝÂ^¨ú
²Ä¤Q¤K³¹ ºô¯¸Â^¨úªºªk³W»P¹D¼w

¯Á¤Þ
¦¬¦^






----------------many ST----------------



Åª¨úhtmlÀÉ
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())






----------------many SP----------------

  



Pythonªº®M¥óºÞ²zµ{¦¡	PIP

python -m pip install -U matplotlib	//Windows
pip install -U matplotlib		//Linux
 

¦bWindows¤U¦w¸ËPython®M¥ó:
¥Îwindows command line¦w¸Ë BeautifulSoup
C:\Users\david>pip3 install beautifulsoup4

windows command line¤U:

>pip list	//¬d¬Ý¥Ø«e¦³¦w¸ËªºPython®M¥ó
>pip3 install matplotlib	//¦w¸Ëmatplotlib
>pip3 install pygame		//¦w¸Ëpygame

¥i¥Î­n¦w¸Ëªº:
requests	bs4	selenium


python -m pip install -U pip
python -m pip install -U matplotlib




 
#²£¥Í³sÄòªº¾ã¼Æ
for num in range(10):
    print(num)

for num in range(2, 7):
    print(num)

import sys
import sys as s#À°¼Ò²Õ¨ú­Ó§O¦W

print (sys.argv)
print (s.argv)









'''
¦h¦æµù¸Ñªº¼gªk¡A¤T­Ó '
'''


import math
math.sin(math.pi * i / 2)


¦³‹×Matplotlibªº¤@¨Ç§Þ¥©

http://www.yeolar.com/note/2011/04/28/matplotlib-tips/







import¤§¥Îªk
¤@¡B	Åª¤@­Ó®M¥ó
import numpy
y = numpy.sin(2*numpy.pi*t)



¤G¡B	Åª¤@­Ó®M¥ó¡Bµ¹­ÓÂ²³æªº¥N¸¹
import numpy as np


¤T¡B	³æ¿W­n¬Y¤@­Ó¨ç¼Æ
from numpy import sin

¥|¡B	¬Y­Ó®M¥ó®wªº¨ç¼Æ¥þ­n
from numpy import *



#¥Ñ¼Ð·Ç±`ºA¤À¥¬ÀH¾÷¨ú100­Ó¼Æ¡C

plt.plot(np.random.randn(100))


plt.show()


#±q0¨ì10,«Ü§¡¤Ãªº§ä¥X100­ÓÂI¡C

x = np.linspace(0, 10, 100)


A = np.arange(10)
¿é¥X:array([1, 2, ¡K, 10])







>>> type(data)
<class 'str'>
>>> 
>>> type(a)
<class 'int'>



 Python¦Cªí¡G	//¾Þ§@¤è¦¡«Ü¹³¦r¦ê
 
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
list3 = ["a", "b", "c", "d"];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
 

§R°£¦Cªí¤¤ªº¤¸¯À¡G

­n§R°£¦Cªíªº¤¸¯À¡A¥i¥H¨Ï¥Îdel»y¥y¡A¦pªGª¾¹D­þ¨Ç¤¸¯À­n§R°£¡F©Î¦pªG§A¤£ª¾¹D¨º»ò¨Ï¥Îremove()¤èªk¡C¨Ò¤l¡G

list1 = ['physics', 'chemistry', 1997, 2000];
print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;

°ò¥»¦Cªí¾Þ§@¡G
Python ªí¹F¦¡ 	µ²ªG 				´y­z
len([1, 2, 3]) 	3 				ªø«×
[1, 2, 3] + [4, 5, 6] 	[1, 2, 3, 4, 5, 6] 	¦êÁp
['Hi!'] * 4 	['Hi!', 'Hi!', 'Hi!', 'Hi!'] 	­«½Æ
3 in [1, 2, 3] 	True 				¦¨­û
for x in [1, 2, 3]: print x, 	1 2 3 		­¡¥N


¤º¸m¨ç¼Æ¦Cªí¤Î¤èªk¡G

Python¤¤¥]¬A¤U­±ªº¦Cªí¨ç¼Æ¥\¯à¡G
SN 	¨ç¼Æ¤Î´y­z
1 	cmp(list1, list2)	¤ñ¸û¨â­Ó¦Cªíªº¤¸¯À
2 	len(list)		µ¹¥X¦CªíªºÁ`ªø«×
3 	max(list)		±q¦Cªí¤¤¡A¶µ¥Øªº³Ì¤j­È
4 	min(list)		±q¦Cªí¤¤¡A¶µ¥Øªº³Ì¤p­È
5 	list(seq)		¤@­Ó¤¸²Õ¨ì¦CªíªºÂà´«

Python¤¤¥]¬A¤U­±ªº¦Cªíªº¤èªk
SN 	¤èªk¤Î´y­z
1 	list.append(obj)	²K¥[obj¹ï¶H¨ì¦Cªí
2 	list.count(obj)		­pºâªð¦^obj¥X²{¦b¦Cªíªº¦¸¼Æ
3 	list.extend(seq)	ªþ¥[§Ç¦Cseq¤º®e¨ì¦Cªí
4 	list.index(obj)		ªð¦^¦Cªí¤¤¥X²{objªº³Ì¤p¯Á¤Þ
5 	list.insert(index, obj)	´¡¤Jobj¹ï¶H¦b¦Cªí°¾²¾¯Á¤Þ¦ì¸m
6 	list.pop(obj=list[-1])	²¾°£¨Ãªð¦^¦Cªí³Ì«á¤@­Ó¹ï¶H©Îobj
7 	list.remove(obj)	±q¦Cªí¤¤²¾°£obj¹ï¶H
8 	list.reverse()		¤ÏÂà¦Cªíªº¹ï¶H
9 	list.sort([func])	±Æ§Ç¦Cªí¤¤ªº¹ï¶H¡A¨Ï¥Îfunc¤ñ¸û¡]¦pªGµ¹©w¡^


¦r¨å
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry


print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])



ython¨Ï¥Î³æ¤Þ¸¹©MÂù¤Þ¸¹¨Óªí¥Ü¦r²Å¦ê¬O¤@¼Ëªº¡C

¨Ò¦p¡G
var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

¦r²Å¦ê®æ¦¡¤Æ¾Þ§@
print "My name is %s and weight is %d kg!" % ('Zara', 21) 

¥i¥Î%c %s %d %u %x %X %f


¼Æ¾ÚÃþ«¬Âà´«¡G
¨ç¼Æ 			´y­z
int(x [,base])		±NxÂà´«¬°¤@­Ó¾ã¼Æ¡C°ò¼Æ«ü©w¬°base¡A¦pªGx¬O¤@­Ó¦r²Å¦ê¡C
long(x [,base] )	±NxÂà´«¬°¤@­Óªø¾ã¼Æ¡C°ò¼Æ«ü©w¬°base¡A¦pªGx¬O¤@­Ó¦r²Å¦ê¡C
float(x)		±NxÂà´«¨ì¤@­Ó¯BÂI¼Æ¡C
complex(real [,imag])	³Ð«Ø¤@­Ó½Æ¼Æ¡C
str(x)			Âà´«¹ï¶Hx¬°¦r²Å¦êªí¥Ü§Î¦¡¡C
chr(x)			¾ã¼ÆÂà´«¬°¤@­Ó¦r²Å¡C
unichr(x)		¾ã¼ÆÂà´«¬°¤@­ÓUnicode¦r²Å¡C
hex(x)			±N¾ã¼ÆÂà´«¬°¤Q¤»¶i»s¦r²Å¦ê¡C

¤º«ØÂà´«¨ç¦¡
str
int
float


int("1010", 2)
int("A0A0", 16)


Python¥]¬A¥H¤U°õ¦æ¼Æ¾Ç­pºâªº¨ç¼Æ¡C
¨ç¼Æ 		ªð¦^¡]´y­z¡^
abs(x)		xªºµ´¹ï­È¡Gx©M¹s¤§¶¡ªº¡]¥¿·¥¡^ªº¶ZÂ÷¡C
ceil(x)		xªº¤W­­¡G³Ì¤p¾ã¼Æ¤£¤p©óx
cmp(x, y)	-1 if x < y, 0 if x == y, ©Î1 if x > y
exp(x)		xªº«ü¼Æ: ex
fabs(x) 	xªºµ´¹ï­È
floor(x) 	xªº¦aªO¡G³Ì¤jªº¾ã¼Æ¤£¤j©óx
log(x)		xªº¦ÛµM¹ï¼Æ¡A¹ï©óx> 0®É
log10(x) 	¥H10¬°©³ªº¹ï¼Æ¡AX>0¡C
max(x1, x2,...) ¥¦³Ì¤jªº°Ñ¼Æ¡G­È³Ì±µªñ¥¿µL½a¤j
min(x1, x2,...) ¥¦ªº³Ì¤p°Ñ¼Æ¡G­È³Ì±µªñ­tµL½a¤j
modf(x) 	xªº¨â­Ó¶µ¤¸²Õªº¾ã¼Æ©M¤p¼Æ³¡¤À¡C³o¨â­Ó¤¸¯À¨ã¦³¬Û¦Pªºx²Å¸¹¡C¾ã¼Æ³¡¤Àªð¦^¤@­Ó¯BÂI¼Æ¡C
pow(x, y) 	x**y ªº­È
round(x [,n]) 	x¦b¤p¼ÆÂI¥|ªÙ¤­¤J¨ìn¦ì¼Æ¦r¡C Python»·Â÷¹sÂI¨M©w¡Ground(0.5) ¬O1.0 ¦Óround(0.5) ¬°-1.0¡C
sqrt(x) 	xªº¥­¤è®Ú¡]x>0¡^

¥Î©ó¹CÀ¸¡A¼ÒÀÀ¡A´ú¸Õ¡A¦w¥þ©Ê©M«O±K©ÊªºÀ³¥ÎªºÀH¾÷¼Æ¡CPython¥]¬A±`¥Î¥H¤U¨ç¼Æ¡C
¨ç¼Æ 		´y­z
choice(seq) 	±q¦Cªí¡A¤¸²Õ©Î¦r²Å¦êÀH¾÷¶µ¡C
randrange ([start,] stop [,step]) 	±q½d³òÀH¾÷¿ï¾Üªº¤¸¯À¡]±Ò°Ê¡A°±¤î¡A¨BÆJ¡^
random() 	ÀH¾÷¯BÂI¼Ær¡A¨Ï±o0¬O¤p©ó©Îµ¥©ór¡Ar¤p©ó1
seed([x]) 	³]¸m¥Í¦¨ÀH¾÷¼Æ¨Ï¥Î¾ã¼Æ¶}©l­È¡C½Õ¥Î¥ô¦ó¨ä¥LÀH¾÷¼Ò¶ô¨ç¼Æ¤§«e½Õ¥Î³o­Ó¨ç¼Æ¡Cªð¦^None¡C
shuffle(lst) 	ÀH¾÷¤Æ¥N´À¦Cªí¤¤ªº¶µ¡Cªð¦^None¡C
uniform(x, y) 	ÀH¾÷¯BÂI¼Ær¡A¨Ï±ox¤p©ó©Îµ¥©ór¡Ar¤p©óy



degrees(x) 	±q©·«×¨ì«×¨¤ x ªºÂà´«
radians(x) 	±q¨¤«×¨ì©·«×¨¤ x ªºÂà´«




python¯S¦³ªº¹Bºâ             

** 	«ü¼Æ¾­- °õ¦æ¹Bºâ²Åªº«ü¼Æ¡]¾­¡^­pºâ 	a**b = 10 ªº 20 ¦¸¾­
// 	Floor Division - Floor°£ªk - ¾Þ§@¼Æ¬Û°£¡A¨äµ²ªGªº¤p¼ÆÂI«áªº¼Æ¦r±N³Q§R°£¡C 	9//2 = 4 ¡A 9.0//2.0 = 4.0

«ü¼Æ
¦aªO°£

**=
//=


a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011


             
¦Ó¤¤¤åªº³B²z¡A§Ú­Ì¥i¥H³z¹Lunicodeªº½s¸Ñ½X¨Ó³B²z

!!!ª`·N¤¤¤åªºÀÉ®×­n¥[¤W# encoding: utf-8

³æ¦æµù¸Ñ¬°#,¦h¦æµù¸Ñ«h¥Î"""¶}ÀY»Pµ²§À
"""
³o¬O¤@­ÓÂ²³æªºpythonµ{¦¡
¤¶²Ð°ò¥»ªº»yªk
"""

Python - ¤Q¤ÀÄÁ¤Jªù 
http://tech-marsw.logdown.com/blog/2014/09/03/getting-started-with-python-in-ten-minute

http://tech-marsw.logdown.com/blog/2016/01/10/crawler-index


python

¨Ï¥ÎmatplotlibÃ¸¹Ï
http://me1237guy.pixnet.net/blog/post/64496047
http://me1237guy.pixnet.net/blog/post/64496047

https://matplotlib.org/index.html

https://matplotlib.org/gallery/index.html

https://matplotlib.org/api/cbook_api.html#matplotlib.cbook.get_sample_data

https://matplotlib.org/api/cbook_api.html#matplotlib.cbook.get_sample_data




https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py



¦³‹×Matplotlibªº¤@¨Ç§Þ¥©

http://www.yeolar.com/note/2011/04/28/matplotlib-tips/




matplotlib

https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-5%E8%AC%9B-%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96-matplotlib-seaborn-plotly-75cd353d6d3f



/**********************************************************
 * Filename	:	python_data.c
 * Description	:	python¬ÛÃö¸ê®Æ»P¤ù¬qµ{¦¡
 **********************************************************/



´ú¸Õ¦³¨S¦³¸Ëtkinter
>>> import tkinter
>>> tkinter._test()
>>> 

[²Ä 18 ¤Ñ] ¸ê®ÆµøÄ±¤Æ matplotlib
https://ithelp.ithome.com.tw/articles/10186484

tkinter±Ð¾Ç
http://effbot.org/tkinterbook/
http://effbot.org/tkinterbook/tkinter-index.htm

python±Ð¾Ç

https://sites.google.com/site/ezpythoncolorcourse/


turtle --- ®üÀtÃ¸¹Ï
https://docs.python.org/zh-cn/3/library/turtle.html


http://www.runoob.com/python/python-tutorial.html
http://www.runoob.com/python/python-tutorial.html

http://tw.gitbook.net/python/index.html

C:\Users\user>python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import tkinter
>>> tkinter._test()
>>> tkinter._test()
>>>
>>>
>>>
>>> tkinter._test()
>>>




·sª©¥»¨ú®ø¤Fraw_input()¡A§ï¬°input()¤F 

pygame.org/download.shtml

pygame-1.9.1.win32-py2.7.msi 3.1MB





