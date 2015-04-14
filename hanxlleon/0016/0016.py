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

    dataitems = sorted(data)

    row, col = 0, 0
    for list in dataitems:
        for value in list:
            sheet.write(row, col, value)
            col += 1
        row += 1
        col = 0
    book.save(filename)


if __name__ == '__main__':
    data = get_json('numbers.txt')
    write_xls('numbers.xls', data)
