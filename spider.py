		############Python爬虫#################


###################网页爬取################################################
# import urllib.request
# weburl = 'http://' + input('Please input the weburl :')  #取得要爬取的页面的url
# webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0'}
# req = urllib.request.Request(url=weburl, headers=webheader)
# webPage = urllib.request.urlopen(req) #得到页面对象(urllib.request.urlopen())
# data = webPage.read()  #读取页面内容
# with open('E:/python/result','wb') as f:
# 	f.write(data)   ##抓取到的数据写入文件
# 	print('抓取网页成功')
	# print(type(webPage))
	# print(webPage.geturl())
	# print(webPage.info())
	# print(webPage.getcode())
###################网页爬取#####################################################


#######################爬取网站的图片###############################
###############太消耗内存了，应该先存入到文件，再从文件读取
import urllib.request
import socket
import re
import sys
import os

targetDir = 'E:/pythonLoad' #文件保存路径
def destFile(path):
	if not os.path.isdir(targetDir):
		os.mkdir(targetDir)
	pos = path.rindex('/')
	t = os.path.join(targetDir, path[pos+1:])
	print(t)
	return t 
if __name__ == '__main__':   #程序运行入口
	# weburl = 'http://' + input('想要爬取的网址：')
	weburl = 'http://news.baidu.com/'
	webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0'}
	req = urllib.request.Request(url=weburl, headers=webheader)  #构造请求报头
	webpage = urllib.request.urlopen(req)  #发送请求报头
	# while webpage != '':
	contentBytes = webpage.read()
		# with open('E:/python/result','wb+') as f:
		# 	f.write(contentBytes)
	success = 0
	fail = 0 
	# while True:
		# with open('E:/python/result','rb') as f:
	for link, t in set(re.findall(r'(http:[^s]*?(jpg|png|gif))', str(contentBytes))):  #正则表达式查找所有的图片
		print('downloading from',link)
		try:
			urllib.request.urlretrieve(link, destFile(link))  #下载图片
			success +=1
		except:
			print('失败')
			fail += 1
		# if f.readline == '':
		# 	break
	print('end.成功：%s张，失败：%s张' %(success, fail))
####################################################################


















