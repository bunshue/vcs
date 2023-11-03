wd = 'Python is funny and powerful.'
print('字串:', wd)
print('Python為開頭的字串嗎', wd.startswith('Python'))   #回傳True
print('funny為開頭的字串嗎', wd.startswith('funny', 0))#回傳False
print('funny從指定位置的開頭的字串嗎', wd.startswith('funny', 10))  #回傳True
print('powerful.為結尾字串嗎', wd.endswith('powerful.'))  #回傳True
