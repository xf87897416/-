from django.shortcuts import render,HttpResponse
from layui import models
from django.core import serializers

# Create your views here.
def test(request):
    if request.method=="GET":
        print("用户已经创建")
        # for i in range(0,100):
        #     obj=models.Cuetomer.objects.create(name='我是%s号'%i,age=i)
        return render(request, 'test1.html')
    if request.method=="POST":
        print(request.POST.get("time"),'time')

    return render(request, 'test1.html')

import json

def getinfo(request):
    if request.method=="GET":
        print("get_info geT")
        return HttpResponse("GET")
    if request.method=="POST":
        print('page',request.POST.get("start"))
        page=request.POST.get("start")

        print("来取数据了")
        data=models.Cuetomer.objects.filter(id=page).values('name')[0]['name']
        print(data)
        ret = {'status': False, 'mydata': ''}
        ret['mydata'] = data
        # return render(request,'test1.html',{mydata:'123'})
        return HttpResponse(json.dumps(ret))





