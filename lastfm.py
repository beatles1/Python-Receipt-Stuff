import urllib.request, json, io, xmltodict
from escpos import *
from PIL import Image
from resizeimage import resizeimage
from time import gmtime, strftime, sleep

while True:
    xml = io.BytesIO(urllib.request.urlopen('https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=edwardbowden&api_key=401ae78cee1da128562cdf3899a9b203&limit=5').read())
    plays = xmltodict.parse(xml)

    last = False
    try:
    	with open('lastlastfm.txt') as lastdata:
    		last = lastdata.read()
    except:
    	pass

    this = False
    try:
        this = plays['lfm']['recenttracks']['track'][0]['image'][3]['#text']
        this = this.replace('300x300', '400x400')
    except:
        pass

    if (this and not (last == this)):
        print(plays['lfm']['recenttracks']['track'][0]['name'] + ' - ' + plays['lfm']['recenttracks']['track'][0]['artist']['#text'])
        try:
        	file = open('lastlastfm.txt', "w")
        	file.write(this)
        	file.close()
        except:
        	pass

        file = io.BytesIO(urllib.request.urlopen(this).read())
        img = Image.open(file)

        if img:
                s = img.size
                if s[0] > 400:
                        ratio = 400/s[0]
                        img = img.resize((int(s[0]*ratio), int(s[1]*ratio)), Image.ANTIALIAS)

                p = printer.Usb(0x0416,0x5011)

                #p.text("Now playing at " + strftime("%H:%M:%S %d/%m/%y ", gmtime()) + "\n")
                p.text(plays['lfm']['recenttracks']['track'][0]['name'] + ' - ' + plays['lfm']['recenttracks']['track'][0]['artist']['#text'] + "\n")

                p.image(img)

                p.cut()
    sleep(2)
