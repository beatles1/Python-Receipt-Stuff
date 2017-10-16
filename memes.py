import praw, urllib.request, json, io
from escpos import *
from PIL import Image
from resizeimage import resizeimage
from time import gmtime, strftime

# Get meme
r = praw.Reddit(client_id="8ADl1rybRzBn2A", client_secret="mrPczmpce0h5MUtYe-0ypLlStzM", username="irl_me", password="totesirl", user_agent='MemePrinter')

sub = r.subreddit('me_irl')

alreadyDone = []

img = False

try:
	with open('memes_done.json') as json_data:
		alreadyDone = json.load(json_data)
		json_data.close()
except:
	pass

for post in sub.hot(limit=40):
	if post.id not in alreadyDone:
			alreadyDone.append(post.id)

			if ".jpg" in post.url or ".png" in post.url or ".gif" in post.url:
				file = io.BytesIO(urllib.request.urlopen(post.url).read())
				img = Image.open(file)

				break

try:
	file = open('memes_done.json', "w")
	json.dump(alreadyDone, file)
	file.close()
except:
	pass

# Print meme
if img:
	s = img.size
	if s[0] > 400:
		ratio = 400/s[0]
		img = img.resize((int(s[0]*ratio), int(s[1]*ratio)), Image.ANTIALIAS)
	
	print(img.size)
	p = printer.Usb(0x0416,0x5011)

	p.text("Fresh Meme at" + strftime("%H:%M:%S %d-%m-%Y ", gmtime()) + "\n")

	p.image(img)

	p.cut()
