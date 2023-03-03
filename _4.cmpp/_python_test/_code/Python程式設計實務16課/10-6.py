# _*_ coding: utf-8 *_*
# 程式 10-6 (Python 3 version)

from selenium import webdriver
urls = [
'http://hophd.com',
'http://drho.club',
'http://skynetbooks.com',
'http://drho.tw/fit',
'http://drho.tw/news']

web = webdriver.Firefox()
web.set_window_position(0,0)
web.set_window_size(800,600)
i = 0
for url in urls:
    web.get(url)
    web.save_screenshot("webpage{}.png".format(i))
    i += 1
web.quit()
