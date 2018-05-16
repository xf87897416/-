import urllib.request
import sys

'''

'''

keywd="python语言"
keywd=urllib.request.quote(keywd)
url="http://www.baidu.com/s?wd="+keywd
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fh=open("F:\BaiduNetdiskDownload\第4章 Urllib库实战\mytest2.html",'wb')
fh.write(data)
fh.close()





















