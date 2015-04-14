# -*- coding: utf-8 -*-
import xlrd
from xml.dom import minidom
import simplejson as json
import re


def get_xls(filename):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    data = []

    rows = sheet.nrows
    for row in range(rows):
        value = sheet.row_values(row)
        data.append(value)

    #data = json.dumps(data)
    return data


def write_xml(data):
    doc = minidom.Document()
    root = doc.createElement('root')
    doc.appendChild(root)

    students = doc.createElement('numbers')
    root.appendChild(students)

    students.appendChild(doc.createComment('\n    数字信息'))

    content = doc.createTextNode('\n[')
    students.appendChild(content)
    for value in data:
        content = doc.createTextNode('\n\t'+str(value)+', ')
        students.appendChild(content)
    content = doc.createTextNode('\n]\n')
    students.appendChild(content)
    with open('numbers.xml', 'w') as f:
        doc.writexml(f, encoding = "utf-8")


if __name__ == '__main__':
    data = get_xls('numbers.xls')
    write_xml(data)
