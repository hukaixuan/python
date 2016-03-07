import urllib.request

response = urllib.request.urlopen('http://placekitten.com/1080/700')
cat_img = response.read()

with open('E:\Pictures\cat_1080_800.jpg','wb') as f:
	f.write(cat_img)

