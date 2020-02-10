from django.http import request, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # 生成响应对象
        res = HttpResponse("生成cookie")
        # 以秒为单位的过期时间
        res.set_cookie("username", username, max_age=3*60*60)
        print(res) #<HttpResponse status_code=200, "text/html; charset=utf-8">
        return res
    return render(request, "app01/login.html")


def reply(request):
    # 获取cookie中的username键值对
    username = request.COOKIES.get("username")
    # username不为空就是登录过，否则未登录
    if username:
        return HttpResponse("发表评论")
    else:
        return redirect(reverse("App01:login"))


def index(request):
    username = request.COOKIES.get("username")
    return render(request, "app01/index.html", context={"username":username})


def logout(request):
    # 生成响应对象
    res = redirect(reverse("App01:home"))
    print(res)
    res.delete_cookie("username")
    return res