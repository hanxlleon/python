# -*- coding: utf-8 -*-
import xlwt
import simplejson as json 
import os


def get_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_xls(filename, data):
    book = xlwt.Workbook(encoding='utf-8')
    sheetname = os.path.splitext(os.path.split(filename)[1])[0] # 提取文件名（不带格式），用于表名
    sheet = book.add_sheet(sheetname, cell_overwrite_ok=True)

    dataitems = sorted(data.iteritems(), key=lambda d:d[0]) # 将字典排序，保存为列表

    row, col = 0, 0
    for (key, value) in dataitems:
        sheet.write(row, col, key)
        col += 1
        sheet.write(row, col, value)
        col += 1

        row += 1
        col = 0
    book.save(filename)


if __name__ == '__main__':
    data = get_json('city.txt')
    write_xls('city.xls', data)
