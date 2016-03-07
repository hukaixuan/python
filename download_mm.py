import urllib.request
import re

def url_open(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0')
	response = urllib.request.urlopen(req)
	html = response.read()
	# print(html)
	return html 


# 返回当前页面的页面值
def get_page_num(url):
	html = url_open(url).decode('utf-8')
	# mode = re.compile(r'current-comment-page*/d{1,}')
	# page = ((mode.findall(html)[0]).split('['))[0]
	a = html.find('current-comment-page')+23
	b = html.find(']',a)
	page = html[a:b]
	return int(page)
	

def find_imgs(url):
	html = url_open(url).decode('utf-8')
	img_paths = []
	# a = html.find('img src=')
	# while a!=-1:
	# 	b = html.find('.jpg', a ,a+255)
	# 	if b != -1 :
	# 		img_paths.append(html[a+9:b+4])
	# 	else:
	# 		b = a+9
	# 	a = html.find('img src=', b)
	# 	print('a的返回值：'+str(a)+'\n' )
	mode = re.compile(r'src="(.+?\.jpg)"')   #捕获型括号获得实际匹配的文本，
	img_paths = mode.findall(html)
	# print(img_paths)
	return img_paths


def save_img(floder, img_paths):
	for each in img_paths:
		filename = each.split('/')[-1]
		with open(floder+filename, 'wb') as f:
			img = url_open(each)
			# print(each)
			f.write(img) 

# floder为图片保存路径，pages为下载的页数
def download_mm(floder='E:\Pictures\mm/', pages=15):
	url = 'http://jandan.net/ooxx/'
	page_now = get_page_num(url)
	for i in range(pages):
		page_now -= 1
		print('正在从第'+str(page_now)+'页下载')
		url = 'http://jandan.net/ooxx/'+'page-'+str(page_now)+'#comments'
		print('downloading from '+url)
		img_paths = find_imgs(url)
		save_img(floder, img_paths)

if __name__ == '__main__':
	download_mm()





