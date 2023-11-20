"""
開放中文轉換
Open Chinese convert (OpenCC)

Conversions 轉換
    hk2s: Traditional Chinese (Hong Kong standard) to Simplified Chinese
    s2hk: Simplified Chinese to Traditional Chinese (Hong Kong standard)
    s2t: Simplified Chinese to Traditional Chinese
    s2tw: Simplified Chinese to Traditional Chinese (Taiwan standard)
    s2twp: Simplified Chinese to Traditional Chinese (Taiwan standard, with phrases)
    t2hk: Traditional Chinese to Traditional Chinese (Hong Kong standard)
    t2s: Traditional Chinese to Simplified Chinese
    t2tw: Traditional Chinese to Traditional Chinese (Taiwan standard)
    tw2s: Traditional Chinese (Taiwan standard) to Simplified Chinese
    tw2sp: Traditional Chinese (Taiwan standard) to Simplified Chinese (with phrases)
"""

from opencc import OpenCC

text1 = u"我去过清华大学和交通大学，打印机、光盘、内存。"
text2 = u"我去過清華大學和交通大學，印表機、光碟、記憶體。"

print('顯示模組的所有名稱')
import opencc
print(dir(opencc))
print()
print(dir(opencc.OpenCC))

openCC = OpenCC('s2t')
line = openCC.convert(text1) 
print("      " + text1)
print("s2t  :" + line)

openCC = OpenCC('s2twp')
line = openCC.convert(text1)
print("s2twp:" + line)

openCC = OpenCC('t2s')
line = openCC.convert(text2) 
print("      " + text2)
print("t2s  :" + line)

openCC = OpenCC('tw2sp')
line = openCC.convert(text2)
print("tw2sp:" + line)

print('------------------------------------------------------------')	#60個

from opencc import OpenCC
cc = OpenCC('s2t')  # convert from Simplified Chinese to Traditional Chinese
# can also set conversion by calling set_conversion
# cc.set_conversion('s2tw')
to_convert = '开放中文转换'
converted = cc.convert(to_convert)

print('原字串 :', to_convert)
print('轉換後 :', converted)

print('------------------------------------------------------------')	#60個



print('OpenCC：繁體簡體轉換')
# pip install opencc-python-reimplemented

from opencc import OpenCC

cc = OpenCC('t2s')
text = '自然語言認知和理解是讓電腦把輸入的語言變成有意思的符號和關係，然後根據目的再處理。自然語言生成系統則是把計算機數據轉化為自然語言。'
print(cc.convert(text))

cc = OpenCC('s2t')
text = '自然语言认知和理解是让电脑把输入的语言变成有意思的符号和关系，然后根据目的再处理。自然语言生成系统则是把计算机数据转化为自然语言。'
print(cc.convert(text))


text = '滑鼠在螢幕上移動'
cc = OpenCC('t2s')
print('一般轉換：{}'.format(cc.convert(text)))
cc = OpenCC('tw2sp')
print('慣用語轉換：{}'.format(cc.convert(text)))

text = '鼠标在屏幕上移动'
cc = OpenCC('s2t')
print('一般轉換：{}'.format(cc.convert(text)))
cc = OpenCC('s2twp')
print('片語轉換：{}'.format(cc.convert(text)))


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

