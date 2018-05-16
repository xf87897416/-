import urllib.request
import re


def user_proxy(url,addr):
    proxy=urllib.request.ProxyHandler({'http':addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    return data

url='http://taobao.com'
addr="139.196.144.222:9999"
data=user_proxy(url,addr)
print(len(data))





















