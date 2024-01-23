#!/usr/bin/env python
import os
import os.path
import requests
import glob
from PIL import Image, ImageDraw

url = 'https://images.ygoprodeck.com/images/cards/'
listImg = list()
x = 396
y = 241
size = (693, 1013)
card_count = 0
page_count = 0
file_n = "print: "
with open ("Builder Deck.ydk", "r") as myfile:
    for line in myfile:
        a = line.strip()
        if a.isdigit():
            listImg.append(a+".jpg")
            a = url+a+".jpg"
            filename = a.split('/')[-1]
            r = requests.get(a, allow_redirects=True)
            with open(filename, 'wb') as f:
                f.write(r.content)



