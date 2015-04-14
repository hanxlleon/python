# -*- coding: utf-8 -*-

import re


#读取文件内容
def file_read(filename):
    with open(filename, 'r') as f:
        article = f.read()
    return article


#返回单词列表
def word_list(article):
    words = re.findall(r'[a-zA-Z]+\b', article) #\b可以匹配单词的开头或者结尾
    return words


#返回排序后的单词列表
def word_rate(words):
    w_rate = {}
    for word in words:
        if word in w_rate:
            w_rate[word] += 1
        else:
            w_rate[word] = 1
    li = sorted(w_rate.iteritems(), key=lambda d:d[1], reverse=True)
    return li


if __name__ == '__main__':
    article = file_read('0006.txt')
    words = word_list(article)
    li = word_rate(words)
    print '%s: %s' % li[0]

