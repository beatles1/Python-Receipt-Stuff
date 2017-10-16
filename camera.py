import picamera, io, time
from escpos import *
from PIL import Image
# Create the in-memory stream
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    time.sleep(2)
    camera.capture(stream, format='jpeg')
# "Rewind" the stream to the beginning so we can read its content
stream.seek(0)
img = Image.open(stream)

if img:
    p = printer.Usb(0x0416,0x5011)

    s = img.size
    if s[0] > 400:
        ratio = 400/s[0]
        img = img.resize((int(s[0]*ratio), int(s[1]*ratio)), Image.ANTIALIAS)

    p.image(img)

    p.cut()
