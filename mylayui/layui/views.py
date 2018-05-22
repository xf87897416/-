from django.shortcuts import render,HttpResponse
from layui import models
# Create your views here.
def test(request):
    if request.method=="GET":
        print("用户已经创建")
        # for i in range(0,100):
        #     obj=models.Cuetomer.objects.create(name='我是%s号'%i,age=i)
        return render(request, 'test1.html')
    if request.method=="POST":
        print(request.POST.get("time"))

    return render(request, 'test1.html')



def test2(request):
    if request.method=="GET":
        return HttpResponse("GET")
    if request.method=="POST":
        print("来取数据了")
        return HttpResponse("POST")






