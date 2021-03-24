from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def welcome(request):
    print('进来了')
    return render(request,'welcome.html')
#test
def aa():
    pass