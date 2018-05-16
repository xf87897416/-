import urllib.request


'''
urlretrieve   下载网页到本地
urlcleanup   清楚缓存
info    环境信息
getcode    代码
geturl    获取url

'''
# req=urllib.request.urlopen('http://www.baidu.com',timeout=1)
# print(req.info())



# urllib.request.urlretrieve('http://www.hellobi.com',filename="F:\BaiduNetdiskDownload\第4章 Urllib库实战\mytest.html")
# urllib.request.urlcleanup()
file=urllib.request.urlopen('http://www.hellobi.com',timeout=1)
wrong=0
for i in range(0,10):
    try:
        file = urllib.request.urlopen('http://www.hellobi.com', timeout=0.3)
        data=file.read()
        print(len(data))

    except Exception as e:
        print("出现异常!")
        global wrong
        wrong=wrong+1
print(str((10-wrong)*10)+"%")






















