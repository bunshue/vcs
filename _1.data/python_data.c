

----------------many ST----------------





----------------many SP----------------

  





'''
︽爹秆糶猭 '
'''


import math
math.sin(math.pi * i / 2)


Τ嬜Matplotlibㄇмォ

http://www.yeolar.com/note/2011/04/28/matplotlib-tips/







importぇノ猭
	弄甅ン
import numpy
y = numpy.sin(2*numpy.pi*t)



	弄甅ン倒虏虫腹
import numpy as np


	虫縒璶琘ㄧ计
from numpy import sin

	琘甅ン畐ㄧ计璶
from numpy import *



#パ夹非盽篈だガ繦诀100计

plt.plot(np.random.randn(100))


plt.show()


#眖010,Аっт100翴

x = np.linspace(0, 10, 100)


A = np.arange(10)
块:array([1, 2, , 10])







>>> type(data)
<class 'str'>
>>> 
>>> type(a)
<class 'int'>



 Python	//巨よΑ钩﹃
 
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
list3 = ["a", "b", "c", "d"];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
 

埃いじ

璶埃じㄏノdel粂狦笵ㄇじ璶埃┪狦ぃ笵ê或ㄏノremove()よ猭ㄒ

list1 = ['physics', 'chemistry', 1997, 2000];
print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;

膀セ巨
Python 笷Α 	挡狦 				磞瓃
len([1, 2, 3]) 	3 				
[1, 2, 3] + [4, 5, 6] 	[1, 2, 3, 4, 5, 6] 	﹃羛
['Hi!'] * 4 	['Hi!', 'Hi!', 'Hi!', 'Hi!'] 	狡
3 in [1, 2, 3] 	True 				Θ
for x in [1, 2, 3]: print x, 	1 2 3 		


ず竚ㄧ计のよ猭

Pythonい珹ㄧ计
SN 	ㄧ计の磞瓃
1 	cmp(list1, list2)	ゑ耕ㄢじ
2 	len(list)		倒羆
3 	max(list)		眖い兜ヘ程
4 	min(list)		眖い兜ヘ程
5 	list(seq)		じ舱锣传

Pythonい珹よ猭
SN 	よ猭の磞瓃
1 	list.append(obj)	睰obj癸禜
2 	list.count(obj)		璸衡obj瞷Ω计
3 	list.extend(seq)	seqず甧
4 	list.index(obj)		い瞷obj程ま
5 	list.insert(index, obj)	础obj癸禜熬簿ま竚
6 	list.pop(obj=list[-1])	簿埃程癸禜┪obj
7 	list.remove(obj)	眖い簿埃obj癸禜
8 	list.reverse()		は锣癸禜
9 	list.sort([func])	逼い癸禜ㄏノfuncゑ耕狦倒﹚


ㄥ
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry


print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])



ythonㄏノ虫ま腹㎝蛮ま腹ㄓボ才﹃琌妓

ㄒ
var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

才﹃Αて巨
print "My name is %s and weight is %d kg!" % ('Zara', 21) 

ノ%c %s %d %u %x %X %f


计沮摸锣传
ㄧ计 			磞瓃
int(x [,base])		盢x锣传俱计膀计﹚base狦x琌才﹃
long(x [,base] )	盢x锣传俱计膀计﹚base狦x琌才﹃
float(x)		盢x锣传疊翴计
complex(real [,imag])	承狡计
str(x)			锣传癸禜x才﹃ボΑ
chr(x)			俱计锣传才
unichr(x)		俱计锣传Unicode才
hex(x)			盢俱计锣传せ秈籹才﹃

ず锣传ㄧΑ
str
int
float


int("1010", 2)
int("A0A0", 16)


