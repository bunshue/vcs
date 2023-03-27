from selenium import webdriver
urls = [
'https://www.google.com.tw/',
'https://tw.yahoo.com/',
'https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5']

web = webdriver.Firefox()
web.set_window_position(0,0)
web.set_window_size(800,600)

i = 0
for url in urls:
    web.get(url)
    web.save_screenshot("webpage{}.png".format(i))
    i += 1
web.quit()
