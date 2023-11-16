# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import aiml
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("03-AIML-random.xml")
while True:   # Press CTRL-C to break this loop
    try:
        print(kernel.respond(input("Enter your message >> ")))
    except:
        print(kernel.respond(raw_input("Enter your message >> ")))

