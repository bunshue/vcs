# _*_ coding: utf-8 *_*
# 程式 10-8 (Python 3 version)

from selenium import webdriver

url = 'http://yourblog.pixnet.net'

web = webdriver.Firefox()
web.get(url)
web.find_element_by_id('topbar__user__login').click()
web.find_element_by_name('username').clear()
web.find_element_by_name('username').send_keys('your account')
web.find_element_by_name('password').clear()
web.find_element_by_name('password').send_keys('your password')
web.find_element_by_id('login-send').click()
