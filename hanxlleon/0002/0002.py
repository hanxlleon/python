# -*- coding: utf-8 -*-
#将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import MySQLdb

def file_read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    for i in range(200):
        lines[i] = lines[i].strip()
    return lines

def mysql_write():
    lines = file_read('result.txt')
    conn = MySQLdb.connect(host='localhost',user='root', passwd='1', db='test', port=3306, charset='utf8')
    cursor = conn.cursor()
    cursor.execute('create table promo_code(id int(3) primary key, number varchar(12))')
    for i in range(200):
        cursor.execute('insert into promo_code (id, number) values(%s, %s)', [i+1, lines[i]])
    conn.commit()
    cursor.close()
    conn.close()
    print 'finish'


if __name__ == '__main__':
    mysql_write()
