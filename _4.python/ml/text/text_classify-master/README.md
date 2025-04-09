##文本分类

###文本分词
* ci_seg.py  文本分词
	- 分词：jieba
	- 文本编码问题：统一utf-8编码

###转为bunch对象
* to_bunch.py 分词后的预料库转为bunch
	- bunch对象
		* target_name:是一个list，存放的是整个数据集的类别集合。
		* label:是一个list，存放的是所有文本的标签。
		* filenames:是一个list，存放的是所有文本文件的名字。
		* contents:是一个list，分词后文本文件词向量形式

###词向量空间
* tfidf_train.py
    - bunch_path = "train_word_bag/train_set.dat"  #导入训练集Bunch的路径  
    - space_path = "train_word_bag/tfdifspace.dat"  # 词向量空间保存路径  
* tfidf_test.py
    - bunch_path = "test_word_bag/test_set.dat"   # 导入训练集Bunch的路径  
    - space_path = "test_word_bag/testspace.dat"   # 词向量空间保存路径

###分类器
*select_test.py
