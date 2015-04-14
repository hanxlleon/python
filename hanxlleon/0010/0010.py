# -*- coding: utf-8 -*-
import Image, ImageDraw, ImageFont, ImageFilter
import random
import string


class Idcode:
    def __init__(self, width=240, height=60, fontsize=36, fontcnt=4):
        self.width = width
        self.height = height
        self.fontsize = fontsize
        self.fontcnt = fontcnt

    def rand_char(self):
        return random.choice(string.uppercase)

    def rand_bgcolor(self):
        return (random.randint(64, 255), random.randint(64, 255), 
                random.randint(64, 255))

    def rand_fontcolor(self):
        return (random.randint(32, 127), random.randint(32, 127), 
                random.randint(32, 127))

    def generate_code(self, name='image.jpg'):
        image = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        font = ImageFont.truetype('Arial.ttf', self.fontsize) #创建font
        draw = ImageDraw.Draw(image) # 创建draw

        for x in range(self.width):
            for y in range(self.height):
                draw.point((x, y), fill=self.rand_bgcolor())

        for t in range(self.fontcnt):
            draw.text(((60 * t + 10, 10)), self.rand_char(), font=font, fill=self.rand_fontcolor())

        image = image.filter(ImageFilter.BLUR)
        image.save(name, 'jpeg')


if __name__ == '__main__':
    Idcode().generate_code('4image.jpg')
    Idcode(360, 60, 36, 6).generate_code('6image.jpg')
