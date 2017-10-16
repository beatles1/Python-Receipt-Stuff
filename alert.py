from escpos import *

p = printer.Usb(0x0416,0x5011)

p.text("This is not a drill!")
#DONT FORGET \n U NOOB
