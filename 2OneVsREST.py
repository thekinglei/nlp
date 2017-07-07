#!/usr/bin/env python  
# -*- coding: UTF-8 -*-  
""" 
@version: python2.7.8  
@author: XiangguoSun 
@contact: sunxiangguodut@qq.com 
@file: NBayes_Predict.py 
@time: 2017/2/8 12:21 
@software: PyCharm 
"""  
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')  
  
import cPickle as pickle  
from sklearn.naive_bayes import MultinomialNB  # 导入多项式贝叶斯算法  
from sklearn.multiclass import OneVsRestClassifier as OR
from sklearn.svm import LinearSVC 
  
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
#clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)  
  
# 预测分类结果  
#predicted = clf.predict(test_set.tdm)  
  
#for flabel,file_name,expct_cate in zip(test_set.label,test_set.filenames,predicted):  
#    if flabel != expct_cate:  
#        print file_name,": 实际类别:",flabel," -->预测类别:",expct_cate  

model = OR(LinearSVC(random_state = 10))
print "================="
prd2 = model.fit(train_set.tdm, train_set.label).predict(test_set.tdm)
#print "预测：", prd2
for flabel,file_name,expct_cate in zip(test_set.label,test_set.filenames,prd2):
    if flabel != expct_cate:
        print file_name,": 实际类别:",flabel," -->预测类别:",expct_cate

#print model.fit(train_set.tdm, train_set.label).decision_function(test_set.tdm)
