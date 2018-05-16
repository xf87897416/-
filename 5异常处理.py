import urllib.error
import urllib.request

'''

try:
    urllib.request.urlopen("http://dig.chouti.com/")
except urllib.error.URLError as e:
    print("有异常")
    if hasattr(e,"code"):
        print(e.code,'----')
    if hasattr(e,"reason"):
        print(e.reason,'=====')
'''
import urllib.request
url="http://blog.csdn.net/"
header=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[header]
data=opener.open(url).read()
fh=open("F:\BaiduNetdiskDownload\第4章 Urllib库实战\mytest4.html",'wb')
fh.write(data)
fh.close()








