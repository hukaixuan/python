import urllib.request

def url_open(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0')
	response = urllib.request.urlopen(url)
	html = response.read()
	# print(html)
	return html 


