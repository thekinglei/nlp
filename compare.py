#!/usr/bin/env python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint

import jieba
from collections import defaultdict
f1=open('./source.txt','r+').read()
f2=open('./source2.txt','r+').read()
data1 = jieba.cut(f1)
data2 = jieba.cut(f2)
data1_words = ''
data2_words = ''
for word in data1:
    data1_words += word+" "
for word in data2:
    data2_words += word+" "
documents = [data1_words,data2_words]
texts = [[word for word in document.split()]
         for document in documents] # 遇到这样的代码，我们阅读的规则是遵循从右往左，先看最外面的for循环，z再看里面的for循环


frequency = defaultdict(int)   # 使用默认字典
for text in texts:      # 下面2行代码是计算每个词的频数。方便下面的代码去除频数少的单词
    for token in text:
        frequency[token] = +1

dictionary = corpora.Dictionary(texts)
print dictionary
print type(dictionary)
dictionary.save('./dictionary.txt')

# texts = [[word for word in text if frequency[token] > 1]
#          for text in texts]   # 去除频数少于1的词语，  内循环是先走if判断，再走循环
texts = [[word for word in text ]
         for text in texts]
f3=open('./source3.txt','r+').read()
data3=jieba.cut(f3)
data3_words =''
for item in data3:
    data3_words += item+' '
new_vec = dictionary.doc2bow(data3_words.split())    # 建立向量
corpus = [dictionary.doc2bow(text) for text in texts]   # 建立新的语料库
corpora.MmCorpus.serialize("./XinYU.mm",corpus)  # 存新的语料库
tfidf = models.TfidfModel(corpus)   # 建立tfidf模型
featureNum = len(dictionary.token2id.keys())   # 通过token2id得到特征数
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)   #稀疏矩阵相似度，从而建立索引
sim = index[tfidf[new_vec]]    # 计算最终相似度结果
print type(sim)
print(sim)
