# -*- coding: utf-8 -*-
#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
#iphone5的分辨率为1136x640像素

from PIL import Image
import glob, os

def search_imgfile(path):
    abspath = os.path.abspath(path)
    return glob.glob(os.path.join(abspath, '*.jpg'))

def change_image_size(filename, size=(1136, 640)):
    im = Image.open(filename)
    im.thumbnail(size, Image.ANTIALIAS)
    #s_w, s_h = im.size
    #ratio = min(size[0]/s_w, size[1]/s_h)
    #im2 = im.resize((s_w*ratio, s_h*ratio), Image.ANTIALIAS)
    #im2.save('result-' + image_path)
    (path, imgname) = os.path.split(filename)
    savedname = str(size[0])+'_'+str(size[1])+'_'+imgname
    im.save(os.path.join(path, savedname))

if __name__ == '__main__':
    imgfiles = search_imgfile('img')
    for img in imgfiles:
        change_image_size(img)
        change_image_size(img, size=(1334, 750))
        change_image_size(img, size=(2208, 1242))

