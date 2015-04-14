# -*- coding: utf-8 -*-
#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
#iphone5的分辨率为1136x640像素

from PIL import Image

def change_image_size(image_path='0005.jpg', size=(1136, 640)):
    im = Image.open(image_path)
    im.thumbnail((1136, 640), Image.ANTIALIAS)
    #im2 = im.resize(size)
    #im2.save('result-' + image_path)
    im.save('result-' + image_path)

if __name__ == '__main__':
    change_image_size('0005.jpg')

