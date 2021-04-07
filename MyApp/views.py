from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required
def welcome(request):
    print('进来了')
    return render(request,'welcome.html')

@login_required
def home(request):
    return render(request,'welcome.html',{"whichHTML":"Home.html","oid":""})

#返回子页面
def child(request,eid,oid):
    return render(request, eid)

#进入登陆页面
def login(request):
    return render(request,'login.html')

#开始登陆
def login_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']


    #开始联通django用户库,查看用户名密码是否正确
    from django.contrib import auth
    user = auth.authenticate(username=u_name,password=p_word)

    if user is not None:
        #进行正确的动作
        #return HttpResponseRedirect('/home/')
        auth.login(request,user)
        request.session['user'] = u_name
        return HttpResponse('成功')
    else:
        #返回前端告诉用户名/密码不对
        return HttpResponse('失败')

#注册
def register_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']

    # 开始联通django用户表
    from django.contrib.auth.models import User
    try:
        user = User.objects.create_user(username=u_name,password=p_word)
        user.save()
        return HttpResponse('注册成功！')
    except:
        return HttpResponse('注册失败~用户名好像已经存在~')

#退出登陆
def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')

#吐槽函数
def tijiao(request):
    tucao_text=request.GET['tucao_text']