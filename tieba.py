import urllib.request
import re

def open_url(url):
	req =  urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0')
	response = urllib.request.urlopen(req)
	html = response.read()
	return html 

def get_img(html):
	# print(html) 
	html = html.decode('utf-8')
	mode = re.compile(r'src="(http://imgsrc.baidu.com/[^"]+\.jpg)"')
	img_list = mode.findall(html)
	for each in img_list:
		filename = each.split('/')[-1]
		with open('E:/Pictures/tieba/'+filename, 'wb') as f:
			img = open_url(each)
			f.write(img)

if __name__ == '__main__':
	url = 'http://tieba.baidu.com/p/2177168441'
	get_img(open_url(url))




