
https://www.kancloud.cn/thinkphp/python-guide/39428

http://www.codedata.com.tw/python/python-tutorial-the-1st-class-4-unicode-support-basic-input-output/
http://www.runoob.com/python/python-chinese-encoding.html



pip install numpy	�w��NumPy

C:\Users\david>pip install pillow
Collecting pillow

#PIL�GPython Imaging Library
�w��Pillow
>pip install pillow

from PIL import Image, ImageFilter

kitten = Image.open("ABP238.jpg")       #�}���ɮ�
kitten.show()                           #����ɮ�

blurryKitten = kitten.filter(ImageFilter.GaussianBlur)  #�L�o�i��
blurryKitten.save("ABP238222.jpg")      #�s��
blurryKitten.show()                     #����ɮ�



Python �ǰe email ���T�ؤ覡

https://www.itread01.com/content/1541896623.html

http://pythonscraping.com/pages/page1.html
http://www.pythonscraping.com/pages/page3.html

Web Scraping with Python - Collecting Data from the Modern Web
https://github.com/REMitchell/python-scraping/tree/master/v1/chapter5
https://github.com/REMitchell/python-scraping/tree/master/v1/chapter6
https://github.com/REMitchell/python-scraping/tree/master/v1


�����^���G�ϥ�Python�]�G���^

�ؿ�
�e��

