# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
# AIML 請安裝0.9.1  其他版本中文字會有問題 ，而最新版本0.9.2 確定不能執行中文對話
#  pip install aiml==0.9.1
import aiml
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("02-AIML-helloChinese.xml")
while True:   # Press CTRL-C to break this loop
    try:
        print(kernel.respond(input("Enter your message >> ")))
    except:
        print(kernel.respond(raw_input("Enter your message >> ")))

