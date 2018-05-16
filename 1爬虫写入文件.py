import re
import urllib.request

data=urllib.request.urlopen("https://read.douban.com/provider/all").read().decode('utf-8')

pat='<div class="name">(.*?)</div>'
result = re.compile(pat).findall(data)
print(result)

# wenzi="你好不好啊，我不是很好啊，他好吗？"
# print(re.compile(u'好+[\u4e00-\u9fa5]+').findall(wenzi))

# strr='<div>hello word</div> my house is so big,我的then i sale my house'
# pat='(.*?)'
# result=re.compile(pat).findall(strr)
# print(result)

fh =open("F:\BaiduNetdiskDownload\第4章 Urllib库实战\/test.txt","w")
for i in range(0,len(result)):
    fh.write(result[i]+"\n")
fh.close()







