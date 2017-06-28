#!/usr/local/env python
#--*-- coding:utf-8 --*--
#功能：分词
import jieba


FILE_NAME = './source.txt'
def fenci(filename):
    fp = file(filename, 'r')
    fp2 = file("./tmp1.txt", "a+")
    comments = fp.readlines()
    for i in comments:

        tmp = list(jieba.cut(i))  #分词
        for j in tmp:
            print j
            fp2.write(j.encode("utf8"))
            fp2.write(" ")
        print '-----------'
    fp.close()
    fp2.close()
if __name__ == "__main__":
    fenci(FILE_NAME)


