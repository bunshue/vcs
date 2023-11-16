# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import sys 
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x
try:
    url="http://www.powenko.com/download_release/get.php?name=powenko"
    #url="http://data.taipei/opendata/datalist/datasetMeta/download?id=5bc82dc7-f2a2-4351-abc8-c09c8a8d7529&rid=1f1aaba5-616a-4a33-867d-878142cac5c4"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents=reponse.read().decode(reponse.headers.get_content_charset())
        else:  
        	contents=reponse.read()   
        print(contents)
except:
    print("error")   