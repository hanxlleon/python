# -*- coding: utf-8 -*-
#第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random
import os

def random_generater(count=12):
    code = []
    # base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]    
    base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'),ord('F'))]
    for i in range(0, count):
        code.append(random.choice(base))
    return ''.join(code)

if __name__ == '__main__':
    with open('result.txt', 'a') as f:
        for i in range(200):
            f.write(random_generater()+'\n')       


