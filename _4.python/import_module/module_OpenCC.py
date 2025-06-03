"""
開放中文轉換
Open Chinese convert (OpenCC)

# pip install opencc-python-reimplemented

轉換模式 :

hk2s : 香港正中 => 簡中
s2hk:  簡中     => 香港正中
s2t:   簡中     => 正中
s2tw:  簡中     => 台灣正中
s2twp: 簡中     => 台灣正中 (包含慣用詞轉換)
t2hk:  正中     => 香港正中
t2s:   正中     => 簡中
t2tw:  正中     => 台灣正中
tw2s:  台灣正中 => 簡中
tw2sp: 台灣正中 => 簡中 (包含慣用詞轉換)

"""

import opencc

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

text1 = "我去过清华大学和交通大学，打印机、光盘、内存。"
text2 = "我去過清華大學和交通大學，印表機、光碟、記憶體。"

print("顯示模組的所有名稱")

print(dir(opencc))
print()
print(dir(opencc.OpenCC))

openCC = opencc.OpenCC("s2t")
line = openCC.convert(text1)
print("      " + text1)
print("s2t  :" + line)

openCC = opencc.OpenCC("s2twp")
line = openCC.convert(text1)
print("s2twp:" + line)

openCC = opencc.OpenCC("t2s")
line = openCC.convert(text2)
print("      " + text2)
print("t2s  :" + line)

openCC = opencc.OpenCC("tw2sp")
line = openCC.convert(text2)
print("tw2sp:" + line)

print("------------------------------------------------------------")  # 60個

cc = opencc.OpenCC("s2t")  # convert from Simplified Chinese to 正中
# can also set conversion by calling set_conversion
# cc.set_conversion('s2tw')
to_convert = "开放中文转换"
converted = cc.convert(to_convert)

print("原字串 :", to_convert)
print("轉換後 :", converted)

print("------------------------------------------------------------")  # 60個

print("OpenCC：繁體簡體轉換")

cc = opencc.OpenCC("t2s")
text = "自然語言認知和理解是讓電腦把輸入的語言變成有意思的符號和關係，然後根據目的再處理。自然語言生成系統則是把計算機數據轉化為自然語言。"
print(cc.convert(text))

cc = opencc.OpenCC("s2t")
text = "自然语言认知和理解是让电脑把输入的语言变成有意思的符号和关系，然后根据目的再处理。自然语言生成系统则是把计算机数据转化为自然语言。"
print(cc.convert(text))

text = "滑鼠在螢幕上移動"
cc = opencc.OpenCC("t2s")
print("一般轉換：{}".format(cc.convert(text)))
cc = opencc.OpenCC("tw2sp")
print("慣用語轉換：{}".format(cc.convert(text)))

text = "鼠标在屏幕上移动"
cc = opencc.OpenCC("s2t")
print("一般轉換：{}".format(cc.convert(text)))
cc = opencc.OpenCC("s2twp")
print("片語轉換：{}".format(cc.convert(text)))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

