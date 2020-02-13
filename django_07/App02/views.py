from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from App02.models import User
from django_07.settings import COUNT_OF_PAGE


def list_user(request, page=1):
    data = User.objects.all()
    print(data)
    # 生成分页器
    paginator = Paginator(data, COUNT_OF_PAGE)
    # 获取分页对象
    pager = paginator.page(int(page))

    return render(request, 'app02/list.html', context={
        'pages': pager,
        'page_range': paginator.page_range
    })