# -*- coding: utf-8 -*-
#第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果

from PIL import Image, ImageDraw, ImageFont

def addNum(filePath):
    img = Image.open(filePath)
    size = img.size
    fontSize = size[1] / 4
    draw = ImageDraw.Draw(img)

    ttFont = ImageFont.truetype("arial.ttf", fontSize)
    draw.text((size[0]-fontSize, 0), "8", (256,0,0), font=ttFont)
    del draw
    img.save('./result.jpg')
    img.show()


if __name__ == '__main__':
    addNum("image.jpg")
