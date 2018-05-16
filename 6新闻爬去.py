import urllib.request
import re,random,string
'''


'''
url="http://news.sina.com.cn/"
data=urllib.request.urlopen(url).read()
data2=data.decode("utf-8","ignore")
pat='href="(http://news.sina.com.cn/\w/.*?)"'
allurl=re.compile(pat).findall(data2)
print(len(allurl))
print(allurl)
num=0
for i in range(0,len(allurl)):
    thisurl=allurl[i]
    num=num+1

    file="F:\BaiduNetdiskDownload\第4章 Urllib库实战\/news/"+ str(num)+".html"
    urllib.request.urlretrieve(thisurl,file)

















