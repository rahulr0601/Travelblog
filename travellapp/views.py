from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from . models import blog

# Create your views here.





def fun(request):
    obj = place.objects.all()
    obj1 = blog.objects.all()
    return render(request, "index.html", {'results': obj,'blogs': obj1})


def addition(request):
    num1  = int(request.GET["num1"])
    num2  = int(request.GET["num2"])
    num3 = num1+num2
    return  render(request,'result.html',{"add": num3})

def update_blog(request):
    updateblog = blog.objects.all()
    return render(request,"update_blog.html",{'updateblog': updateblog})