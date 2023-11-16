#!/usr/bin/env python
# coding=utf8
__author__ = "Powen Ko, www.powenko.com"
import sys
try:
    import urllib
    import urllib2 as httplib   #  python 2.x
except Exception:
    import urllib.request as httplib  # python 3.x

try:
    url="http://www.powenko.com/download_release/post.php"
    values={'name':'powenko','password':123}
    if (sys.version_info < (3, 0)):       # python 2.x
        data = urllib.urlencode(values)
        req = httplib.Request(url, data)
        reponse = httplib.urlopen(req)
        if reponse.code == 200:
            contents=reponse.read()
    else:
        data = urllib.parse.urlencode(values)      # python 3.x
        data = data.encode('utf-8')  # data should be bytes
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            contents = response.read().decode(response.headers.get_content_charset())
    print(contents)
except:
    print("error")   