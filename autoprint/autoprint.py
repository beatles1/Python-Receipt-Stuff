import io
from PIL import Image
from os import walk, remove
from escpos import *

p = printer.Usb(0x0416,0x5011)

dir = "/home/pi/receipt/autoprint/"

files = []
for (dirpath, dirnames, filenames) in walk(dir):
    files.extend(filenames)
    break

for f in files:
    if ".txt" in f:
        with open(dir + f, 'r') as txtFile:
            data = txtFile.read()
            p.text(data + "\n")
            p.cut()
            remove(dir + f)
    elif ".png" in f or ".jpg" in f or ".gif" in f:
        with open(dir + f, 'rb') as imgFile:
            data = io.BytesIO(imgFile.read())
            img = Image.open(data)
            if img:
                s = img.size
                if s[0] > 400:
                    ratio = 400/s[0]
                    img = img.resize((int(s[0]*ratio), int(s[1]*ratio)), Image.ANTIALIAS)
                p.image(img)
                p.cut()
                remove(dir + f)


