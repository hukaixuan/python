import urllib.request
import random

url = 'http://www.whatismyip.com.tw'
iplist = ['118.26.62.234:3128','118.26.143.202:3128','117.114.129.122:3128']

# 1.参数是一个字典{'类型':'代理ip:端口号'}
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
# 2.定制、创建一个opener
opener = urllib.request.build_opener(proxy_support)
# 3.安装opener(临时使用的话可选 )
urllib.request.install_opener(opener)
# 4.调用opener
response = opener.open(url)
html = response.read().decode('utf-8')

print(html)

##可不可以从ip代理的网页上爬取免费代理ip进行代理





