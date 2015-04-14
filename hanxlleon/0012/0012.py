# -*- coding: utf-8 -*-
import re


with open('filtered_words.txt', 'r') as f:
    lines = f.read().decode('utf-8')

words = '|'.join(lines.splitlines())
while True:
    input = raw_input('("q":exit) input > ')
    if input == 'q':
        exit()
    #for word in words:
    print re.sub(words, '**', input)

