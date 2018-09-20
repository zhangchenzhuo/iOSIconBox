#!usr/bin/env python3
# -*- coding: utf-8 -*-

from  __future__ import print_function
import sys, re, os
from PIL import Image

sysargs = sys.argv

if len(sysargs) <= 1:
    print('ERROR!!!!IMAGE NOT FOUND! need image file path')
    exit(-1)

t = (
     '20@1x',
     '20@2x',
     '20@3x',
     '29@1x',
     '29@2x',
     '29@3x',
     '40@1x',
     '40@2x',
     '40@3x',
     '60@2x',
     '60@3x',
     '76@1x',
     '76@2x',
     '83.5@2x',
     '1024@1x',
     )

imgpath = sysargs[1]
dirpath = os.path.join(os.path.split(imgpath)[0], 'pyappicons')

# 自动生成ios所需要的图片
def getsize(str):
    m = re.match(r'^([\d.]*)@(\d*)x$', str)
    b = int(float(m.group(1)) * float(m.group(2)))
    return b, b


def resize_image(img, size):
    return img.convert('RGB').resize(size, resample=Image.HAMMING)

try:
    with Image.open(imgpath) as originimg:

        size_tuple = tuple(getsize(string) for string in t)
        for idx, val in enumerate(size_tuple):
            size = val
            newImage = resize_image(originimg, size)
            if not os.path.isdir(dirpath):
                os.mkdir(dirpath, 0o777)
            newImage.save(os.path.join(dirpath, 'AppIcon' + t[idx] + '.png'))

except IOError as e:
    print(f'cannot create image {e}')
