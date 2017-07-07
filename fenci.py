#!/usr/bin/env python  
# -*- coding: UTF-8 -*-  
""" 
@version: python2.7.8  
@author: XiangguoSun 
@contact: sunxiangguodut@qq.com 
@file: corpus_segment.py 
@time: 2017/2/5 15:28 
@software: PyCharm 
"""  
import sys  
import os  
import jieba  
# 配置utf-8输出环境  
reload(sys)  
jieba.load_userdict( "dict.txt" )
sys.setdefaultencoding('utf-8')  
# 保存至文件  
def savefile(savepath, content):  
    with open(savepath, "wb") as fp:  
        fp.write(content)  
    ''''' 
    上面两行是python2.6以上版本增加的语法，省略了繁琐的文件close和try操作 
    2.5版本需要from __future__ import with_statement 
    新手可以参考这个链接来学习http://zhoutall.com/archives/325 
    '''  
# 读取文件  
def readfile(path):  
    with open(path, "rb") as fp:  
        content = fp.read()  
    return content  
  
def corpus_segment(companies_file, seg_dir):  
    ''''' 
    corpus_path是未分词语料库路径 
    seg_path是分词后语料库存储路径 

    '''  
    fp = open(companies_file,'r')
    content = fp.readlines()
    len_content = len(content)
    if not os.path.exists(seg_dir + "classless"):
        os.makedirs(seg_dir + "classless") 
    for i in range(len_content):
        tmp = content[i].replace("\n", "")
        tmp = tmp.replace(" ", "")
        tmp_seg = jieba.cut(tmp)
        savefile(seg_dir + "classless/" + str(i) + '.txt', " ".join(tmp_seg))
    print "中文语料分词结束！！！"  
  
''''' 
如果你对if __name__=="__main__":这句不懂，可以参考下面的文章 
http://imoyao.lofter.com/post/3492bc_bd0c4ce 
简单来说如果其他python文件调用这个文件的函数，或者把这个文件作为模块 
导入到你的工程中时，那么下面的代码将不会被执行，而如果单独在命令行中 
运行这个文件，或者在IDE（如pycharm）中运行这个文件时候，下面的代码才会运行。 
即，这部分代码相当于一个功能测试。 
如果你还没懂，建议你放弃IT这个行业。 
'''  
if __name__=="__main__":  
    #对训练集进行分词  
    #corpus_path = "./train_corpus/"  # 未分词分类语料库路径  
    #seg_path = "./train_corpus_seg/"  # 分词后分类语料库路径  
    #corpus_segment(corpus_path,seg_path)  
  
    #对测试集进行分词  
    #corpus_path = "./test_corpus/"  # 未分词分类语料库路径  
    seg_path = "./test_corpus_seg/"  # 分词后分类语料库路径  
    corpus_segment("company.txt",seg_path) 
