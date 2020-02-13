from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from App01.forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('username'))
            print(form.cleaned_data)
            return HttpResponse("首页")
        else:
            print(form.errors)
            return render(request, "app01/register.html", locals())
    return render(request, "app01/register.html")


def verify(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        # 验证
        if form.is_valid():
            return HttpResponse("验证通过")
        else:
            return render(request, 'app01/login.html', locals())
    form = LoginForm()
    return render(request, 'app01/login.html', locals())


def send_sms(request):
    from App01.SMS import sms
    from random import randint
    # 判断是ajax请求
    if request.is_ajax():
        # 获取手机号
        phone = request.POST.get('phone')
        # 生成随机验证码
        code = randint(1000, 9999)
        # 把验证码存入session
        request.session['code'] = code
        request.session.set_expiry(20*60)  # 1200秒后失效

        # 拼接模板参数
        param = "{'number':%d}" % code
        # 发送
        res = sms.send(phone, param)
        print(code, phone)
        return JsonResponse({'code': 1})
    else:
        # 生成随机验证码
        code = randint(1000, 9999)
        # 拼接模板参数
        param = "{'number':%d}" % code
        # 发送
        res = sms.send('15733190269',param)
        print(res)
        print(type(res))
        return HttpResponse(f"已发送{code}")


def sms_login(request):
    if request.method == 'POST':
        # 验证短信验证码
        yzm = request.POST.get('yzm')
        # 从session获取存入验证码
        code = str(request.session.get('code'))
        print(code, yzm)
        print(type(code), type(yzm))
        if yzm == code:
            return HttpResponse("验证成功")
    return render(request, 'app01/sms.html')