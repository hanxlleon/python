# -*- coding: utf-8 -*-


with open('filtered_words.txt', 'r') as f:
    line = f.read().decode('utf-8')

words = line.splitlines()
print words
while True:
    input = raw_input('("q":exit) input > ')
    if input == 'q':
        exit()
    for word in words:
        if input.find(word) != -1:
            print 'Freedom'
            break
    else:
        print 'Human Rights'

