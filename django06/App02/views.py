from django.http import request, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def login(request):
    if request.method == "POST":
        # 获取用户名和密码
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 设置session
        request.session['username'] = username
        request.session['password'] = password
        return redirect(reverse("App02:index"))
    return render(request, "app02/login.html")


def index(request):
    # 获取session
    username = request.session.get("username")
    password = request.session.get("password")
    print(username, password)
    return render(request, "app02/index.html", context=locals())


def logout(request):
    # 删除单个session键值对
    del request.session['password']
    del request.session["username"]
    return redirect(reverse("App02:index"))