#/usr/bin/env python
#--*-- coding:utf-8 --*--
import sys
#sys.path.append('../')
#功能:关键字提取
#topK为返回几个TF/IDF权重最大的关键词，默认值为10
#打印关键字及其权重
#调整关键字频率的默认权重，通过自定义字段实现
import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python extract_tags.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

content = open(file_name, 'rb').read()

jieba.initialize()
jieba.set_dictionary("./dict.txt")


tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
for i in tags:
    print i[0], "  ", i[1]
#print(",".join(tags))
