#!/usr/bin/env python
#coding:utf-8
import csv

company_file = open("company.txt", "r")
src_file = open("result3.txt")
tag_file =  open("tag.csv")

company_info = company_file.readlines()
tags = tag_file.readlines()
src_contents = src_file.readlines()
print tags
print src_contents
'''
for i in src_contents:
    tmp = i.split(" ")
    content = open("../" + tmp[0], "rb").read()
    tag_num = int(tmp[1].split("\n")[0])
    tmp_str = content + ',' + tags[tag_num - 1]
    dest_file.write(tmp_str)
'''
tag_name = []
for i in src_contents:
    tmp = i.split(" ")
    tag_num = int(tmp[1].split("\n")[0])
    tag_name.append(tags[tag_num-1])

csvfile = open('finally.csv', 'w')
writer = csv.writer(csvfile)
for i in range(len(company_info)):
    tmp = []
    tmp.append(company_info[i].split("\n")[0])
    tmp.append(tag_name[i].split('\n')[0])
    writer.writerow(tmp)
#dataframe = pd.DataFrame({'company_name':company_info,'tags':tag_name})
#dataframe.to_csv("wl.csv","index=False", sep="")
src_file.close()
tag_file.close()
