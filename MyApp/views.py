from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def welcome(request):
    print('进来了')
    return render(request,'welcome.html')

def home(request):

    return render(request,'welcome.html',{"whichHTML":"Home.html","oid":""})

#返回子页面
def child(request,eid,oid):
    return render(request, eid)
