#!/usr/local/env python
#--*-- coding:utf-8 --*--
#分词:分词时标注词性
import jieba

#标注词性需要这个模块
#from jieba import analyse
from jieba import posseg

FILE_NAME = './source.txt'
def fenci(filename):
    fp = file(filename, 'r')
    fp2 = file("./tmp3.txt", "a+")
    comments = fp.readlines()
    for i in comments:

#与my_fenci.py基本一致，默认cut_all是False
        tmp = jieba.cut(i, cut_all=False)
        for j in tmp:
            print j
            fp2.write(j.encode("utf8"))
            fp2.write(" ")
        print '-----------'
    fp.close()
    fp2.close()
if __name__ == "__main__":
    fenci(FILE_NAME)


