import urllib.request
import urllib.parse

'''

'''
url='http://127.0.0.1:8009/test/'
mydata=urllib.parse.urlencode({
    'name':'xf',
    'passwd':'abcd421'
}).encode('utf-8')

req=urllib.request.Request(url,mydata)

data=urllib.request.urlopen(req).read()
fh=open("F:\BaiduNetdiskDownload\第4章 Urllib库实战\mytest3.html",'wb')
fh.write(data)
fh.close()









