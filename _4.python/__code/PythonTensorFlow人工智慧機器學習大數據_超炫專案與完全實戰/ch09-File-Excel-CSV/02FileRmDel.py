#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import os
import os.path
import shutil
FileName1='workfile.txt'
FileName2='workfileCopy.txt'
FileName3='workfileRename.txt'

def FunListAllFiles(iMeg):
	allFiles = os.listdir('.')
	print(iMeg)
	print(allFiles)


FunListAllFiles("1.")
if os.path.isfile(FileName1) and os.access(FileName1, os.R_OK):
    shutil.copy(FileName1, FileName2)   


FunListAllFiles("2.")
if os.path.isfile(FileName2) and os.access(FileName2, os.R_OK):
    os.rename(FileName2, FileName3)   


FunListAllFiles("3.")
if os.path.isfile(FileName3) and os.access(FileName3, os.R_OK): 
    os.remove(FileName3)
    print('%s deleted' %(FileName3))   


FunListAllFiles("4.")