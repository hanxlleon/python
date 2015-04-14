# -*- coding: utf-8 -*-
import xlrd
from xml.dom import minidom
import simplejson as json
import re


def get_xls(filename):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    data = {}

    rows = sheet.nrows
    for row in range(rows):
        value = sheet.row_values(row)
        data[value[0]] = value[1:]
    #data = json.dumps(data)
    return data


def write_xml(data):
    doc = minidom.Document()
    root = doc.createElement('root')
    doc.appendChild(root)

    students = doc.createElement('students')
    root.appendChild(students)

    students.appendChild(doc.createComment('\n    学生信息表\n    "id" : [名字, 数学, 语文, 英文]'))

    for i in data:
        data[i][0] = data[i][0].encode('utf-8')

    content = doc.createTextNode('\n{')
    students.appendChild(content)
    for key in data.keys():
        content = doc.createTextNode('\n\t' + str(key) + ': [' )
        students.appendChild(content)
        for value in data[key]:
            content = doc.createTextNode(str(value)+' ')
            students.appendChild(content)
        content = doc.createTextNode(']')
        students.appendChild(content)
    content = doc.createTextNode('\n}')
    students.appendChild(content)
    with open('student.xml', 'w') as f:
        doc.writexml(f, encoding = "utf-8")


if __name__ == '__main__':
    data = get_xls('student.xls')
    write_xml(data)