�Ĥ@�� �غc�^���{��
�Ĥ@�� �A���Ĥ@���^���{��
�ĤG�� �i��HTML�ѪR
�ĤT�� ���g��������{��
�ĥ|�� ��������ҫ�
�Ĥ��� Scrapy
�Ĥ��� �x�s���

�ĤG�� �x�s���
�ĤC�� Ū�����
�ĤK�� �M�zż���
�ĤE�� Ū�g�۵M�y��
�ĤQ�� ���P�n�J
�ĤQ�@�� �P�^��������JavaScript
�ĤQ�G�� �z�LAPI ����
�ĤQ�T�� �v���B�z�P��r����
�ĤQ�|�� �׶}�^������
�ĤQ���� �H����{�Ǵ��էA������
�ĤQ���� �����^������
�ĤQ�C�� �����^��
�ĤQ�K�� �����^�����k�W�P�D�w

����
���^






----------------many ST----------------



Ū��html��
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())






----------------many SP----------------

  



Python���M��޲z�{��	PIP

python -m pip install -U matplotlib	//Windows
pip install -U matplotlib		//Linux
 

�bWindows�U�w��Python�M��:
��windows command line�w�� BeautifulSoup
C:\Users\david>pip3 install beautifulsoup4

windows command line�U:

>pip list	//�d�ݥثe���w�˪�Python�M��
>pip3 install matplotlib	//�w��matplotlib
>pip3 install pygame		//�w��pygame

�i�έn�w�˪�:
requests	bs4	selenium


python -m pip install -U pip
python -m pip install -U matplotlib




 
#���ͳs�򪺾��
for num in range(10):
    print(num)

for num in range(2, 7):
    print(num)

import sys
import sys as s#���Ҳը��ӧO�W

print (sys.argv)
print (s.argv)









'''
�h����Ѫ��g�k�A�T�� '
'''


import math
math.sin(math.pi * i / 2)


����Matplotlib���@�ǧޥ�

http://www.yeolar.com/note/2011/04/28/matplotlib-tips/







import���Ϊk
�@�B	Ū�@�ӮM��
import numpy
y = numpy.sin(2*numpy.pi*t)



�G�B	Ū�@�ӮM��B����²�檺�N��
import numpy as np


�T�B	��W�n�Y�@�Ө��
from numpy import sin

�|�B	�Y�ӮM��w����ƥ��n
from numpy import *



#�ѼзǱ`�A�����H����100�ӼơC

plt.plot(np.random.randn(100))


plt.show()


#�q0��10,�ܧ��ê���X100���I�C

x = np.linspace(0, 10, 100)


A = np.arange(10)
��X:array([1, 2, �K, 10])







>>> type(data)
<class 'str'>
>>> 
>>> type(a)
<class 'int'>



 Python�C��G	//�ާ@�覡�ܹ��r��
 
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
list3 = ["a", "b", "c", "d"];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
 

�R���C���������G

�n�R���C�������A�i�H�ϥ�del�y�y�A�p�G���D���Ǥ����n�R���F�Φp�G�A�����D����ϥ�remove()��k�C�Ҥl�G

list1 = ['physics', 'chemistry', 1997, 2000];
print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;

�򥻦C��ާ@�G
Python ��F�� 	���G 				�y�z
len([1, 2, 3]) 	3 				����
[1, 2, 3] + [4, 5, 6] 	[1, 2, 3, 4, 5, 6] 	���p
['Hi!'] * 4 	['Hi!', 'Hi!', 'Hi!', 'Hi!'] 	����
3 in [1, 2, 3] 	True 				����
for x in [1, 2, 3]: print x, 	1 2 3 		���N


���m��ƦC��Τ�k�G

Python���]�A�U�����C���ƥ\��G
SN 	��Ƥδy�z
1 	cmp(list1, list2)	�����ӦC������
2 	len(list)		���X�C���`����
3 	max(list)		�q�C���A���ت��̤j��
4 	min(list)		�q�C���A���ت��̤p��
5 	list(seq)		�@�Ӥ��ը�C���ഫ

Python���]�A�U�����C����k
SN 	��k�δy�z
1 	list.append(obj)	�K�[obj��H��C��
2 	list.count(obj)		�p���^obj�X�{�b�C������
3 	list.extend(seq)	���[�ǦCseq���e��C��
4 	list.index(obj)		��^�C���X�{obj���̤p����
5 	list.insert(index, obj)	���Jobj��H�b�C�������ަ�m
6 	list.pop(obj=list[-1])	�����ê�^�C��̫�@�ӹ�H��obj
7 	list.remove(obj)	�q�C������obj��H
8 	list.reverse()		����C����H
9 	list.sort([func])	�ƧǦC������H�A�ϥ�func����]�p�G���w�^


�r��
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry


print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])



ython�ϥγ�޸��M���޸��Ӫ�ܦr�Ŧ�O�@�˪��C

�Ҧp�G
var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

�r�Ŧ�榡�ƾާ@
print "My name is %s and weight is %d kg!" % ('Zara', 21) 

�i��%c %s %d %u %x %X %f


�ƾ������ഫ�G
��� 			�y�z
int(x [,base])		�Nx�ഫ���@�Ӿ�ơC��ƫ��w��base�A�p�Gx�O�@�Ӧr�Ŧ�C
long(x [,base] )	�Nx�ഫ���@�Ӫ���ơC��ƫ��w��base�A�p�Gx�O�@�Ӧr�Ŧ�C
float(x)		�Nx�ഫ��@�ӯB�I�ơC
complex(real [,imag])	�Ыؤ@�ӽƼơC
str(x)			�ഫ��Hx���r�Ŧ��ܧΦ��C
chr(x)			����ഫ���@�Ӧr�šC
unichr(x)		����ഫ���@��Unicode�r�šC
hex(x)			�N����ഫ���Q���i�s�r�Ŧ�C

�����ഫ�禡
str
int
float


int("1010", 2)
int("A0A0", 16)


Python�]�A�H�U����ƾǭp�⪺��ơC
��� 		��^�]�y�z�^
abs(x)		x������ȡGx�M�s�������]�����^���Z���C
ceil(x)		x���W���G�̤p��Ƥ��p��x
cmp(x, y)	-1 if x < y, 0 if x == y, ��1 if x > y
exp(x)		x������: ex
fabs(x) 	x�������
floor(x) 	x���a�O�G�̤j����Ƥ��j��x
log(x)		x���۵M��ơA���x> 0��
log10(x) 	�H10��������ơAX>0�C
max(x1, x2,...) ���̤j���ѼơG�ȳ̱��񥿵L�a�j
min(x1, x2,...) �����̤p�ѼơG�ȳ̱���t�L�a�j
modf(x) 	x����Ӷ����ժ���ƩM�p�Ƴ����C�o��Ӥ����㦳�ۦP��x�Ÿ��C��Ƴ�����^�@�ӯB�I�ơC
pow(x, y) 	x**y ����
round(x [,n]) 	x�b�p���I�|�٤��J��n��Ʀr�C Python�����s�I�M�w�Ground(0.5) �O1.0 ��round(0.5) ��-1.0�C
sqrt(x) 	x������ڡ]x>0�^

�Ω�C���A�����A���աA�w���ʩM�O�K�ʪ����Ϊ��H���ơCPython�]�A�`�ΥH�U��ơC
��� 		�y�z
choice(seq) 	�q�C��A���թΦr�Ŧ��H�����C
randrange ([start,] stop [,step]) 	�q�d���H����ܪ������]�ҰʡA����A�B�J�^
random() 	�H���B�I��r�A�ϱo0�O�p��ε���r�Ar�p��1
seed([x]) 	�]�m�ͦ��H���ƨϥξ�ƶ}�l�ȡC�եΥ����L�H���Ҷ���Ƥ��e�եγo�Ө�ơC��^None�C
shuffle(lst) 	�H���ƥN���C�������C��^None�C
uniform(x, y) 	�H���B�I��r�A�ϱox�p��ε���r�Ar�p��y



