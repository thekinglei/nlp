#!/usr/local/env python
#--*-- coding:utf-8 --*--
#分词:分词时标注词性
from __future__ import print_function
import math
import sys
import jieba

jieba.load_userdict("userdict.txt")

data = {}
total = 0
with open("source.txt") as f:
    for line in f:
        line = line.decode("utf-8")
        words = [w for w in jieba.cut(line) if w in jieba.dt.FREQ]

        for word in words:
            data[word] = data.get(word, 0.0) + 1.0
data = [(k, math.log(total / v)) for k, v in data.iteritems()]
for k, v in data:
    print(k.encode("utf-8"), v)


