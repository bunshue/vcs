#coding=utf-8
import sys  
import os  
import jieba  
import chardet

 
# 保存至文件  
def savefile(savepath, content):  
    with open(savepath, "wb") as fp:  
        fp.write(content)  

# 读取文件  
def readfile(path):  
    with open(path, "rb") as fp:  
        content = fp.read()
        cod=chardet.detect(content)['encoding']
    return content.decode(cod)
  
def corpus_segment(train_set, seg_path):  

    #catelist = os.listdir(corpus_path)  # 获取corpus_path下的所有子目录  
    catelist=train_set.keys()
    for myclass in catelist:  
        ''''' 
        这里mydir就是train_corpus/art/21.txt中的art（即catelist中的一个类别） 
        '''  

        seg_dir = seg_path + str(myclass) + "/"  # 拼出分词后存贮的对应目录路径如：train_cor       art/  
  
        if not os.path.exists(seg_dir):  # 是否存在分词目录，如果没有则创建该目录  
            os.makedirs(seg_dir)  
  
        file_list = train_set[myclass]  # 获取未分词语料库中某一类别中的所有文本
        file_num=0  
        for content in file_list:  # 遍历类别目录下的所有文件 
            file_name=str(file_num)+'.txt' 
            content = content.replace("\r\n", "")  # 删除换行  
            content = content.replace(" ", "")#删除空行、多余的空格  
            content_seg = jieba.cut(content)  # 为文件内容分词  
            savefile(seg_dir + file_name, " ".join(content_seg).encode()) 
            file_num+=1
  
    print("中文语料分词结束！！！") 

def corpus_test(corpus_path, seg_path):  
    ''''' 
    corpus_path是未分词语料库路径 
    seg_path是分词后语料库存储路径 
    '''  
    catelist = os.listdir(corpus_path)  # 获取corpus_path下的所有子目录  
    ''''' 
    其中子目录的名字就是类别名，例如： 
    train_corpus/art/21.txt中，'train_corpus/'是corpus_path，'art'是catelist中的一个成员 
    '''  
  
    # 获取每个目录（类别）下所有的文件  
    for mydir in catelist:  
        ''''' 
        这里mydir就是train_corpus/art/21.txt中的art（即catelist中的一个类别） 
        '''  
        class_path = corpus_path + mydir + "/"  # 拼出分类子目录的路径如：train_corpus/art/  
        seg_dir = seg_path + mydir + "/"  # 拼出分词后存贮的对应目录路径如：train_corpus_seg/art/  
  
        if not os.path.exists(seg_dir):  # 是否存在分词目录，如果没有则创建该目录  
            os.makedirs(seg_dir)  
  
        file_list = os.listdir(class_path)  # 获取未分词语料库中某一类别中的所有文本  
        ''''' 
        train_corpus/art/中的 
        21.txt, 
        22.txt, 
        23.txt 
        ... 
        file_list=['21.txt','22.txt',...] 
        '''  
        for file_path in file_list:  # 遍历类别目录下的所有文件  
            fullname = class_path + file_path  # 拼出文件名全路径如：train_corpus/art/21.txt  
            content = readfile(fullname)  # 读取文件内容

            '''''此时，content里面存贮的是原文本的所有字符，例如多余的空格、空行、回车等等， 
            接下来，我们需要把这些无关痛痒的字符统统去掉，变成只有标点符号做间隔的紧凑的文本内容 
            '''  
            content = content.replace("\r\n", "")  # 删除换行  
            content = content.replace(" ", "")#删除空行、多余的空格  
            content_seg = jieba.cut(content)  # 为文件内容分词  
            savefile(seg_dir + file_path, (" ".join(content_seg)).encode('utf-8')) # 将处理后的文件保存到分词后语料目录  
  
    print("中文语料分词结束！！！") 

if __name__=="__main__":  
    #对训练集进行分词  
    '''
    1:品牌
    2:价格
    3:项目简介
    4:效果
    '''
    train_set={
        1:["厨房橱柜","无锡装修公司","月星家居","实木床","青山厨柜","实木复合地板","无锡建材市场在哪里","无锡华夏家居港","实木门","华夏家居港","木门十大名牌有哪些","橱柜品牌","瓷砖品牌","地板品牌","东鹏瓷砖","复合地板十大排名","樱花木门是几线品牌","马桶品牌排行榜","国内十大马桶品牌","十大卫浴品牌"],
        2:["实木门价格","红酸枝家具价格","一套威法橱柜要多少钱","无锡双11建材那里有优惠活动","木地板价格","优格橱柜多少钱一平米","橡木地板的价格","红酸枝家具大降价","一般实木门价格","整体卫生间价格多少","toto马桶价格","toto智能马桶价格","索非亚衣柜价格","白酸枝一套家具多少钱","红酸枝的价格","无锡买家具哪里便宜"],
        3:["无锡家装节2017","无锡家装节","家博会","无锡家装博览会","无锡家博会","无锡2012年10月15日家博会","2017无锡家装博览会","2017无锡新体家装节","无锡建材团购活动","无锡新体家装节","兔狗家装节","无锡广电家博会","无锡广电家装节2017","家装节","2017无锡家装节","2017无锡广电家装节","无锡家博会2017","无锡家装博览会2016","2017无锡家装节时间","2017无锡太湖博览中心家装节"],
        4:["卫生间装修效果图","客厅装修效果图","装修效果图","客厅背影墙装修效果图","地板砖效果图","窗帘效果图","复式楼装修效果图","餐厅装修效果图","开放式厨房装修效果图","装潢效果图"]}

    seg_path = "./clickplus_train_seg/"  # 分词后分类语料库路径  
    corpus_segment(train_set,seg_path)  
    #对测试集进行分词  
    #test_set = "./clickplus_test_new/"  # 未分词分类语料库路径  
    #seg_path = "./clickplus_test_seg/"  # 分词后分类语料库路径  
    #corpus_segment(corpus_path,seg_path)  