# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import aiml
kernel = aiml.Kernel()
kernel.learn("01-AIML-hello.xml")
while True:   # Press CTRL-C to break this loop
    try:
        print(kernel.respond(input("Enter your message >> ")))
    except:
        print(kernel.respond(raw_input("Enter your message >> ")))



