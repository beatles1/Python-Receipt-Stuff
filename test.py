from escpos import *

p = printer.Usb(0x0416,0x5011)

p.text("omg\n")
p.text(" \n")
p.text("gmo\n")
p.cut()
