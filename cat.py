from escpos import *

p = printer.Usb(0x0416,0x5011)

p.image("cat.jpg")
