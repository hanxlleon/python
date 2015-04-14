# -*- coding: utf-8 -*-

import glob
import re
import os


def file_read(filename):
    expline = blankline = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        n = line.strip()
        if n.startswith('#') or n.startswith("'''") or n.endswith("'''\n"):
            expline += 1
        elif n == '':
            blankline += 1
    return len(lines), expline, blankline


if __name__ == '__main__':
    codeline = expline = blankline = 0
    os.chdir('./code')
    file_list = glob.glob('*')
    for file in file_list:
        (n1, n2, n3) = file_read(file)
        codeline += (n1 - n2 - n3)
        expline += n2
        blankline += n3
    print 'codeline: %d , ecpline: %d, blankline: %d' % (codeline, 
            expline, blankline)