Python珹磅︽计厩璸衡ㄧ计
ㄧ计 		磞瓃
abs(x)		x荡癸x㎝箂ぇ丁タ伐禯瞒
ceil(x)		x程俱计ぃx
cmp(x, y)	-1 if x < y, 0 if x == y, ┪1 if x > y
exp(x)		x计: ex
fabs(x) 	x荡癸
floor(x) 	x狾程俱计ぃx
log(x)		x礛癸计癸x> 0
log10(x) 	10┏癸计X>0
max(x1, x2,...) ウ程把计程钡タ礚絘
min(x1, x2,...) ウ程把计程钡璽礚絘
modf(x) 	xㄢ兜じ舱俱计㎝计场だ硂ㄢじㄣΤx才腹俱计场だ疊翴计
pow(x, y) 	x**y 
round(x [,n]) 	x计翴きn计 Python环瞒箂翴∕﹚round(0.5) 琌1.0 τround(0.5) -1.0
sqrt(x) 	xキよx>0

ノ笴栏家览代刚┦㎝玂盞┦莱ノ繦诀计Python珹盽ノㄧ计
ㄧ计 		磞瓃
choice(seq) 	眖じ舱┪才﹃繦诀兜
randrange ([start,] stop [,step]) 	眖絛瞅繦诀匡拒じ币笆氨ゎ˙艼
random() 	繦诀疊翴计rㄏ眔0琌┪单rr1
seed([x]) 	砞竚ネΘ繦诀计ㄏノ俱计秨﹍秸ノヴㄤ繦诀家遏ㄧ计ぇ玡秸ノ硂ㄧ计None
shuffle(lst) 	繦诀て蠢い兜None
uniform(x, y) 	繦诀疊翴计rㄏ眔x┪单rry



degrees(x) 	眖┓à x 锣传
radians(x) 	眖à┓à x 锣传




python疭Τ笲衡             

** 	计经- 磅︽笲衡才计经璸衡 	a**b = 10  20 Ω经
// 	Floor Division - Floor埃猭 - 巨计埃ㄤ挡狦计翴计盢砆埃 	9//2 = 4  9.0//2.0 = 4.0

计
狾埃

**=
//=


a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011


             
τいゅ矪瞶и硓筁unicode絪秆絏ㄓ矪瞶

!!!猔種いゅ郎璶# encoding: utf-8

虫︽爹秆#,︽爹秆玥ノ"""秨繷籔挡Ю
"""
硂琌虏虫python祘Α
ざ残膀セ粂猭
"""

Python - だ牧 
http://tech-marsw.logdown.com/blog/2014/09/03/getting-started-with-python-in-ten-minute

http://tech-marsw.logdown.com/blog/2016/01/10/crawler-index


python

ㄏノmatplotlib酶瓜
http://me1237guy.pixnet.net/blog/post/64496047
http://me1237guy.pixnet.net/blog/post/64496047

https://matplotlib.org/index.html

https://matplotlib.org/gallery/index.html

https://matplotlib.org/api/cbook_api.html#matplotlib.cbook.get_sample_data

https://matplotlib.org/api/cbook_api.html#matplotlib.cbook.get_sample_data




https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py



Τ嬜Matplotlibㄇмォ

http://www.yeolar.com/note/2011/04/28/matplotlib-tips/




matplotlib

https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-5%E8%AC%9B-%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96-matplotlib-seaborn-plotly-75cd353d6d3f



Windows杆Python甅ン

windows command line:


>pip list	//琩ヘ玡Τ杆Python甅ン


>pip3 install matplotlib	//杆matplotlib
>pip3 install pygame		//杆pygame

ノ璶杆:
requests	bs4	selenium


python -m pip install -U pip
python -m pip install -U matplotlib



/**********************************************************
 * Filename	:	python_data.c
 * Description	:	python闽戈籔琿祘Α
 **********************************************************/



代刚Τ⊿Τ杆tkinter
>>> import tkinter
>>> tkinter._test()
>>> 

[材 18 ぱ] 戈跌谋て matplotlib
https://ithelp.ithome.com.tw/articles/10186484

tkinter毙厩
http://effbot.org/tkinterbook/
http://effbot.org/tkinterbook/tkinter-index.htm

python毙厩

https://sites.google.com/site/ezpythoncolorcourse/


turtle --- 纓酶瓜
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




穝セraw_input()эinput() 

pygame.org/download.shtml

pygame-1.9.1.win32-py2.7.msi 3.1MB





