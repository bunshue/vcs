#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"
import os
import os.path
if os.path.exists('./folder'):
    os.rmdir('./folder')
    print(os.getcwd())    
else: 
    os.mkdir('./folder')  
    os.chdir('./folder')
    print(os.getcwd())    