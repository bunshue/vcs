#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

fr = open('workfile.txt', 'w')
fr.write('This is a test\n')
fr.close()

fw = open('workfile.txt', 'r')
for line in fw:
    print(line)
fw.close()
