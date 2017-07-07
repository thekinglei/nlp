#!/usr/bin/env python  
# -*- coding: UTF-8 -*-  
""" 
@version: python2.7.8  
@author: XiangguoSun 
@contact: sunxiangguodut@qq.com 
@file: NBayes_Predict.py 
@time: 2017/2/8 12:21 
@software: PyCharm 

机器学习领域的算法评估有三个基本指标：

· 召回率（recall rate,查全率）：是检索出的相关文档数与文档库中所有相关文档的比率，衡量的是检索系统的查全率
召回率=系统检索到的相关文件/系统所有相关的文件综述

· 准确率（Precision，精度）：是检索出的相关文档数于检索出的文档总数的比率，衡量的是检索系统的查准率
准确率=系统检索到的相关文件/系统所有的检索到的文件数

准确率和召回率是相互影响的，理想情况下是二者都高，但是一般情况下准确率高，召回率就低；召回率高，准确率就低

· F-Score（）：计算公式为：
 

当=1时就是最常见的-Measure
"""  
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')  
  
import cPickle as pickle  
from sklearn.naive_bayes import MultinomialNB  # 导入多项式贝叶斯算法  
  
  
# 读取bunch对象  
def _readbunchobj(path):  
    with open(path, "rb") as file_obj:  
        bunch = pickle.load(file_obj)  
    return bunch  
  
# 导入训练集  
trainpath = "train_word_bag/tfdifspace.dat"  
train_set = _readbunchobj(trainpath)  
  
# 导入测试集  
testpath = "test_word_bag/testspace.dat"  
test_set = _readbunchobj(testpath)  
  
# 训练分类器：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高  
clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)  
  
# 预测分类结果  
predicted = clf.predict(test_set.tdm)  
  
for flabel,file_name,expct_cate in zip(test_set.label,test_set.filenames,predicted):  
    if flabel != expct_cate:  
        #print file_name,": 实际类别:",flabel," -->预测类别:",expct_cate
        #print file_name, "train_corpus/%s/%s.txt"%(expct_cate,expct_cate)
        #print file_name, "train_corpus/%s/model1.txt"%expct_cate
        print file_name.split("/")[2].split('.')[0], expct_cate
print "预测完毕!!!"  
  
# 计算分类精度：  
from sklearn import metrics  
def metrics_result(actual, predict):  
    print '精度:{0:.3f}'.format(metrics.precision_score(actual, predict,average='weighted'))  
    print '召回:{0:0.3f}'.format(metrics.recall_score(actual, predict,average='weighted'))  
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual, predict,average='weighted'))  
  
metrics_result(test_set.label, predicted)
