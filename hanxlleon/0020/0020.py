# -*- coding:utf-8 -*-
import xlrd
import re


def get_time(filename):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    timelist = sheet.col_values(4)

    sum = 0
    for t in timelist[1:]:
        time = re.findall(r'\d+', t) # 找出中文日期中的数字
        for i, s in enumerate(time[::-1]): # 将时、分、秒反转为秒、分、时
            sum += int(s) * 60 ** int(i)
    return sum


if __name__ == '__main__':
    seconds = get_time('order.xls')
    print '一共%s秒' % seconds
