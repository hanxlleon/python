# -*- coding: utf-8 -*-
#第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import redis


def file_read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    for n in range(200):
        lines[n] = lines[n].strip()
    return lines

def redis_write():
    lines = file_read('result.txt')
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for n in range(200):
        key = str(n+1)
        value = str(lines[n])
        r.set(key, value)
    r.save()
    print 'finish'

if __name__ == '__main__':
    redis_write()
