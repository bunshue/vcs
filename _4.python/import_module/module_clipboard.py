import clipboard

print('目前剪貼簿內的文字 :')
cc = clipboard.paste()
print(cc)

print('將一些文字放進剪貼簿內')
text = "將一些文字放進剪貼簿內"
clipboard.copy(text)

