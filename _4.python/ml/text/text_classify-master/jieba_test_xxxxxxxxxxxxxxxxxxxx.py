import jieba

"""
cut方法有两个参数
1)第一个参数是我们想分词的字符串
2)第二个参数cut_all是用来控制是否采用全模式
"""

txt = "什么是双眼皮整形手术？,双眼皮手术原理？,什么是重睑术？,重睑术手术原理是什么？"

# 精确模式 , 默认就是精确模式
word_list = jieba.cut(txt, cut_all=False)
print(word_list)
for i in word_list:
    print(i)
# print(" ".join(word_list))


# 搜索引擎模式
# word_list = jieba.cut_for_search(txt)
# print("搜索引擎：","".join(word_list))
# 全模式
# word_list = jieba.cut(txt,cut_all=True)
# print("全模式：","|".join(word_list))
