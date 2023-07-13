#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().run_line_magic('pip', 'install pyautogui')


# In[9]:


import pyautogui as auto
from IPython.display import clear_output
import time
while True:
    x, y = auto.position()
    clear_output()
    print(x, y)
    time.sleep(0.5)
    if x < 10:
        break


# In[6]:


import pyautogui as auto
import time
auto.PAUSE = 1
x, y = 630, 20
auto.moveTo(x, y, 2)
auto.click()
x, y = 264, 62
auto.moveTo(x, y, 2)
auto.click()
auto.typewrite("https://hophd.wordpress.com")
time.sleep(2)
auto.press("enter")


# In[5]:


from selenium import webdriver
import time
url = "https://hophd.wordpress.com"
web = webdriver.Chrome("chromedriver.exe")
web.implicitly_wait(60)
web.get(url)
web.set_window_position(0, 0)
time.sleep(10)
web.quit()


# In[ ]:




