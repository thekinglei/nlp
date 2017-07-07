#!/bin/bash
set -e -x
[[ -d "./test_corpus_seg/" ]] && { rm ./test_corpus_seg/* -rf; }
[[ -d "./test_word_bag" ]] && { rm ./test_word_bag/* -rf; }
python fenlei.py #跑训练集分词
python fenci.py
python fenlei_2.py
python fenlei_5.py
python fenlei_6.py

