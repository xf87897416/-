import urllib.request
import re

url='http://blog.csdn.net'
# url='http://dig.chouti.com/'


header=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[header]
data=opener.open(url).read()
urllib.request.install_opener(opener) #添加为全局
data=urllib.request.urlopen(url).read().decode('utf-8','ignore')

print(data)



































