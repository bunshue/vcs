# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import sys
import jieba
import jieba.analyse
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

try:
    url="http://www.powenko.com/wordpress/"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents=reponse.read().decode(reponse.headers.get_content_charset())
        else:
            contents=reponse.read()
        #print(contents)

        #print(",".join(jieba.analyse.extract_tags(contents, topK=1000)))
        jieba.analyse.set_stop_words("stop_words.txt")
        #print(",".join(jieba.analyse.extract_tags(contents, topK=1000)))

        dic = {}
        #keywords = jieba.analyse.extract_tags(contents, topK=40, withWeight=True, allowPOS=())
        keywords = jieba.analyse.extract_tags(contents, topK=100, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
        for item in keywords:
            if (sys.version_info > (3, 0)):
                print(" %s =  %f  %s "  %  (item[0], item[1],flag))
            else:
                print(" %s =  %f  " % (item[0].encode('utf_8'), item[1] ))
        print("="*40)
        words =jieba.posseg.cut(contents)
        for word, flag in words:
            if flag=="ns" or flag=="n" or flag=='vn' or flag=='n':
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] = dic[word] + 1
        for w in sorted(dic, key=dic.get, reverse=True):
            if dic[w]>1:
               print("%s  %i " % (w, dic[w]))

except:
    print("error")

