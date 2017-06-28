# nlp
自然语言处理：中文分词，打标签，文章匹配相似度

打标签：
extra_tags.py：

关键函数：extarct_tags ，通过help(jieba.analyse.extarct_tags) 查看

函数提示如下：

withWeight：单词权重

allowPOS：单词性质，参看https://wenku.baidu.com/view/49eab3a9ad51f01dc281f1f8.html

withFlag：


======================================================

Help on method extract_tags in module jieba.analyse.tfidf:

extract_tags(self, sentence, topK=20, withWeight=False, allowPOS=(), withFlag=False) method of jieba.analyse.tfidf.TFIDF instance

    Extract keywords from sentence using TF-IDF algorithm.
    
    Parameter:
    
        - topK: return how many top keywords. `None` for all possible words.
        
        - withWeight: if True, return a list of (word, weight);
        
                      if False, return a list of words.
                      
        - allowPOS: the allowed POS list eg. ['ns', 'n', 'vn', 'v','nr'].
        
                    if the POS of w is not in this list,it will be filtered.
                    
        - withFlag: only work with allowPOS is not empty.
        
                    if True, return a list of pair(word, weight) like posseg.cut
                    
                    if False, return a list of words

