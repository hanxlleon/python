# -*- coding: utf-8 -*-
#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

def counter(string):
    ignore = [',', '.', ':', '!', '?', '“', '”', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in ignore:
        string = string.replace(i, ' ')
    words = string.lower().split()
    dic = {}
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

def file_read(filename):
    with open(filename, 'r') as f:
        lines = f.read()
    return lines

if __name__ == '__main__':
    lines = file_read('0004.txt')
    item_dic = counter(lines)
    for k, v in item_dic.items():
        print k, v


