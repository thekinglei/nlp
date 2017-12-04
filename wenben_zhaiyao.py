#coding=utf-8
import jieba
import jieba.analyse
from optparse import OptionParser
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
TRAIN_DATA="/root/train_corpus_seg"
DSET_DATA="/data/zhaiyao_train_corpus_seg"
jieba.initialize()
jieba.load_userdict("./dict.txt")
jieba.analyse.set_stop_words('stop_words.txt')
import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence

#tr4w = TextRank4Keyword()
#tr4w.analyze(text=content,lower=True,window=2)
#content = open("ooo").read()
tr4s = TextRank4Sentence(stop_words_file='stop_words.txt')
#tr4s.analyze(text=content,lower=True,source="all_filters")

news = os.listdir(TRAIN_DATA)
for i in news:
    files = os.listdir(TRAIN_DATA + "/" + i )
    for j in files:
        with open(TRAIN_DATA + "/" + i + '/' + j, "rb") as tmp_s, open(DSET_DATA + "/" + i + '/' + j, "w+") as tmp_d:
            content = tmp_s.read().replace(" ","")
            tr4s.analyze(text=content,lower=True,source="all_filters")
            all_sentence = ""
            for item in tr4s.get_key_sentences(num=3):
                all_sentence += item.sentence + " "
            tmp_d.write(all_sentence)