degrees(x) 	�q���ר�ר� x ���ഫ
radians(x) 	�q���ר쩷�ר� x ���ഫ




python�S�����B��             

** 	���ƾ�- ����B��Ū����ơ]���^�p�� 	a**b = 10 �� 20 ����
// 	Floor Division - Floor���k - �ާ@�Ƭ۰��A�䵲�G���p���I�᪺�Ʀr�N�Q�R���C 	9//2 = 4 �A 9.0//2.0 = 4.0

����
�a�O��

**=
//=


a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011


             
�Ӥ��媺�B�z�A�ڭ̥i�H�z�Lunicode���s�ѽX�ӳB�z

!!!�`�N���媺�ɮ׭n�[�W# encoding: utf-8

�����Ѭ�#,�h����ѫh��"""�}�Y�P����
"""
�o�O�@��²�檺python�{��
���а򥻪��y�k
"""

Python - �Q�����J�� 
http://tech-marsw.logdown.com/blog/2014/09/03/getting-started-with-python-in-ten-minute

http://tech-marsw.logdown.com/blog/2016/01/10/crawler-index


python

�ϥ�matplotlibø��
http://me1237guy.pixnet.net/blog/post/64496047
http://me1237guy.pixnet.net/blog/post/64496047

https://matplotlib.org/index.html

https://matplotlib.org/gallery/index.html

https://matplotlib.org/api/cbook_api.html#matplotlib.cbook.get_sample_data

https://matplotlib.org/api/cbook_api.html#matplotlib.cbook.get_sample_data




https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py



����Matplotlib���@�ǧޥ�

http://www.yeolar.com/note/2011/04/28/matplotlib-tips/




matplotlib

https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-5%E8%AC%9B-%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96-matplotlib-seaborn-plotly-75cd353d6d3f



/**********************************************************
 * Filename	:	python_data.c
 * Description	:	python������ƻP���q�{��
 **********************************************************/



���զ��S����tkinter
>>> import tkinter
>>> tkinter._test()
>>> 

[�� 18 ��] ��Ƶ�ı�� matplotlib
https://ithelp.ithome.com.tw/articles/10186484

tkinter�о�
http://effbot.org/tkinterbook/
http://effbot.org/tkinterbook/tkinter-index.htm

python�о�

https://sites.google.com/site/ezpythoncolorcourse/


turtle --- ���tø��
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




�s���������Fraw_input()�A�אּinput()�F 

pygame.org/download.shtml

pygame-1.9.1.win32-py2.7.msi 3.1MB





