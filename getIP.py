import urllib.request
import re
# 获取代理ip
url = 'http://www.xicidaili.com/'
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0')
response = urllib.request.urlopen(req)
# print(response)
html = response.read().decode('utf-8')
# print(html)
ip_list = re.findall(r'((?:(?:[01]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d?\d|2[0-4]\d|25[0-5]))[^\d]+(\d{2,4})',html)
# print(ip_list)
list = []
for each in ip_list:
	# print(each)
	list.append(each[0]+':'+each[1])
print(list)




