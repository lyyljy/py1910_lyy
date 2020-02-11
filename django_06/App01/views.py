from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App01.forms import RegisterForm
from App01.models import User


def register(request):
    if request.method == 'POST':
        # 验证数据
        # 1 把提交过来的数据request.POST生成表单对象
        form = RegisterForm(request.POST)
        # 2 通过form的is_valid来检测数据是否合格，合格返回True，不合格返回Flse
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            user = User(username=username,password=password,email=email,phone=phone)
            user.save()
            return HttpResponse("首页")
        else:
            return render(request, "register.html", locals())
    else:
        # get请求
        form = RegisterForm()
        return render(request, 'register.html',locals())