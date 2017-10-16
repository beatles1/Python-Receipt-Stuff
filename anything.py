import time
from escpos import *

p = printer.Usb(0x0416,0x5011)

p.set(align=u'CENTER')
p.text("Memes Inc\n")
p.text("69 The Internet\n")
p.text("\n\n")

p.set(align=u'LEFT')
p.text("You should screenshot this\n")
p.text("and post it on me_irl\n")
p.text("\n\n")

p.set(align=u'RIGHT')
p.text("But this is just\n")
p.text("some text on a\n")
p.text("receipt printer\n")
p.text("\n\n")

p.set(align=u'LEFT')
p.text("Doesn't matter they'll\n")
p.text("upvote anything\n")
p.text("\n\n\n")

time.sleep(4)
p.qr("I miss dat boy :(", size=14)

p.cut()
