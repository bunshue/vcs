#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import json
import sys 
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x
    import ssl
    import urllib.request



url="https://parks.taipei/parks/api/"




req=httplib.Request(url)
try:
    context = ssl._create_unverified_context()
    reponse = httplib.urlopen(url, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
                contents=reponse.read().decode(reponse.headers.get_content_charset())
                contents=contents.replace("\r\n", "")
                print(contents)
        else:  
                contents=reponse.read()   
        data = json.loads(contents)
        for data2 in data:
            print(data2['pm_name'],data2['pm_location'])
except:                                                                 #  處理網路連線異常
    print("error")   