from escpos import *

p = printer.Usb(0x0416,0x5011)

with open("pi.txt", "r") as file:
	for line in file.readlines():
		p.text(line + "\n")

