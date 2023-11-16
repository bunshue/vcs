# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import sys
from os import path
import jieba
import jieba.analyse
d = path.dirname(__file__)
text = """柯博文老師和我們喜歡去甜心一點DIY烘焙坊做蛋糕"""
jieba.load_userdict(path.join(d, 'userdict.txt'))
if (sys.version_info > (3, 0)):
  content = text
else:
  content = text.decode('utf_8')
print(",".join(jieba.analyse.extract_tags(text, topK=10)))
jieba.analyse.set_stop_words("stop_words.txt")
print(",".join(jieba.analyse.extract_tags(text, topK=10)))


print(' default idf'+'-'*40)
keywords = jieba.analyse.extract_tags(text, topK=10, withWeight=True, allowPOS=()) #topK=TF/IDF 
print(" topK=TF/IDF , TF=%d" % len(keywords))
for item in keywords:
    if (sys.version_info > (3, 0)):
        print(" %s =  %f "  %  (item[0], item[1]))      # 分別為關鍵詞和相應的權重
    else:
        print(" %s =  %f " % (item[0].encode('utf_8'), item[1]))     # 關鍵詞和權重


print('set_idf_path'+'-'*40)
jieba.analyse.set_idf_path("idf.txt")
keywords = jieba.analyse.extract_tags(text, topK=10, withWeight=True, allowPOS=())
for item in keywords:
    if (sys.version_info > (3, 0)):
        print("  %s   TF=%f , IDF=%f  topK=%f" % (item[0], item[1], len(keywords)*item[1], item[1]*len(keywords)*item[1]))      # 分別為關鍵詞和相應的權重
    else:
        print(" %s   TF=%f , IDF=%f  topK=%f" % (item[0].encode('utf_8'), item[1],len(keywords)*item[1], item[1]*len(keywords)*item[1]))     # 關鍵詞和權重