"""
OpenCC：繁體簡體轉換

開放中文轉換

Open Chinese convert (OpenCC)

# pip install opencc-python-reimplemented

openCC = opencc.OpenCC("s2t")
openCC.set_conversion("s2t") same

轉換模式 :

s2t:   簡中     => 正中
s2tw:  簡中     => 台灣正中
s2twp: 簡中     => 台灣正中 (包含慣用詞轉換)

t2s:   正中     => 簡中
t2tw:  正中     => 台灣正中
tw2s:  台灣正中 => 簡中
tw2sp: 台灣正中 => 簡中 (包含慣用詞轉換)

hk2s : 香港正中 => 簡中
s2hk:  簡中     => 香港正中
t2hk:  正中     => 香港正中

"""
import sys
import opencc

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("顯示模組的所有名稱")

print(dir(opencc))
print()
print(dir(opencc.OpenCC))

print("------------------------------")  # 30個

text1 = "中国简体中文电脑用语，打印机、光盘、内存、鼠标、屏幕。"
text2 = "台灣正體中文電腦用語，印表機、光碟、記憶體、滑鼠、螢幕。"

print("s2t 簡中     => 正中")
openCC = opencc.OpenCC("s2t")
line = openCC.convert(text1)
print("原 :", text1)
print("轉 :", line)

print("------------------------------")  # 30個

print("t2s 正中     => 簡中")
openCC = opencc.OpenCC("t2s")
line = openCC.convert(text2)
print("原 :", text2)
print("轉 :", line)

print("------------------------------")  # 30個

print("tw2sp 台灣正中 => 簡中 (包含慣用詞轉換)")
openCC = opencc.OpenCC("tw2sp")
line = openCC.convert(text2)
print("原 :", text2)
print("轉 :", line)

print("------------------------------")  # 30個

print("s2twp 簡中     => 台灣正中 (包含慣用詞轉換)")
openCC = opencc.OpenCC("s2twp")
line = openCC.convert(text1)
print("原 :", text1)
print("轉 :", line)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個
